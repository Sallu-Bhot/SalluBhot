from response import get_comment_reply
from utils import *


class SALLU_BHOT:
    def __init__(self):
        
        load_dotenv()
        
        # Set the bot's username
        self.bot_username = os.getenv('sallu_username')
       
        # Initialize a Reddit object
        self.reddit = praw.Reddit(
            client_id=os.getenv('sallu_client_id'),
            client_secret=os.getenv('sallu_client_secret'),
            password=os.getenv('sallu_password'),
            user_agent=os.getenv('sallu_user_agent'),
            username=os.getenv('sallu_username')
        )

        # Set the subreddits to monitor join with '+'
        self.subreddit = self.reddit.subreddit('sallu_bhot_test')
        #self.subreddit = self.reddit.subreddit('sallu_bhot_test+biggboss+BollyBlindsNGossip')
        
        #webhook url for discord notifications
        self.webhook_sb = os.getenv('webhook_sb')

        print(f"Configuration complete, Starting {self.bot_username}!")


    def send_webhook(self, message):
        """ Send Notification to Discord Server """

        data = {'content': message, 'username': 'Sallu-bhot'}
        requests.post(self.webhook_sb, data=data)


    def send_errors(self, error, redditObject):
        """ Sending Error To Discord """

        if "NoneType' object has no attribute 'name" in error:
            pass
        else:
            print(error)
            error = f"{error}\nhttps://www.reddit.com{redditObject.permalink}"
            self.send_webhook(error)


    def getText(self,redditObject):
        if isComment(redditObject):
            user_text = redditObject.body.lower()
        else:
            user_text = redditObject.title.lower() + "\n" + redditObject.selftext.lower()

        return user_text.strip()


    def make_comment(self, redditObject, response):
        """Reply to (comment/post) with response and Store ID in txt"""

        try:
            #reply to submission
            redditObject.reply(body=response)

            #store id of already replied submissions in txt
            writeComment(redditObject.id)

            #Send Discord Notification
            link = f"\n{redditObject.author.name}: {self.getText(redditObject)}\nResponse: **'{response}'** \nLink - https://www.reddit.com{redditObject.permalink}"
            self.send_webhook(link)

        except Exception as e:
            error = str(e)
            self.send_errors(error, redditObject)


    def response_canon(self, redditObject, text, author, sub):
        """Sending a Keyword specific / random response to a triggered Submission"""

        response = get_comment_reply(text, author, sub)
        self.make_comment(redditObject, response)


    def response_greet(self,redditObject, title):
        """Sending a Greeting to Shukravar ka vaar/ Shanivaar Ka Vaar Discussion Thread"""
        response = f"*Hello, Namaste, Assalamu Alaikum, Sat Sri Akal, Kem Cho, Kedo Haal Hai, Kemon Acho, Kasa Kai. Welcome to BiggBoss {title}!*"
        self.make_comment(redditObject, response)


    def skip_checker(self, redditObject):
        """Check to see if we should skip this thing"""

        #Skip posts older than 7 hrs
        if not checkTime(redditObject):
            return True

        # Skip if the author is None (Someone deleted something)
        if redditObject.author.name is None:
            return True

        # Skip if the author is Sallu-Bhot
        elif redditObject.author.name == 'Sallu-Bhot':
            return True

        # Skip if the comment ID is in the txt file already
        elif redditObject.id in getComments():
            return True

        # Otherwise, don't skip.
        else:
            # print(f"This {id} has a valid author, and is not in the txt")
            return False


    def blacklist_checker(self, redditObject, user_text, author):
        """ blacklist/whitelist an author based on keywords - start/stop """

        if user_text.strip() == "/unblock":
            if(whitelistAuthor(author)):
                message = f"🟩 USER: **'{author}'** is UNBLOCKED\nLink - https://www.reddit.com{redditObject.permalink}"
                print(message)
                self.send_webhook(message)
                writeComment(redditObject.id)
                return True
        elif user_text.strip() == "/block":
            if(blacklistAuthor(author)):
                    message = f"🟥 USER: **'{author}'** BLOCKED!\nLink - https://www.reddit.com{redditObject.permalink}"
                    print(message)
                    self.send_webhook(message)
                    writeComment(redditObject.id)
                    return True
        else:
            return False

    
    def sallu_main(self, redditObject):
        """Primary Function"""
        
        if self.skip_checker(redditObject):
            print(f"Skipping https://www.reddit.com{redditObject.permalink}")
            return

        #get info
        author = redditObject.author.name
        user_text = self.getText(redditObject)
        subreddit = redditObject.subreddit.display_name
        if(isPost(redditObject)):
            post_title = redditObject.title.lower()
        else:
            post_title = ""

        #change sallu_bhot_test to biggboss for testing
        if subreddit == "sallu_bhot_test":
            subreddit = "biggboss"

        # Black list authors/ Whitelist authors (reply to bot comment with /block or /unblock)
        if isComment(redditObject) and len(user_text.split()) == 1 and user_text[0] == "/":
            parent_author = redditObject.parent().author
            if parent_author == self.bot_username:
                if (self.blacklist_checker(redditObject, user_text, author)):
                    return True
            
        # Skip if the author is blacklisted
        if redditObject.author.name in getBlacklist():
            return

        #check both common trigger for posts and specific trigger for post and comments
        if triggered(user_text) or (isPost(redditObject) and luck(post_title)):
            print(f"Triggered, on https://www.reddit.com{redditObject.permalink}")
            self.response_canon(redditObject, user_text, author, subreddit)
            return
        
        #greet on fri and sat discussion thread
        if isPost(redditObject) and redditObject.link_flair_text == "Scheduled Discussion Thread":
            fri = "Shukravar Ka Vaar"
            sat = "Shanivaar Ka Vaar"
            if fri.lower() in post_title:
                title = fri
            elif sat.lower() in post_title:
                title = sat
            else:
                title = ""
            if (title):
                print(f"Greeting Triggered, on https://www.reddit.com{redditObject.permalink}")
                self.response_greet(redditObject, title)

        
        
    def run(self):
        print("\nStreaming Comments and Posts...")

        while True:
            try:

                # Iterate through all the posts / comments
                for object in praw.models.util.stream_generator(lambda **kwargs: submissions_and_comments(self.subreddit, **kwargs)):
                    self.sallu_main(object)
                    

            except KeyboardInterrupt:
                print("Keyboard termination received. Shutting Down!")
                break
            
            except Exception as e:
                body = f"Stream Error:\n{e}"
                print(body)
                self.send_webhook(body)
                time.sleep(2)


if __name__ == '__main__':
    sb = SALLU_BHOT().run()