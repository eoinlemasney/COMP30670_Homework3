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
    
    # this regular expression will give us the command and the rectangular bounding box
    # https://docs.python.org/2/library/re.html#re.MatchObject.group
    
    pat = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")
    def __init__(self, L):
        
        self.size=L
        # Initialisation of 2D array.
        self.array=[[False]*L for _ in range(L)]
  
    def get_cmd(lines):    
        
    
        pat = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")
        file = read_file(sys.argv[2])
        # function to parse the input to a usable format 

        lines = pat.finditer(file)
        cmd, x1, y1, x2, y2 = Seater.pat.match(line).groups()
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        return cmd, x1, y1, x2, y2


def read_file(input_link):
    '''Function which reads in a file from a URL or local file and returns the
    contents of the file in a string'''
    
    if input_link.startswith("http://"):
        req=urllib.request.urlopen(input_link)
        text=req.read().decode('utf-8')
        print("Reading from the http")
    else:
        text=open(input_link,'r').read() #.read() converts to a string
    return text


def main():
    #pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    pat = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")
    if len(sys.argv) < 3:
        print( file_input, "\nCheck the parameters, no file given.\nInput should be of form 'led_checker --input file_link'")

    else:
        '''use regular expression and create a line for each in file'''

        file = read_file(sys.argv[2])
        print(file)
        arraySize=int(file.split("\n")[0])
        print("This is the array size", arraySize)
        lines = pat.finditer(file)
        
        for line in lines:
            print(line)      
        
        
                                                    
if __name__ == "__main__":
    main()
