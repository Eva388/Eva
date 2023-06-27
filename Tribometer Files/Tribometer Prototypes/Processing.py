assert os.path.exists("./config.py"), "config file is missing, please include the config.py file in the working folder"
assert os.path.exists(config.RAW_PATH), "make sure that the folder with the raw data exists"
assert len(listdir(config.RAW_PATH)) == 1, "make sure that the folder with the raw data contians a single raw dataset"

from os import listdir 
import os
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import config

#Initialize and check folder contents/structure
if not os.path.exists(config.RAW_PATH):
    os.mkdir(config.RAW_PATH)
if not os.path.exists(config.CLEAN_PATH):
    os.mkdir(config.CLEAN_PATH)
    
    
#Clean up old files
for file in listdir(config.CLEAN_PATH)[1:]:
    os.remove(config.CLEAN_PATH + file)
   
#Start with cleaning up RAW data and putting it in a temporary file
file = config.RAW_PATH + listdir(config.RAW_PATH)[1]    
with open(file, 'r') as data:
    with open(config.CLEAN_PATH+ "temp.csv",'w') as output:
        skipping = True
        skip_once = False
        interval_skip = False
        File_Name = None
        
        for line in data:
            
            #If a name is found then update the file_prefix
            if line.startswith("\"Name:"):
                file_prefix = str(line)[15:-2]
            
        
            #Check if the current interval should be skipped and set file extension if needed
            if line.startswith("\"Interval:"):
                if line.endswith("1\"\n"):
                    interval_skip = True
                    
                elif line.endswith("2\"\n"):
                    file_ext = "_fwd"
                    file_name = file_prefix + file_ext
                    output.write("NAME:"+file_name+"\n")
                    interval_skip = False
                    
                elif line.endswith("3\"\n"):
                    file_ext = "_rev"
                    file_name = file_prefix + file_ext
                    output.write("NAME:"+file_name+"\n")
                    interval_skip = False
            
            
            #Check if the interval starts and then start outputing to the file
            if line.startswith("\"Meas. Pts.") and interval_skip == False:
                skipping = False
                output.write(line)
                
                #the single line below should still be skipped
                skip_once = True
                continue
            
            #Check if interval has ended and update the skipping flag
            if line == "\"\"\n" and skipping == False:
                output.write("\n")
                skipping = True
            
            
            if skip_once:
                skip_once = False
                continue
            if interval_skip: continue
            if skipping: continue
            
            output.write(line)
            

#Splitting up the temporary file into the required individual datasets
with open(config.CLEAN_PATH+ "temp.csv", 'r') as data:
    
    file_name = None
    
    for line in data:
        
        if line.startswith("NAME:"):
            file_name = str(line)[5:-1]
            continue   
        if line == "\n":continue
        
        with open(config.CLEAN_PATH + file_name + ".csv", 'a') as file:
            if line == "":continue
            
            line.replace("\"", "")
            
            file.write(line)
            
#removing the temporary file