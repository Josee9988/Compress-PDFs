#!/usr/bin/env python3

import os
from fnmatch import fnmatch
from pylovepdf.ilovepdf import ILovePdf
from pathlib import Path
import shutil
import glob
import time
import zipfile
import re
import sys

ALL_PDFS_PATTERN = "*.pdf"
COMPRESSED_PDFS_PATTERN = "*compress*.pdf"
COMPRESSED_ZIP_PATTERN = "*compress*.zip"
REGEX_ADDED_COMPRESSED_FILE_NAME = "_compress_\d\d\-\d\d\-\d\d\d\d"
pdf_files = []
compressed_pdfs = []

# path found as first argument
if len(sys.argv) > 1 and os.path.exists(Path(sys.argv[1]).resolve()):
    ACTION_PATH = sys.argv[1]
else:  # path not found or not defined (use the current working directory)
    ACTION_PATH = os.getcwd()


ilovepdf = ILovePdf(
    'project_public_04c63dae8446159db1ea601538ef45ed_BO_347a60cf121bc09ba69d8e6327ed792dc9', verify_ssl=True)
task = ilovepdf.new_task('compress')

for path, subdirs, files in os.walk(ACTION_PATH):
    for name in files:
        if fnmatch(name, ALL_PDFS_PATTERN):
            pdf_files.append(os.path.join(path, name))

for file in pdf_files:
    print("Uploading: "+file)
    task.add_file(file)
    task.set_output_folder(ACTION_PATH)
    task.file.set_metas('Title', file)
task.execute()
task.download()
task.delete_current_task()

time.sleep(3)  # wait for the task to finish

# unzip the downloaded compressed pdf files
zip_file_location = glob.glob(ACTION_PATH + "/" + COMPRESSED_ZIP_PATTERN)[0]
with zipfile.ZipFile(zip_file_location, 'r') as zip_ref:
    zip_ref.extractall(ACTION_PATH)
time.sleep(5)
compressed_pdfs = glob.glob(os.path.join(ACTION_PATH, COMPRESSED_PDFS_PATTERN))

# replace the recently compressed files to their original file location
for original_file in pdf_files:
    for compressed in compressed_pdfs:
        compressed_file = re.sub(
            REGEX_ADDED_COMPRESSED_FILE_NAME, '', compressed)
        if compressed_file[compressed_file.rindex("/")::] in original_file:
            if os.path.exists(Path(original_file).resolve()) and os.path.exists(Path(compressed).resolve()):
                print("Replacing "+compressed+" to "+original_file)
                shutil.move(Path(compressed), Path(original_file))
            else:
                print("\033[1;31;40mE:\033[0m Couldn't replace: " +
                      compressed+" to " + original_file)

# delete zip file
os.remove(zip_file_location)
