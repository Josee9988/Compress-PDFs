#!/usr/bin/env python3

import os
from fnmatch import fnmatch
from pylovepdf.ilovepdf import ILovePdf
import shutil
import glob
import time
import zipfile
import re

pdf_files = []
compressed_pdfs = []

os.chdir(os.getcwd())
filepath=os.listdir()

arr = os.listdir()

ilovepdf = ILovePdf('project_public_04c63dae8446159db1ea601538ef45ed_BO_347a60cf121bc09ba69d8e6327ed792dc9', verify_ssl=True)
task = ilovepdf.new_task('compress')

for path, subdirs, files in os.walk(os.getcwd()):
    for name in files:
        if fnmatch(name, "*.pdf"):
            pdf_files.append(os.path.join(path, name))


for file in pdf_files:
    print("Uploading: "+file)
    task.add_file(file)
    task.set_output_folder(os.getcwd())
    task.file.set_metas('Title', file)
task.execute()
task.download()
task.delete_current_task()

time.sleep(3); # wait for the task to finish

# unzip the downloaded compressed pdf files
with zipfile.ZipFile(glob.glob("*compress*.zip")[0], 'r') as zip_ref:
    zip_ref.extractall(os.getcwd())
time.sleep(5);
compressed_pdfs = glob.glob("*compress*.pdf")

# replace the recently compressed files to their original file location
for okfile in pdf_files:
    for compressed in compressed_pdfs:
        a = re.sub("_compress_\d\d\-\d\d\-\d\d\d\d", '', compressed)
        if a in okfile:
            print("Replacing "+compressed+" to "+okfile)
            shutil.move(compressed, okfile)

# delete zip file
os.remove(os.getcwd()+"/"+glob.glob("*compress*.zip")[0])
