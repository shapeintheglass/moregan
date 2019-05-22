import argparse
import os
import shutil
import zipfile
from zipfile import ZipFile

parser = argparse.ArgumentParser(description='Example usage: python moregan.py --name MorganKarlFemale')
parser.add_argument('--name', help='Name to copy. Must come from src/ without the file ext.')
args = parser.parse_args()

# Current dir the script is in, same as output dir.
pwd = os.path.dirname(os.path.realpath(__file__)) + '\\'
# Source files. Just expect this to be in the same dir as the script.
src = 'src\\'
# Objects path to use for when packing the files.
path = 'objects\characters\humansfinal\\'
# File extension
ext = 'cdf'

# The source file we will be duplicating.
srcfile_path = pwd + src + args.name + '.' + ext

# Make sure source file exists.
os.stat(srcfile_path)

# Temporary zip archive to hold all files.
zipfile_path = pwd + args.name + '.zip'

with ZipFile(zipfile_path, 'w') as zip:
  for filename in os.listdir(pwd + src):
    # Copy chosen file into the zip file but with the other file name.
    if filename.endswith(ext):
      zip.write(srcfile_path, path + filename, zipfile.ZIP_DEFLATED)

# Rename the .zip to a .pak
pakfile = 'patch_' + args.name + '.pak'
shutil.move(zipfile_path, pwd + pakfile)

# Zip one more time for good measure.
# Uncomment if you want to send this to someone else in a handy zip file.
#with ZipFile(zipfile_path, 'w') as zip:
#  zip.write(pwd + pakfile, pakfile, zipfile.ZIP_DEFLATED)