# Project 5 - Puzzle
# Name: John Wright
# Instructor: S. Einakian
# Section: 101-05
import sys
def main():
   #ppm -> ppm
   # multiplies red value by 10 and sets each pixel value to the result
   args = sys.argv
   newfile = 'P3\n'
   i = 4
   lines = ''
   val = 0
   try:
      file = open(args[1])
      for line in file:
         lines += line
      lines = lines.split()
      while i < len(lines):
         val = 10 * int(lines[i])
         if val > 255:
            val = 255
         lines[i] = val
         lines[i+1] = val
         lines[i+2] = val
         i += 3
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
