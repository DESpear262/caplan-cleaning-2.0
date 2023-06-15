from bs4 import BeautifulSoup
from dateutil import parser
from datetime import datetime


def XMLDump(infile, outfile):
    try:
        # Open the html file and Parse it
        # using Beautiful soup's html.parser.
        with open(infile, 'r', encoding='utf-8') as inp:
            soup = BeautifulSoup(inp, 'html.parser')

        title = str(soup.find("title"))                                 #Find line containing title
        title = title[:-18] + title[-8:]                                #Remove EconLog tag
        #Find the lines containing the jumbotron (article tags, publication date, etc.)
        header = str(soup.find("section", {"class": "article-single-page jumbotron main-banner econlog-logo-wide-center"}))
        date = datetime.today()                                         #init datetime object
        for p in header.splitlines(True):                               #Read jumbotron line-by-line
            try:                                                        #Try to parse each line as a datetime object
                if "div class" not in p:                                #fuzzy=True was necessary to get parser to work despite the html tags, but it also parsed the div class line as a datetime, so I had to tell it to ignore those
                    temp = parser.parse(p, fuzzy=True)
                    #Replace date with the info from the line. parser failed to identify the year in the line, for some reason, so I had to manually slice out that part of the string to pass to replace
                    date = date.replace(year=int(p[-9:-5]), day=temp.day, month=temp.month).date()
            except ValueError:
                pass

        #Manually compose the link out of folder names from the scrape
        link = "https:/"
        for subdir in infile.split("\\")[2:-1]:
            link = f'{link}/{subdir}'

        #Copy over the actual blog post, with some superfluous stuff manually sliced out
        content = str(soup.find("div", {"class": "post-content"}))[26: -7]

        # Open a output.xml file and write the modified content.
        with open(outfile, 'a', encoding='utf-8') as out:
            out.write(f'''
            <item>
                {str(title)}
                <link>{link}</link>
                <pubDate>{date}</pubDate>
                    <content:encoded><![CDATA[{content} 
                    <p>The post <a rel="nofollow" href="{link}">{title}</a> appeared first on <a rel="nofollow" href="https://www.econlib.org">Econlib</a>.</p>
                ]]></content:encoded>
            </item>''')
            #I did mess the pointer to EconLog part up. I just used {title} which included the <title> and </title> tags. This means the link didn't actually show up in the post
            #If I had the ability and inclination to redo this, I'd slice out those tags
            #But I don't want to delete ~5000 Substack posts just to add that pointer
            #In fairness, I warned EconLog that if I had to do this by hand, there was a good chance I'd mess up the pointers to the original hosts
            #They declined to cooperate
            #As above, so below; as without, so within, I suppose

    except Exception as e:                                                  #Some of the files failed to parse. I don't grok html enough to figure out why
        print(f"{infile}:\n{e}\n\n")
