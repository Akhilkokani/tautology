from globals import first, last
import node as NODE

def _insert():

  global first, last
  p = input ( "Enter P value: " )
  q = input ( "Enter Q value: " )
  t = tautology ( p, q )

  temp = NODE.node(p, q, t)

  if first == None:
    first = last = temp
    return t

  last.link = temp
  last = temp
  return t

def tautology ( p = 0, q = 0 ):
  if p < 0 or q < 0:
    print "Do not insert values less than 0."
    return None

  if p == 1 and q == 0:
    return 0

  return 1

def _display():

  print "P\tQ\tT"
  temp = first
  while temp != None:
    if temp.value == 1:
      print temp.p, "\t", temp.q, "\t", temp.value
    else:
      print temp.p, "\t", temp.q, "\t", temp.value, " <== Not a tautology."
    temp = temp.link