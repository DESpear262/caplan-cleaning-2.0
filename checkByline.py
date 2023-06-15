def checkByline(file):
    with open(file, encoding="utf8") as f:
        for line in f:
            if '<!-- <a href="https://www.econlib.org/' in line:                                        #Token string which uniquely identifies a byline in EconLog
                return 'author/bcaplan/" class="author url fn" rel="author"> -->Bryan Caplan' in line   #Token string which, given an Econlog byline, uniquely identifies Bryan's byline