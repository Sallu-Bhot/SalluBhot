import random
import re
from triggers import trigger_dictionary, quotes


def find_word_in_text(text, word):
    """
    Finds if a word is within a text

    :param text: The text to search
    :param word: Word to look for in text
    :return: True if the word appears as a word in the text, False otherwise
    """
    found = re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search(text)
    if found:
        return True
    return False

#send in author name as param with text
def get_comment_reply(text, author):
    """
    Takes the text of a comment, determines which reply to use for it

    :param text: Reddit comment text
    :return: String to reply with for a keyword, Random quote if no Keyword is found
    """
    random.seed()
    for triggers, responses in trigger_dictionary.items():  # For every case in trigger_dictionary
        for trigger in triggers:  # For each string in the cases
            if find_word_in_text(text, trigger):  # If the Reddit comment contains the string
                num = random.randint(0, len(responses) - 1)
                response = responses[num] 
                if "{}" in response: #check if string has {} and author
                    response = response.format(author)
                return response #Return a random string that corresponds to the matched tuple
    
    num = random.randint(0, len(quotes) - 1)
    response = quotes[num]
    if "{}" in response: #check if string has {} and author
        response = response.format(author)
    return response
