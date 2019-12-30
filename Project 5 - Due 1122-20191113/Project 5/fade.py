# Project 5 - Puzzle
# Name: John Wright
# Instructor: S. Einakian
# Section: 101-05
import sys
from math import sqrt

def main():
   #ppm -> ppm
   #adds fade effect to image using a row column and radius
   args = sys.argv
   i = 4
   lines = ''
   val = 0
   if len(args) != 5:
      print('Usage: python3 fade.py <image> <row> <column> <radius>')
      quit()
   row = int(args[2])
   col = int(args[3])
   radius = int(args[4])
   scale = 0
   pixcol = 0
   pixrow = 0
   count = 0
   inc = 0
   width = 0

   try:
      file = open(args[1])
      for line in file:
         lines += line
      lines = lines.split()
      while i < len(lines):
         width = lines[1]
         pixcol = count % int(width)
         pixrow = count // int(width)
         scale = (radius - sqrt(((col - pixcol)**2)+((row-pixrow)**2))) / radius
         val = int(int(lines[i]) * scale)
         if val > 255:
            val = 255
         if val < 0:
            val = 0
         lines[i] = val
         i += 1
         inc += 1
         if inc == 3:
            count += 1
            inc = 0

      output = open('hidden.ppm', 'w+')
      x = 0
      while x < len(lines):
         if x == 0:
            output.write(str(lines[x])+'\n')
            x += 1
         elif x == 1:
            output.write(str(lines[x])+' '+str(lines[x+1])+'\n')
            x += 2
         elif x > 2:
            output.write(str(lines[x])+'\n')
            x += 1
   except IOError:
      print('Unable to open '+str(args[1]))

if __name__ == '__main__':
   main()