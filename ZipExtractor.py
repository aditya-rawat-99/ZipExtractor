import os, zipfile, sys

extractFile = zipfile.ZipFile(sys.argv[1])

extractFile.extractall(sys.argv[2])
