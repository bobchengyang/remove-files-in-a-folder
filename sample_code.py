import os
import glob

files = glob.glob('/resources/data/Negative/*')
for f in files:
    os.remove(f)
print('removed all images in Negative folder')
files = glob.glob('/resources/data/Positive/*')
for f in files:
    os.remove(f)
print('removed all images in Positive folder')
