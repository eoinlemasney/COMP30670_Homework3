# -*- coding: utf-8 -*-

"""Main module."""
import sys
import click
import urllib.request
import argparse 
import requests 
from urllib.request import urlopen
import os


def read_file(input_link):
    '''Function which reads in a file from a URL or local file and returns the
    contents of the file in a string'''
    if input_link.startswith('http://'):
        
        req = urllib.request.urlopen(input_link)
        text = req.read().decode('utf-8')
        print ("File has been read Eoin!")
        return text
        
        
    else: 
        text =open(input_link,'r').read() #.read() converts to a string
        
        return text
        





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

def main():
        
        if len(sys.argv) < 3:
            print( file_input, "\nCheck the parameters, no file given.\nInput should be of form 'led_checker --input file_link'")
            
        else:
            file_input = read_file(sys.argv[2])
            file= read_file(file_input)
            #print (file_input)
        
                                                    
if __name__ == "__main__":
    main()