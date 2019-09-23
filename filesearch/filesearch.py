import os

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

# With a dedicated function?
"""
def searchExt(directory,extension):
    '''searches a a given directory tree for specific file types'''
    for f in directory:
        if extension in f:
            return f
"""

print('Welcome to File search, below you will enter a directory')
print('Please enter the EXACT directory path, case sensitive, filesystem order and so on...')

files = input('Please enter a directory.....') #take a string to pass to the function

print('Thanks! Now what kind of file do we want? e.g. .jpg .doc .pdf and so forth....')

extension = input('Please specify a file extension: ') #ask for a file extension

print('All files of extension ' + str(extension) + ' in the dir & sub-dir you entered include: ')

search = getListOfFiles(files)
#print(search)

#print(searchExt(search, extension))

for f in search:
    if extension in f:
        print(f)

# With a nested for loop?
'''
for f in files:
    for sf in os.walk(files):
        if extension in f:
            print(f)
'''



