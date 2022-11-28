from pathlib import Path

# Initial local file config
txtname = "SalluData.txt"
dbfolder = "data/"

# Create the local data folder if it doesn't exist
Path(dbfolder).mkdir(parents=True, exist_ok=True)

def init_data():    
    f = open(f"./{dbfolder+txtname}", 'a+')
    f.close()

def getComments():
    """Get all comment IDs from the txt file
    :return list: All comment IDs.
    """
    with open(f"./{dbfolder+txtname}", 'r') as file:
        f = file.read()
        result = [x.strip() for x in f.split('\n') if x]
    return result


def writeComment(id):
    """Write a comment ID to the txt file
    :param str id:  The comment ID to record
    """
    with open(f"./{dbfolder+txtname}", 'a+') as file:
        file.write(f"{id}\n")

try:
    init_data()
except:
    pass