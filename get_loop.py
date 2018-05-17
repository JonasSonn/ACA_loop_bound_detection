# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:02:15 2018

@author: moth
"""

#fp = open('path/to/file.txt', 'r')  

import sys
import os

def get_simple_for_loop (path) :
   
    
    if not os.path.isfile(path):
       print("File path {} does not exist. Exiting...".format(path))
       sys.exit()
    meat_items = None
    for_loop = {}
    with open(path) as fp:
       cnt = 0
       for line in fp:
           #print("line {} contents {}".format(cnt, line))
           if "for" in line:
               s = line.find("(")
               e = line.find(")")
               meat = line[s+1:e]           
               meat_items = meat.split(";")
               var = meat_items[0]
               condition = meat_items[1]
               expression = meat_items[2]
               if "=" in expression:
                   meat_items[2] = expression.split("=")[1]
               #print("foudn var {0}; condition{1}; expression{2}".format(var, condition, expression))
               
           cnt += 1
           
    if meat_items is None :
        return -1
    else :
        return meat_items
    
    
def get_for_loop_with_var (path) :
   
    
    if not os.path.isfile(path):
       print("File path {} does not exist. Exiting...".format(path))
       sys.exit()
    meat_items = None
    for_loop = []
    with open(path) as fp:
       cnt = 0
       for line in fp:
           #print("line {} contents {}".format(cnt, line))
           if "for" in line:
               s = line.find("(")
               e = line.find(")")
               meat = line[s+1:e]           
               meat_items = meat.split(";")
               var = meat_items[0]
               condition = meat_items[1]
               expression = meat_items[2]
               if "=" in expression:
                   meat_items[2] = expression.split("=")[1]
               #print("foudn var {0}; condition{1}; expression{2}".format(var, condition, expression))
           else : 
               for_loop_body.append(line)
               
         #  if meat_items[0]+" =" in line:
          #    for l in for_loop_body:
             #     if ";"
                  
                  
           #if "}" in line :
           #    break
           cnt += 1
           
    if meat_items is None :
        return -1
    else :
        return meat_items
    

    