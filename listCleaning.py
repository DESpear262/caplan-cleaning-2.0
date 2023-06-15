content = ""

with open("D:\\Caplan\\toclean.txt", encoding="utf8") as f:     #toclean.txt is a file copy-pasted from Substack's list of published articles into a notepad doc
    for line in f:
        if len([s for s in [
            "By Bryan Caplan",                                  #This is a list of superfluous lines which were also copied over from Substack
            "0\n",
            "N/A",
            "Opened",
            "Views",
            "New subs",
            " 2005\n",                                          #In hindsight, I probably should have just used dateutils parser function to find the date lines, but I didn't for some reason
            " 2006\n",
            " 2007\n",
            " 2008\n",
            " 2009\n",
            " 2010\n",
            " 2011\n",
            " 2012\n",
            " 2013\n",
            " 2014\n",
            " 2015\n",
            " 2016\n",
            " 2017\n",
            " 2018\n",
            " 2019\n",
            " 2020\n",
            " 2021\n",
            " 2022\n"] if s in line ]) == 0:
            content += line                                     #Merge lines which aren't junk into content

with open("D:\\Caplan\\cleaned.txt", 'a', encoding='utf-8') as out:
    out.write(str(content))                                     #Dump content to cleaned.txt
