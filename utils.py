from datetime import *
from data import *
from response import *
import requests
import time
import praw
import prawcore
import os
from dotenv import load_dotenv


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


def checkTime(obj):
    """ Return true fro posts older than certain amount of time (hours = 7) else False """
    time = obj.created
    timestamp = datetime.fromtimestamp(time)
    if (datetime.now() - timedelta(hours=7)) < timestamp:
        return True
    else:
        return False


def luck(text):
    """ 1:10 chance of being triggered with common keywords """

    random.seed()
    keys = ["sallu", "salman", "bhoi", "selmon", "savlon"]
    if random.randrange(10) < 1:
        if any(key in text for key in keys):
            return True
    else:
        return False


def triggered(text):
    """ Triggered only with specific keywords """

    key = [ ".*\\bsallu bot\\b.*", ".*\\bsallu bhot\\b.*", ".*\\bsallu b\\b.*"]
    combined = "(" + ")|(".join(key) + ")"
    if re.search(combined, text):
        return True
    else:
        return False