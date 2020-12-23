
import sys

dy = 0
productoftrees = 1
trees = 1

while True:
  try:
    dy = int(input("Enter how many up/down: "))
    dx = int(input("Enter how many right/left: "))
  except ValueError:
    sys.exit()

  with open("C:\\Users\\JennEric\\Documents\\Python\\AdventOfCode\\Day 3\\slope.txt") as file:
    v = [x for x in file.read().split("\n")[::dy]]

  print (v)
  trees = 0
  x = 0

  for y in v:
    trees += (y[x % len(v[0])] == "#") 
    x += dx

  productoftrees *= trees
  print ("Total number of trees multiplied is: ",productoftrees)
  print ("Numbers of trees", trees)




