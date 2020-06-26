import os
import sys
import re
import logging
import tokenize
import linecache
from PIL import Image

def save_normal(arg_width, current_image_width, arg_length, current_image_height, current_file):
 new_image = current_image.resize((arg_width,arg_length), Image.ANTIALIAS)
 new_image.save(current_file)

def save_forced(arg_width, current_image_width, arg_length, current_image_height, current_file):
 new_image = Image.new('RGB', (arg_width, arg_length), (255, 255, 255, 255))
 offset = ((arg_width - current_image_width) // 2, (arg_length - current_image_height) // 2)
 new_image.paste(current_image, offset)
 new_image.save(current_file)

arg_param_valid = True
if len(sys.argv) != 5:
 arg_param_valid = False
if arg_param_valid:
 arg_mode = sys.argv[1]
 arg_type = sys.argv[2]
 arg_width = int(sys.argv[3])
 arg_length = int(sys.argv[4])
 x=os.getcwd() 
 folder = x+"./butternaan"
 folder1=x+"./butternaan1"
 i=1
 for file in os.listdir(folder):
  newName = file
  if arg_mode == "copy":
   newName = "t"+file
   current_file = os.path.join(folder, file)
   current_image = Image.open(current_file, 'r') 
   current_image_width, current_image_height = current_image.size
   current_file = os.path.join(folder1, newName)

   if arg_type == "normal": 
     if arg_width <= current_image_width and arg_length <= current_image_height:
       save_normal(arg_width, current_image_width, arg_length, current_image_height, current_file)
   elif arg_type == "forced":
     if arg_width <= current_image_width and arg_length <= current_image_height:
       save_normal(arg_width, current_image_width, arg_length, current_image_height, current_file)
     else:
       save_forced(arg_width, current_image_width, arg_length, current_image_height, current_file)
   else:
       print("The length of parameter is not valid.")