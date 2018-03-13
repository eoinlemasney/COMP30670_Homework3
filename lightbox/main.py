# -*- coding: utf-8 -*-

"""Main module."""
import sys
import click
import urllib.request
import argparse 
import requests 
from urllib.request import urlopen
import os
import re

# its a good idea to make a class to hold the various bits of data 
# and functions we need to solve this problem
class LightBox:
    
    # the rectangular bounding box
    
    
    def __init__(self, L, file_path):
        
        self.size=L
        # creates 2D array
        self.read_file(file_path)
        self.array=[[False]*L for _ in range(L)]
  
    def get_cmd(self):    
        #regular exp to give us the commands
        pat = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")
        
        # function to parse the input to a usable format 
        #finditer will allow us to find multiple patterns as opposed to just finding the pttern and exiting
        # and then we itter through each appearance of the group to go through every strinf 
        lines = pat.finditer(self.text)
        self.instructions = []
        
        count = 0
        for line in lines:
            while count < 1000:
                print("This is a line", line.groups())
                print ("count is ",count)
                self.instructions.append(line.groups())
                count += 1
        print ("This is line.groups", line.groups)
        cmd, x1, y1, x2, y2 = pat.match(line).groups()
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        print("printing from the get_cmd method now")
        return cmd, x1, y1, x2, y2
    
    def assign(self):
        if line.groups == 'turn on':
            a = line.group
            print (line.group)

        
        
 #   def turn_on():
    
 #   def turn_off():
        
  #  def switch():
        


    def read_file(self, input_link):
        '''Function which reads in a file from a URL or local file and returns the
        contents of the file in a string'''

        if input_link.startswith("http://"):
            req=urllib.request.urlopen(input_link)
            self.text=req.read().decode('utf-8')
            print("Reading from the http")
        else:
            self.text=open(input_link,'r').read() #.read() converts to a string
            print("This should not be printed")
        


def main():
    #pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    pat = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")
    if len(sys.argv) < 3:
        print( file_input, "\nCheck the parameters, no file given.\nInput should be of form 'led_checker --input file_link'")

    else:
        '''use regular expression and create a line for each in file'''
        print("reading from the main now")
        lightBox = LightBox(5, sys.argv[2])
        lightBox.get_cmd()
        lightBox.assign()
        

        
        
        
        
        
        
       # file_text = read_file(sys.argv[2])
       # arraySize=int(file_text.split("\n")[0])
       # print("This is the array size", arraySize)
      #  lines = pat.finditer(file_text)
        
     #   instructions = []
     #   for line in lines:
       #     print(line.groups())
     #       instructions.append(line.groups())
    #
        
        
                                                    
if __name__ == "__main__":
    main()