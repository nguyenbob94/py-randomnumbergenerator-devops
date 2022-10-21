import os
import random
import sys

# Print number
def printer(randomnumber):
  os.system('cls')
  print("Flight number generated: " + str(randomnumber))
  print("Enjoy your flight" '\n\n')

#Get random number between start and end range
def runGenerator(start,end):
  randomnumber = random.randrange(start,end+1)
  printer(randomnumber)

try: 
  start = int(sys.argv[1])
  end = int(sys.argv[2])
except:
  start = None
  end = None

while True:
  try:
    if start is None:
      start = int(input("Enter starting range number: "))
    if end is None:
      end = int(input("Enter ending range number: "))

    if start > end:
      print("Starting range number cannot be higher than Ending range")
    elif start == end:
      print("Starting and Ending range cannot be the same")
    else:
      runGenerator(start,end)
      break
  except:
    print("Input must be a numberic")
  
  start = None
  end = None

input("Press Enter to continue..")
