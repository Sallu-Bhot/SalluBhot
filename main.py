from response import get_comment_reply
from utils import *
import requests

class SALLU_BHOT:
    def __init__(self):

        # Load in credentials from .env
        load_dotenv()
        # Set the bot's username
        self.bot_username = os.getenv('sallu_username')

        print(f"STARTING {os.getenv('sallu_username')}")
       
        # Initialize a Reddit object
        self.reddit = praw.Reddit(
            client_id=os.getenv('sallu_client_id'),
            client_secret=os.getenv('sallu_client_secret'),
            password=os.getenv('sallu_password'),
            user_agent=os.getenv('sallu_user_agent'),
            username=os.getenv('sallu_username')
        )

        #webhook url for discord notifications
        self.webhook_sb = os.getenv('webhook_sb')

        # Set the subreddit to monitor
        #self.subreddit = self.reddit.subreddit('sallu_bhot_test')
        self.subreddit = self.reddit.subreddit('sallu_bhot_test+biggboss')

        # Set the subreddit stream to comments and posts
        #self.stream = praw.models.util.stream_generator(lambda **kwargs: submissions_and_comments(self.subreddit, **kwargs))
        
        #bhaikadosth config
        self.army = config

    def send_webhook(self, message):
        data = {'content': message, 'username': 'Sallu-bhot'}
        requests.post(self.webhook_sb, data=data)

    def send_errors(self, body, comment):
        """Print Error"""

        if "NoneType' object has no attribute 'name" in str(body):
            pass
        else:
            print(body)
            body = f"{body}\nhttps://www.reddit.com{comment.permalink}"
            try:
                if "RATELIMIT" in str(body):
                    user = self.army['bhai-ka-driver-bot']
                    res = "Sorry sir, Bhai ~~has been rate-limited~~ is working out and may miss tags. Sab mera galti hai!"
                    driver_comment = user['reddit'].comment(id=comment.id)
                    driver_comment.reply(body=res)
                    writeComment(comment.id)
                    body += "\nDriver has apologized!."


                self.send_webhook(body)
                             
            except Exception as e:
                body += "BHAI KA DRIVER ERROR: {}".format(e)
                print(body)
                self.send_webhook(body)
                pass

    
    def getText(self,redditObject):
        if isComment(redditObject):
            user_text = redditObject.body.lower()
        else:
            user_text = redditObject.title.lower() + "\n" + redditObject.selftext.lower()

        return user_text

    """Sending a normal, random response"""
    def response_canon(self,redditObject,comment):
        try:
            response = get_comment_reply(comment, redditObject.author.name)

            redditObject.reply(body=response)

            #store id of already replied submissions in DB
            writeComment(redditObject.id)
            
            link = f"\n{redditObject.author.name}: {self.getText(redditObject)}\nResponse: **'{response}'** \nLink - https://www.reddit.com{redditObject.permalink}"
            self.send_webhook(link)

        except Exception as e:
            body = "https://www.reddit.com"+redditObject.permalink + " - " + str(e)
            self.send_errors(body, redditObject)



    """Check to see if we should skip this thing"""
    def base_response_checks(self,redditObject):
        skip = False

        if not checkTime(redditObject):
            skip = True

        elif (not isComment(redditObject)) and (redditObject.link_flair_text == "no entry sallu bhot"):
            skip = True

        # Skip if the author is none, or Vizzy.
        elif redditObject.author == None or redditObject.author.name == self.bot_username:
            skip = True

        # I'm really scared of him going crazy again, man...
        elif "sallu-bhot" in str(redditObject.author.name.lower()):
            skip = True

        elif redditObject.author.name.lower() == 'sallu-bhot':
            skip = True

        elif redditObject.author.name.lower() == 'bhai-ka-driver':
            skip = True
        
        else:
            # Read in comments we've made
            readComments = getComments()

            # Skip if we've already read this comment.
            if redditObject.id in readComments:
                skip = True

        return skip


    """Get all the info we need about a comment to respond to it"""
    def comment_processer(self,redditObject):
        user_text = redditObject.body.lower()

        return user_text


    """Get all the info we need about a post to respond to it"""
    def post_processer(self, redditObject):
        user_text = redditObject.title.lower() + "\n" + redditObject.selftext.lower()
        return user_text


    """Splitting up between comments and posts, uses the above two functions"""
    def firstlook(self, redditObject):
        # Gather needed info if it's a comment
        if isComment(redditObject):
            user_text = self.comment_processer(redditObject)

        # Gather information if it's a post
        else:
            user_text = self.post_processer(redditObject)

        # Make sure there's nothing the bot will consider an extra line(not sure)
        """
        if f"{redditObject.author.name}: " in user_text:
            user_text = user_text.split(f"{redditObject.author.name}: ")[0]
        """
        is_triggered = triggered(user_text)

        return user_text, is_triggered

    
    """Primary Function"""
    def sallutime(self, redditObject):

        skip = self.base_response_checks(redditObject)

        if skip:
            print(f"Skipping https://www.reddit.com{redditObject.permalink}")
            return

        else:
            user_text, triggered = self.firstlook(redditObject)

            try:

                if triggered:
                    '''
                    If there's a normal Sallu Bhot trigger on a comment/post
                    '''
                    print(f"Triggered, on https://www.reddit.com{redditObject.permalink}")

                        # Send a canon response
                    self.response_canon(redditObject, user_text)
            except:
                pass

    def run(self):
        while True:
            try:
                for posts in praw.models.util.stream_generator(lambda **kwargs: submissions_and_comments(self.subreddit, **kwargs)):
                    try:
                        self.sallutime(posts)
                    except Exception as e:
                        body = f"Sallu Bhot Error Report:\n{e}"
                        print(body)
                        time.sleep(2)
                        pass
            except (praw.exceptions.PRAWException, prawcore.exceptions.PrawcoreException) as e:
                body = f"Reddit Stream Error Report:\n{e}"
                print(body)
                self.send_webhook(body)
                time.sleep(2)
            except KeyboardInterrupt:
                print("Keyboard termination received. Shutting Down!")
                break
            except Exception:
                body = f"Unexpected Error Report:\n{e}"
                print(body)
                time.sleep(2)

if __name__ == '__main__':
    sb = SALLU_BHOT().run()