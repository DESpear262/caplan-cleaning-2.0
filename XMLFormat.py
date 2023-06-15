import os


def XMLInit(filename):                                                          #Method to initialize the xml file
    if os.path.exists(filename):
        os.remove(filename)                                                     #Delete the file if it exists (from an earlier run of this program, saves having to delete them by hand
    with open(filename, 'a', encoding='utf-8') as out:
        #Dumps the xml preamble from a known-working xml file to the new xml
        out.write('''<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"   
	xmlns:content="http://purl.org/rss/1.0/modules/content/"
	xmlns:wfw="http://wellformedweb.org/CommentAPI/"
	xmlns:dc="http://purl.org/dc/elements/1.1/"
	xmlns:atom="http://www.w3.org/2005/Atom"
	xmlns:sy="http://purl.org/rss/1.0/modules/syndication/"
	xmlns:slash="http://purl.org/rss/1.0/modules/slash/"
	>

<channel>
	<title>Bryan Caplan &#8211; Econlib</title>
	<atom:link href="https://www.econlib.org/feed/?author_name=bcaplan" rel="self" type="application/rss+xml" />
	<link>https://www.econlib.org</link>
	<description>The Library of Economics and Liberty</description>
	<lastBuildDate>Tue, 17 May 2022 14:34:34 +0000</lastBuildDate>
	<language>en-US</language>
	<sy:updatePeriod>
	hourly	</sy:updatePeriod>
	<sy:updateFrequency>
	1	</sy:updateFrequency>
	<generator>https://wordpress.org/?v=5.8.6</generator>''')

def XMLClose(filename):                                                             #Method to close out the xml file
    with open(filename, 'a', encoding='utf-8') as out:
        #Code below dumps the xml postamble
        out.write('''     
	</channel>
</rss>''')