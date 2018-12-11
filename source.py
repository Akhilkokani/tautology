"""
A tautology finder.

A simple python program which will find whether for given 
values is a tautology or not.


@author Akhil Kokani
@package tautology
"""
import sys
sys.path.insert(0, "globals.py")
sys.path.insert(0, "node.py")
sys.path.insert(0, "functions.py")
import node as NODE
import functions as FUNC

def main():
  print "Program to find whether given set of values are tautology or not."
  print "We use conditional operator (->)."

  i = total_number_of_inputs = input("Total set of input's: ")
  p = q = counter = 0

  print "Enter Truth Table of", i, "rows."
  while i > 0:
    if FUNC._insert() == 1:
      counter = counter + 1
    i = i - 1

  FUNC._display()

  if counter == total_number_of_inputs:
    print "Truth Table is a tautology."
  else :
    print "Truth table which you entered is not a tautology."

if __name__ == "__main__":
  main()