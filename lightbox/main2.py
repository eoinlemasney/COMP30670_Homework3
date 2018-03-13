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

class Led_Box():
    '''Defining Led_Box class'''
    def __init__(self, L):
        '''Board is initialized with an LxL array, with every value set to 
        -1 i.e. false is equal to off. This is the value used to indicate a light is off
        this will create an array of 1000 rows and columns
        '''
        self.array=[[False]*L for _ in range(L)]
        self.size=L
        
    def apply (self, parseline):
        
        pat = read_file.re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")
        cmd, x1, y1, x2, y2 = pat.match(file).groups()
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        return cmd, x1, y1, x2, y2
        
    def read_file(input_link):
        pat = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")

        '''Function which reads in a file from a URL or local file and returns the
        contents of the file in a string'''

        if input_link.startswith('http://'):

            req = urllib.request.urlopen(input_link)
            text = req.read().decode('utf-8')
            print ("File has been read Eoin!")
            return pat.text
        
        
        else: 
            text =open(input_link,'r').read() #.read() converts to a string

            return pat.text

def single_line(read_line):
    pat = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")
    read_line = pat.read_file
    







def main():
    print ("hello",apply(sys.argv[2])
    
    '''  
    if len(sys.argv) < 3:
        print( file_input, "\nCheck the parameters, no file given.\nInput should be of form 'led_checker --input file_link'")

    else:
        file_input = read_file(sys.argv[2])
        print(file_input)
        file= read_file(file_input)
        #print (file_input)
        
     '''                                             
if __name__ == "__main2__":
    main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''


#argparse stuff
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

group.add_argument("-i", "--input", action="store_true")
#group.add_argument("-f", "--file", action="store_true")

parser.add_argument("source", help="a valid url")
args = parser.parse_args()




def read_file(filename):
    """Function to read a file and process the contents"""
    if filename.startswith("http"):
        req = urllib.request.urlopen(filename)
        line =req.read().decode('utf-8')
        print ("File has been read")
        return line
    else:
        if not os.path.isfile(filename):
            print('File does not exist.')
        else:
        # Open the file for reading as a string
            line = open(filename, 'r').read()
            return line
'''''