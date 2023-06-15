import os
from tqdm import tqdm
from bs4 import BeautifulSoup



def checkUploaded(to_check, uploaded):
    try:
        with open(to_check, 'r', encoding='utf-8') as inp:
            soup = BeautifulSoup(inp, 'html.parser')

        title = str(soup.find("title"))
        title = title[:-18] + title[-8:]
        title = title[7: -8]
        if title in uploaded:
            return True
        return False
    except OSError:
        pass


directory_name = "D:\\Caplan\\www.econlib.org"      #Target directory
uploaded = "D:\\Caplan\\cleaned.txt"                #List of uploaded posts, line-separated list output by listCleaning

#####################
#Code for deployment#
#####################

uploadedSet = set()                                 #init set

with open(uploaded, encoding="utf8") as f:
    for line in f:
        uploadedSet.add(line[:-1])                  #Converts line-separated list to a set (with \n's sliced out) to reduce time complexity if I ended up needing to run this on the 5000 post repo to remove 2000 posts or something like that

#loop through all files in directory = directory_name
for path, subdirs, files in tqdm(os.walk(directory_name)):
    for name in files:
        if checkUploaded(f'{path}\\{name}', uploadedSet):
            os.remove(f'{path}\\{name}')
            try:
                os.rmdir(path)
            except:
                pass
