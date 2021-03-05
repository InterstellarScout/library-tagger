# Library Tagger
This project is used to organize your library and output a catalog of what is where, 
and what is in each directory and item.  

##Main Features:
- Separate PDF's or files with the same name into folders
- Output a file with the names and contents of everything in the directory. 
- This program can run over an already sorted set, and mark what has not been marked. 
- It will use a PDF's metadata to get Author, Title, and Genre.
- The Genre is also generated based on the file directories. For example, if you have your book 
"aftermath_vol1" saved in the directories /Literature/Comics/Fiction/Fantasy/, you will get
three genre's, Literature, Comics, Fiction, and Fantasy. The base directory is defined by where the script is sitting. 
- It can grab the first page of a PDF and save it as a JPG for previews.

##What's includes?
There are two script included in this project:
1. LibraryTagger.py
2. FileOrganizer.py

LibraryTagger.py is intended to run against a library of files and folders that have already been 
broken apart into directories. 

The FileOrganizer.py is intended to run against a single directory that has not been organized into folders. It works
a lot like another project located at https://github.com/InterstellarScout/file-organizer

##Usage:
1. Update the walk_dir with the directory you will me organizing. 
2. Run the command: ```python3 LibraryTagger.py```


##Dependencies:
- Python3
- os
- math import log
- re
- PyPDF2
- Poppler for Windows (see below)

##Installing Poppler:
In order to get a jpg of the first page of a PDF, you need Poppler. 
1. Use the included package or download the package from https://blog.alivate.com.au/poppler-windows/
2. With the package, unzip it and place the contents into your user's Program Files. 
3. Go into the deployed folder and grab the URL.
4. Press your start button and search for "system environment variables" Press enter.
5. At the bottom of the pop up, click the button "Environmental Variables" 
6. In the new Pop Up, go to the second box labeled "System Variables" and find "Path". Double click it. 
7. In the new Pop Up, go to the bottom of the list and paste the URL to the poppler folder.
8. Restart your IDE

At the end of this, our script can now access the components offered by Poppler.


##Samples:

The index.txt created in a directory looks like this:
```
Title=Aftermath #1 : Ares
Author=Humanoids Inc-Hudnall, James-Vigouroux, Mark
Genre1=Literature
Genre2=Comics
Genre3=Fiction
Genre4=Fantasy
``` 
NOTE: In addition to the PDF's Genre, the scripts creates a Genre based on the PDF and the folder directory. 
(See note in Main Features)

This project is meant to work with the Library Navigator (Upcoming Project) that is a GUI to navigate your library and 
take advantage of everything this script creates. 