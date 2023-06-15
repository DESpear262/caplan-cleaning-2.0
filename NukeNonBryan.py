import os
from tqdm import tqdm

from checkByline import *

directory_name = "D:\\Caplan\\www.econlib.org"      #Target directory

#####################
#Code for deployment#
#####################



#loop through all files in directory = directory_name
for path, subdirs, files in tqdm(os.walk(directory_name)):
        for name in files:
            if len([s for s in [
                "@",
                ".html.1",
                "\\wp-",
                "www.econlib.org\\library",
                "www.econlib.org\\econlog",
                "www.econlib.org\\econtalk",
                "www.econlib.org\\res\\img",
                "www.econlib.org\\GQE"
            ] if s in f"{path}\\{name}"]) > 0: #feed files contain comments, which I don't need for this project, @ implies printer-friendly or otherwise redundant content
                os.remove(f"{path}\\{name}")
            else:
                if not checkByline(f"{path}\\{name}") or not name.endswith(".html"):
                    os.remove(f"{path}\\{name}")

deleted = set()

for path, subdirs, files in tqdm(os.walk(directory_name, topdown=False)):
    for name in path:
        still_has_subdirs = any([subdir for subdir in subdirs if os.path.join(path, subdir) not in deleted])

        if len(files) == 0 and not still_has_subdirs:
            try:
                deleted.add(path)
                os.rmdir(path)
            except:
                pass
