__author__ = 'Shrestha, Sumit'
import os
rootdir='/Users'
size_filter=4000000
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        try:
            if size_filter <= os.path.getsize(os.path.join(subdir, file)):
                print (os.path.join(subdir, file),os.path.getsize(os.path.join(subdir, file)),"bytes")
        except FileNotFoundError:
            pass
