from pathlib import Path
import collections


# Initial local file config
comment_id_data = "Comments_ID.txt"
author_name_data = "Blacklist_Names.txt"
dbfolder = "data/"
max_size = 1000


# Create the local data folder if it doesn't exist
Path(dbfolder).mkdir(parents=True, exist_ok=True)


def init_data():    
    with open(f"./{dbfolder+comment_id_data}", 'a+'):
        print(f"{comment_id_data}.txt created!")
    with open(f"./{dbfolder+author_name_data}", 'a+'):
        print(f"{author_name_data}.txt created!")


def getComments():
    """Get all comment IDs from the txt file
    :return list: All comment IDs.
    """
    with open(f"./{dbfolder+comment_id_data}", 'r') as inp:
        f = inp.read()
        result = [x.strip() for x in f.split('\n') if x]
    return result


def writeComment(id):
    """Write a comment ID to the txt file
    :param str id:  The comment ID to record
    """
    #fcircular buffer maintain only max_size in txt and delete - fifo
    comments = collections.deque(getComments(), maxlen=max_size)
    comments.append(id)
    with open(f"./{dbfolder+comment_id_data}", 'w') as out:
        out.write('\n'.join(list(comments)))


def getBlacklist():
    """Get all author names from the txt file
    :return set: All author names.
    """
    with open(f"./{dbfolder+author_name_data}", 'r') as inp:
        f = inp.read()
        result = {x.strip() for x in f.split('\n') if x}
    return result


def blacklistAuthor(author):
    """Blacklist a author name by adding it to the txt file
    :param str author:  The author to record
    :return True if new username is added else False
    """
    if author == None:
        return False
    authors = getBlacklist()
    temp = authors.copy() 
    authors.add(author)
    if (len(authors) == len(temp)):
        return False
    with open(f"./{dbfolder+author_name_data}", 'w') as out:
        out.write('\n'.join(authors))
    return True


def whitelistAuthor(author):
    """Whitelist a author name by removing it from the txt file
    :param str author:  The author to remove
    :return True if new username is removed else False
    """
    if author == None:
        return False
    authors = getBlacklist()
    try:
        authors.remove(author)
    except KeyError:
        return False
    with open(f"./{dbfolder+author_name_data}", 'w') as out:
        out.write('\n'.join(authors))
    return True


try:
    init_data()
except:
    pass