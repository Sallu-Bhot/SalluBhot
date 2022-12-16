from datetime import *
from data import *
from bhaikadosth import *
import re


def submissions_and_comments(subreddit, **kwargs):
    results = []
    results.extend(subreddit.new(**kwargs))
    results.extend(subreddit.comments(**kwargs))
    results.sort(key=lambda post: post.created_utc, reverse=True)
    return results


def isPost(obj):
    return isinstance(obj,praw.models.Submission)

def isComment(obj):
    return isinstance(obj,praw.models.Comment)

def triggered(text):
    key = [ ".*\\bsallu bot\\b.*", ".*\\bsallu bhot\\b.*", ".*\\bsallu b\\b.*"]
    # Make a regex that matches if any of our regexes match.
    combined = "(" + ")|(".join(key) + ")"

    if re.search(combined, text):
        return True
    return False



def checkTime(obj):
    time = obj.created
    timestamp = datetime.fromtimestamp(time)
    print(timestamp)
    #skip post older than certain amount of time
    if (datetime.now() - timedelta(hours=7)) < timestamp:
        return True
    else:
        # print("Skipping old comment.")
        return False

#Check if post is scheduled discussion thread posted on Friday/Saturday
def checkPost(obj, user_text):
    try:
        print(f'post - {user_text}')
        time = obj.created
        timestamp = datetime.fromtimestamp(time)
        #monday - 0, friday, saturday - 4,5 
        weekday = timestamp.weekday()

        if obj.link_flair_text == "Scheduled Discussion Thread":
            if weekday in [4,5]:
                if 'vaar' in user_text:
                    return True
        return False
    except Exception as e:
        body = f"Chekpost Error:\n{e}"
        print( body)