# Project 5 - Puzzle
# Name: John Wright
# Instructor: S. Einakian
# Section: 101-05
import sys
from math import sqrt
from typing import List

class Image:
   def __init__(self, filename):
      self.filename = filename
      self.width = 0
      self.column = 0
      self.file_content = open(filename)

   def process_file(self):
      self.column = self.file_content





def main():
   args = sys.argv
   if len(args) != 3:
      print('Usage: python3 blur.py <image_file.ppm> <reach>')
      quit()
   try:
      image = Image(args[0])
      file = open(args[1])
      for line in file:
         lines += line
      lines = lines.split()
      raw_file =  " ".join(char for char in file)
      print(type(lines))
      exit(0)


if __name__ == '__main__':
   main()
