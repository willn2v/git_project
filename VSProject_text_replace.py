import os
import sys
import fileinput
from fnmatch import fnmatch

textToSearch = "Debug|x64"
textToReplace = "Vuong/Loan"

root = "."
path = os.path.join(root, "targetdirectory")
pattern = "*.sln"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            fileToSearch = os.path.join(path, name)
			#Replace the text
            print("File to search: {}".format(fileToSearch))
            tempFile = open( fileToSearch, 'r+' )
            for line in fileinput.input( fileToSearch ):
               #if textToSearch in line :
               #   print('Match Found')
               tempFile.write( line.replace( textToSearch, textToReplace ) )
            tempFile.close()

print ('Done!!!')
input( '\n\n Press Enter to exit...' )