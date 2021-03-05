import os
from math import log
import re
from PyPDF2 import PdfFileReader

##The following is used for "infering spaces" from a String.
#Reference/Source https://stackoverflow.com/questions/8870261/how-to-split-text-without-spaces-into-list-of-words
# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).


#walk_dir = sys.argv[1]
walk_dir = r"C:\Users\user\OneDrive\LiteraryResources\Literature\Astronomy"
print('walk_dir = ' + walk_dir)

print(os.path.isdir(walk_dir))

directory_contents = ""
folderCount = 0
fileCount = 0

print('walk_dir = ' + walk_dir)

def upper_infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""
    words = open("upperCommonWordsAndNames.txt", encoding="utf8").read().split()
    wordcost = dict((k, log((i + 1) * log(len(words)))) for i, k in enumerate(words))
    maxword = max(len(x) for x in words)

    # Find the best match for the i first characters, assuming cost has been built for the i-1 first characters. Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))

def upper_infer_caps(s):
    #split into word via spaces
    #uppercase first letter of each
    #MUST COME IN LOOKING LIKE THIS
    #Or this I guess. It will always leave
    #Or This I Guess. It Will Always Leave
    out = s.split(" ")

    newOut = []
    for word in out:
        word = word.lower()
        word = word[0:1].upper()+word[1:]
        newOut.append(word)

    return " ".join(newOut)

def lower_infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""
    words = open("lowerCommonWordsAndNames.txt", encoding="utf8").read().split()
    wordcost = dict((k, log((i + 1) * log(len(words)))) for i, k in enumerate(words))
    maxword = max(len(x) for x in words)

    # Find the best match for the i first characters, assuming cost has been built for the i-1 first characters. Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))

def old_lower_infer_caps(s):
    """Uses dynamic programming to infer the location of spaces in a string without spaces."""
    words = open("lowerCommonWordsAndNames.txt", encoding="utf8").read().split()
    wordcost = dict((k, log((i + 1) * log(len(words)))) for i, k in enumerate(words))
    maxword = max(len(x) for x in words)

    # Find the best match for the i first characters, assuming cost has been built for the i-1 first characters. Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    newOut = []
    for word in out:
        word = word[0:1].upper()+word[1:]
        newOut.append(word)

    #return " ".join(reversed(out))
    return "".join(reversed(newOut))

