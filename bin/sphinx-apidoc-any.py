# very simple python code that goes through all julia files
# and extract content into a restructured file

import os, glob
from shutil import move
from os import remove
import re

import argparse

parser = argparse.ArgumentParser(
  description ='Extracts rst content from comments in all source files',
  epilog      ="that's all")

parser.add_argument('-s',help='source folder')
parser.add_argument('-o',help='destination folder')
parser.add_argument('-e',help='source code extension, for example py or jl')
parser.add_argument('-c',help="comment selector, for example #' ")

args = parser.parse_args()

DOC_FOLDER = "./source/"
SRC_FOLDER = "../julia/"
CMT_SELECT = "#'"

if (args.o != None):
  DOC_FOLDER = args.o
if (args.s != None):
  SRC_FOLDER = args.s
if (args.c != None):
  CMT_SELECT = args.c

def extract(file_in, file_out, startstr):
  directory = os.path.dirname(file_out)
  some_content = False
  if not os.path.exists(directory):
    os.makedirs(directory)
  with open(file_out, 'w') as target_file:
    with open(file_in, 'r') as source_file:
      beginp = True
      for line in source_file:
        if line.startswith(startstr):
          some_content = True
          if beginp:
            target_file.write("\n")  
            beginp = False
          target_file.write(line.replace(startstr, ""))
        else:
          beginp = True

  if some_content:
    print "done with " + file_in
  else:
    print "done with " + file_in + " but empty"
    remove(file_out)


# for loop on all files
filelist = glob.glob(SRC_FOLDER + "**/*." + args.e) + glob.glob(SRC_FOLDER + "/*." + args.e)

for f in filelist:
  # create new file by replacing the extension
  outname = re.sub(r'.[a-z]?$',"rst",f)
  outname = outname.replace(SRC_FOLDER,DOC_FOLDER)
  extract(f,outname,"#'")

