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
    
    def __init__(self, L, text):
        
        self.size=L
        print("this is self.size", self.size)
        self.text = text
        
        self.array=[[False]*L for _ in range(L)]
            
    def get_cmd(self):
        pat = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")
        matches = pat.finditer(self.text)
        self.instructions = []
        for match in matches:
            command = list(match.groups())

            for i in range(1, 5):
                command[i] = int(command[i])
             
            self.instructions.append(command)
            
            
            
    def apply_all(self):
        
        
        print ("apply all now")
        for instruction in self.instructions:
            self.apply(instruction)
         
    def apply(self, instruction):
        cmd, x1, y1, x2, y2 = instruction
        
        if cmd == 'turn on':
            self.turn_on(x1, y1, x2, y2)


        if cmd == 'turn off':
            self.turn_off(x1, y1, x2, y2)

        print ("this is the ", instruction)
            
        if cmd == 'switch':
            self.switch (x1, y1, x2, y2)
            
        
            
            
    def turn_on(self, x1, y1, x2, y2):
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                self.array[j][i] = 1
              
    
    def turn_off(self, x1, y1, x2, y2):

        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                self.array[j][i] = 0
              
        
    def switch(self, x1, y1, x2, y2):
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if self.array[j][i] == 0:
                    self.array[j][i] = 1
                   
                else: 
                    self.array[j][i] = 0
                    
    def count(self):
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.array[i][j]==1:
                        count+=1
        return count
        print (count)
        

def read_file(input_link):
    '''Function which reads in a file from a URL or local file and returns the
    contents of the file in a string'''

    if input_link.startswith("http://"):
        req = urllib.request.urlopen(input_link)
        text = req.read().decode('utf-8')
    else:
        text = open(input_link,'r').read() #.read() converts to a string
    
    try:
        L = int(text.split('\n')[0])
    except Exception:
        L = None
        text = None
       
    return text, L
        
def main():
    if len(sys.argv) < 3:
        print( file_input, "\nCheck the parameters, no file given.\nInput should be of form 'led_checker --input file_link'")

    else:
    
        
        
        
        file, length = read_file(sys.argv[2])
        
        lightBox99 = LightBox(length, file)

        lightBox99.get_cmd()
    
        lightBox99.apply_all()

        print ("This is the count",lightBox99.count())

        
if __name__ == "__main__":
    print("In main2.py")
    main()
        
        
        
                                                    
