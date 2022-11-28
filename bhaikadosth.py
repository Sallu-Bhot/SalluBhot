import praw
import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "bhai-ka-driver-bot": {
        "reddit": praw.Reddit(
                    client_id=os.getenv("driver_client_id"),
                    client_secret=os.getenv("driver_client_secret"),
                    password=os.getenv("driver_password"),
                    user_agent=os.getenv("driver_user_agent"),
                    username=os.getenv("driver_username")
                )
                }
        }