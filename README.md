# caplan-cleaning-2.0
The second and final version of the project to scrape, clean, and import Bryan Caplan's old blog posts.

main is my primary control code

NukeNonBryan is a QOL change I made from 1.0. 1.0 ran on a full mirror of EconLog. For 2.0, I used this method to delete all the files which I didn't want to upload, which both saved time in running the primary program, and let me simplify my main. I did more hard-coding here than I should have, and I ran it seperately instead of calling it from main. But as a one-off component of a one-off project, I thought it was worthwhile anyway.

checkByline identifies EconLog posts as being written by Bryan. Unchanged from 1.0, but now called by NukeNonBryan rather than an if statement in main

XMLFormat contains two methods, one to initialize the xml outfile (delete it if it exists as residue from a previous run, then add the xml preamble), and another to add the xml postamble.

XMLDump copies xml-formatted content from the original hmtl files to the outfile. Biggest change from 1.0 is to the date-identifcation, which was done (badly) by hand in 1.0, and uses dateutil's parser in 2.0

listCleaning cleans line separated list of published articles copy/pasted from Substack, removing superfluous data (publication date, byline, etc.) to produce a machine-readable list of posts successfully uploaded after deployment of the 1.0 version of this project

listCompare tests a hypothesis for why 1.0 failed. The hypothesis was that the uploader could only handle so many lines of xml, and so only uploaded the first N files. This program created a dict of the first N files run by the 1.0 version, and compared it against the output of listCleaning (see inline comments for implementation details). The result found no more overlap between uploaded and first files than would be expected by chance, so the hypothesis was falsified.

removeUploaded deletes files and folders referenced by the output of listCleaning.

In addition to these scripts, I also used XmlLint to debug the xml files. This is how I identified the date malformation that caused the problems in the 1.0 version.

Using these scripts, I successfully uploaded 5107 of Bryan's 5112 EconLog posts.
