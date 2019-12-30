# Project 5 - Puzzle
# Name: John Wright
# Instructor: S. Einakian
# Section: 101-05
import sys
from math import sqrt
from typing import List

def main():
   #ppm -> ppm
   #returns a blurred photo individually averaging the red green and blue values for the puxels within given reach.
   args = sys.argv
   i = 4
   lines = ''
   val = 0
   if len(args) != 3:
      print('Usage: python3 blur.py <image_file.ppm> <reach>')
      quit()
   reach = int(args[2])
   pixcol = 0
   pixrow = 0
   pixelcount = 0
   width = 0
   val = 0
   pixels = []
   rgb_index = 0
   boxred = []
   boxgreen = []
   boxblue = []
   pix = 0
   try:
      file = open(args[1])
      for line in file:
         lines += line
      lines = lines.split()
      for x in range(len(lines)-2):
         if x >= 4:
            pixels.append( [ lines[x], lines[x + 1], lines[x + 2] ] )
      while i < len(lines):
         width = lines[1]
         select_col = pixelcount % int(width)
         select_row = pixelcount // int(width)
         boxred = []
         boxgreen = []
         boxblue = []
         while pix < len(pixels):
            b_current_col = pix % int(width)
            b_current_row = pix // int(width)
            if b_current_col in range(select_col - reach, select_col + reach) and b_current_row in range(select_row - reach, select_row + reach):
               val = pixels[pix]
               boxred.append(int(val[0]))
               boxgreen.append(int(val[1]))
               boxblue.append(int(val[2]))
            pix += 1
         print(boxred)
         valred = sum(boxred) / len(boxred)
         valgreen = sum(boxgreen) / len(boxgreen)
         valblue = sum(boxblue) / len(boxblue)
         if valred > 255:
            valred = 255
         elif valred < 0:
            valred = 0
         if valgreen > 255:
            valgreen = 255
         elif valgreen < 0:
            valgreen = 0
         if valblue > 255:
            valblue = 255
         elif valblue < 0:
            valblue = 0
         lines[i] = valred
         lines[i + 1] = valblue
         lines[i + 2] = valgreen
         rgb_index += 1
         i += 3
         pixelcount += 1
      output = open('hidden.ppm', 'w+')
      x = 0
      while x < len(lines):
         if x == 0:
            output.write(str(lines[x]) + '\n')
            x += 1
         elif x == 1:
            output.write(str(lines[x]) + ' ' + str(lines[x + 1]) + '\n')
            x += 2
         elif x > 2:
            output.write(str(lines[x]) + '\n')
            x += 1
   except IOError:
      print('Unable to open ' + str(args[1]))



if __name__ == '__main__':
   main()