def lower_infer_caps(s):
    #Split the string via spaces
    out = s.split(" ")

    newOut = []
    for word in out:
        word = word.lower()
        word = word[0:1].upper()+word[1:]
        newOut.append(word)

    return " ".join(newOut)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# Reference: https://stackoverflow.com/questions/2212643/python-recursive-folder-read
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)
    list_file_path = os.path.join(root, 'my-directory-list.txt')
    print('list_file_path = ' + list_file_path)
    directory_contents = directory_contents + 'list_file_path = ' + list_file_path + "\n"

    for subdir in subdirs: #For each subdirectory in this directory
        print('\t- subdirectory ' + subdir + "\n")
        directory_contents = directory_contents + '\t- subdirectory ' + subdir + "\n"
        folderCount = folderCount + 1

    extensionList = list()
    cleanFolderFileList = list()
    duplicateFileList = list()
    fullPathList = list()
    directoryModified = 0

    hasFiles = 1
    for filename in files: #For each file in this directory
        just_file_path = os.path.join(root)
        file_path = os.path.join(root, filename)

        #Track the contents of the directory
        splitList = filename.split(".")
        if len(splitList) != 2:
            if len(splitList) > 2: #if it's greater than 2, connect the first elements and return a list of two items.
                # {x.y.z}.{pdf}
                print("Fixing multiple periods in name.")
                #x,y,z,pdf
                #0,1,2,3

                countDown = len(splitList) - 1 #convert to list. Countdown is the largest number- contains .pdf
                firstPiece = ""
                while (countDown >= 1):
                    if countDown == len(splitList) - 1:
                        firstPiece = firstPiece + splitList[countDown - 1]
                    else:
                        firstPiece = splitList[countDown - 1] + "." + firstPiece
                    countDown = countDown - 1
                splitList[0] = "".join(firstPiece)
                splitList[1] = splitList[len(splitList)-1]
                # print("Created " + splitList[0])
            else:
                # print("Invalid File Name + [" + filename + "]")
                exit()
        # This will take the extention and be used to track what's in the directory later.
        # print("Found: " + splitList[0])
        # print("Full string is " + str(splitList[0]) + "(period)" + str(splitList[1]))
        extensionList.append(splitList[1])
        duplicateFileList.append("".join(splitList[0]+"."+splitList[1]))
        # This makes a list of the file name without the extension and special characters. TO be used to make folders
        cleanFolderFileList.append(''.join(e for e in "".join(splitList[0]) if e.isalnum()))

        # IF the file is a pdf, take the first page, save as PNG
        title = ""
        author = ""
        try:
            if splitList[1] == "pdf":
            # if a picture already exists
            #if os.path.exists(just_file_path + "\\" + splitList[0] + ".png"):
                # print("Found a pdf " + filename)
                # print("Have " + filename + " Want to save the first page. Save as:" + splitList[0] + '.png' + " in " + file_path)
                # pdfimages -f 1 -l 1 -png Pathfinder08_1418163538.pdf filename

                #This program needs to be local. Get it here: http://blog.alivate.com.au/poppler-windows/
                print("Will run command: " + "pdftoppm -f 1 -l 1 -png \"" + file_path + "\" \"" + just_file_path + "\\" + splitList[0] + "\"")
                output = os.system("pdftoppm -f 1 -l 1 -png \"" + file_path + "\" \"" +
                                   just_file_path + "\\" + splitList[0] + "\"")
                print("Completed saving filename as png. Got Exit Code: " + str(output))

                # Get any other information
                with open(file_path, 'rb') as f:
                    pdf = PdfFileReader(f)
                    info = pdf.getDocumentInfo()
                    number_of_pages = pdf.getNumPages()

                    print(str(info))
                    author = info.author
                    print("Author=" + str(author))
                    title = info.title
                    print("Title=" + str(title))
                    hasFiles = 1
                #else:
                #print("Image exists. Skipping")
        except:
            print("There was an issue working with the PDF.")


        print('\t- file %s (full path: %s)' % (filename, file_path) + "\n")
        fullPathList.append(file_path)
        directory_contents = directory_contents + '\t- file %s (full path: %s)' % (filename, file_path) + "\n"

        if hasFiles == 1:
            # if
            #if os.path.exists(just_file_path + "\\index.txt"):
            # Get Title
            f = open(just_file_path + "\\index.txt", "w+")
            if title is None or title == "":
                # remove all special characters with spaces
                title = re.sub('[^0-9a-zA-Z]+', '', splitList[0])

                # remove numbers in a row if there are more than 4
                numbersInRow = 0
                for letter in title:
                    if letter.isnumeric():
                        numbersInRow = numbersInRow + 1

                    if not letter.isnumeric():
                        numbersInRow = 0

                    if numbersInRow == 5:
                        print("Original:" + title)
                        title = re.sub('[0-9]+', '', title)

                        print("Modified:" + title)
                        break

                #if not splitList[0].isupper():
                    # if everything is lowercase,
                    # infer spaces
                    #title = lower_infer_spaces(title)
                    # infer caps
                    #title = lower_infer_caps(title)
                    #title.strip()  # Remove leading spaces
                #else:
                    # if it is uppercase, ignore this spacing and capsem.
                    #title = splitList[0]
                    # infer spaces
                    #title = upper_infer_spaces(title)
                    # infer caps
                    #title = upper_infer_caps(title)
                    #title.strip()  # Remove leading spaces
                print("Book Title: " + title)
                f.write("Title=" + title + "\n")
            else: # Title is found from the PDF
                f.write("Title=" + str(title) + "\n")

            #Get Genre(s)
            toBreak = file_path.split("\\")
            #C:\Users\das09\Downloads\ToSort\Comics\PathfinderCityOfSecretsIssue4\pathfinder_cityofsec
            startNum = 5
            endNum = len(toBreak)-2 #exclude the file and file folder
            #for each organizational folderp[]\][;
            count = 1
            while startNum < endNum:
                print("Genre" + str(count) + "=" + toBreak[startNum])
                f.write("Genre" + str(count) + "=" + toBreak[startNum] + "\n")
                count = count + 1
                startNum = startNum + 1

            #Add other info
            f.write("Author=" + str(author) + "\n")
            #f.write("title=" + title + "\n")

            f.close()
            print("This directory has files. Julie, Do the thing!")
            hasFiles = 0
            #else:
             #   print("index.txt exists. Skipping")
    directory_contents = directory_contents + "\n"

print("Done reading directories")
print(directory_contents)

with open(walk_dir+r"\DiscorveredPaths.txt", 'wb') as list_file:  # for each path found, report the concents
    list_file.write(directory_contents.encode('utf-8'))
    list_file.write(b'\n')