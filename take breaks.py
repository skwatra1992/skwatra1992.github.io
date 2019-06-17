#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 16:46:41 2019

@author: skwatra@us.ibm.com
Multiple programs in 1
"""

# take breaks every 2 hours while working

"""import numpy as num
import webbrowser
import time

count = 3
breaks = 0

print("The program started on" + time.ctime())
while(breaks<count):
    time.sleep(2*60*60)
    webbrowser.open_new('https://www.youtube.com/watch?v=xaRHgUS_49Q')
    breaks = breaks +1
    

       """  
    


#remove numbers from images stored on pc

import os
def rename_files():
    file_list = os.listdir("/Users/skwatra@us.ibm.com/Desktop/Python/prank")
    print (file_list)
    print (type(file_list))
    saved_path = os.getcwd()
    print("current directory is" + saved_path)
    os.chdir("/Users/skwatra@us.ibm.com/Desktop/Python/prank")
      
    for file_name in file_list:
        os.rename(file_name, file_name.translate(str.maketrans('','','1234567890')))
    print (file_list)
    os.chdir(saved_path)

rename_files()

        
    #os.renames(old, new)

#rename_files()
