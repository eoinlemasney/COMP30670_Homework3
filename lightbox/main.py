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


class LightBox:
    
    def __init__(self, L, file_path):
        
        self.size=L
        self.read_file(file_path)
        
        self.array=[[False]*L for _ in range(L)]

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
            
            
    def get_cmd(self):    
        pat = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")
        matches = pat.finditer(self.text)
        self.instructions = []
        for match in matches:
            command = list(match.groups())
            for i in range(1, 5):
                command[i] = int(command[i])
            self.instructions.append(command)
            # print(match)   
        print ("This is instrictuons 2 ",self.instructions[2])
    
    def apply(self, instruction):
        cmd, x1, y1, x2, y2 = instruction
        if cmd == 'turn on':
            print ("This is self.cmd ", cmd)
            
            self.array[x1][y1] = True
            self.array[x2][y2] = True

        if cmd == 'switch':
            print ("This is self.cmd ", cmd)
            
            self.array[x1][y1] = True
            self.array[x2][y2] = True
            
        if cmd == 'turn off':
            print ("This is self.cmd ", cmd)
            
            self.array[x1][y1] = False
            self.array[x2][y2] = False
            
        
            
            
            
            
        

        
        
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
    if len(sys.argv) < 3:
        print( file_input, "\nCheck the parameters, no file given.\nInput should be of form 'led_checker --input file_link'")

    else:
        '''use regular expression and create a line for each in file'''
        print("reading from the main now")
        lightBox = LightBox(1000, sys.argv[2])
        print("SIZE OF GRID: ", lightBox.text.split('\n')[0])
        #lightBox.get_cmd()
        #lightBox.apply(lightBox.instructions[0])
        
if __name__ == "__main__":
    main()
        
        
        
        
        
        
       # file_text = read_file(sys.argv[2])
       # arraySize=int(file_text.split("\n")[0])
       # print("This is the array size", arraySize)
      #  lines = pat.finditer(file_text)
        
     #   instructions = []
     #   for line in lines:
       #     print(line.groups())
     #       instructions.append(line.groups())
    #
        
        
                                                    
