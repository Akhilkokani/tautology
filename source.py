"""
A tautology finder.

A simple python program which will find whether for given 
values is a tautology or not.


@author Akhil Kokani
@package tautology
"""

first = last = temp = None

def tautology ( p = 0, q = 0 ):
  if p < 0 or q < 0:
    print "Do not insert values less than 0."
    return None

  if p == 1 and q == 0:
    return 0

  return 1

class node:
  
  def __init__ ( self, p = 0, q = 0, value = 1 ):
    self.p = p
    self.q = q
    self.value = value
    self.link = None

def _insert():

  global first, last
  p = input ( "Enter P value: " )
  q = input ( "Enter Q value: " )
  t = tautology ( p, q )

  temp = node(p, q, t)

  if first == None:
    first = last = temp
    return t

  last.link = temp
  last = temp
  return t

def _display():

  print "P\tQ\tT"
  temp = first
  while temp != None:
    if temp.value == 1:
      print temp.p, "\t", temp.q, "\t", temp.value
    else:
      print temp.p, "\t", temp.q, "\t", temp.value, " <== Not a tautology."
    temp = temp.link

#  Main program starts from here
print "Program to find whether given set of values are tautology or not."
print "We use conditional operator (->)."

i = total_number_of_inputs = input("Total set of input's: ")
p = q = counter = 0

print "Enter Truth Table of", i, "rows."
while i > 0:
  if _insert() == 1:
    counter = counter + 1
  i = i - 1

_display()

if counter == total_number_of_inputs:
  print "Truth Table is a tautology."
else :
  print "Truth table which you entered is not a tautology."