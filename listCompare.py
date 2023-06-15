from checkByline import *
from bs4 import BeautifulSoup
import os


def makeDict():
    directory_name = "D:\\Caplan\\www.econlib.org"                      #Target directory, shouldn't be hard-coded but I doubt anyone's going to recycle this code, and it's an easy fix if they do

    comp = {}                                                           #Declare comp as an empty dict to minimize time complexity if removing, say, 2000 posts from a repo of 5000 files
    for path, subdirs, files in os.walk(directory_name):
        for name in files:
            if len([s for s in [
                "@",                                                    #printer-friendly versions
                ".html.1",                                              #Not sure what exactly this indicates, but it's not a normal blog post, so I don't need it
                "\\wp-",                                                #do.
                "www.econlib.org\\library",                             #Main, non-EconLog Library of Econ and Liberty stuff
                "www.econlib.org\\econlog",                             #Econlog info page (author bios, etc.)
                "www.econlib.org\\econtalk",                            #EconTalk podcast pages
                "www.econlib.org\\res\\img",                            #Website data (art assets, etc.)
                "www.econlib.org\\GQE"                                  #Not sure what this is
            ] if
                    s in f"{path}\\{name}"]) > 0:
                pass
            elif len(comp) > 113:                                       #This module was specifically meant to compare the uploaded posts to the non-uploaded posts, since there were 113 original uploads, I only needed to check the first 113 posts
                return(comp)
            else:
                if name.endswith((".html")):                            #There were some non-html items in the folder which threw an exception if I didn't include this
                    if checkByline(f"{path}\\{name}"):
                        try:
                            # Open the html file and Parse it
                            # using Beautiful soup's html.parser.
                            with open(f"{path}\\{name}", 'r', encoding='utf-8') as inp:
                                soup = BeautifulSoup(inp, 'html.parser')


                            title = str(soup.find("title"))             #Find line containing html title
                            title = title[:-18] + title[-8:]            #Remove EconLog tag
                            title = title[7:-8]+"\n"                    #Remove <title> and </title> html tags
                            comp.setdefault(title, 1)                   #Add resulting cleaned title to the comp dict with a value of 1
                        except:
                            pass


comp = makeDict()
file = "D:\\Caplan\\cleaned.txt"                                        #line-separated list of successfully uploaded files output by listCleaning.py

with open(file, encoding="utf8") as f:
    for line in f:
        comp[line] = comp.get(line, 0) - 1                              #line-by-line add the elements of cleaned.txt to the comp dict, with value equal to current value -1 with a default value of 0 if they don't exist
                                                                        #This makes elements only in the first 113 of the original repo keys with values of 1, elements only in the uploaded list have values of -1, and elements in both have values of 0
print(comp)