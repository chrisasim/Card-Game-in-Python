import random

class deck():
 values="A23456789TJQK"
 symbols="shcd"
 def __init__():
  self.content=[]
  self.pile=[]
  for s in deck.symbols:
   for v in deck.values:
    c = card(v,s)
    self.content.append(c)
 def __str__(self):
  s=""
  cntr=0
  for i in self.content:
   s = s+str(i)+" "
   cntr=cntr+1
   if cntr%12==0: s=s+ '\n'
   s=s+str(len(self.content))+"-"+str(len(self.pile))
   return s
 def shuffle(self):
  random.shuffle(self.content)
 def draw(self):
  if len(self.content)<1: return "empty"
  c=self.content[0]
  self.content = self.content[1:]
  self.pile.append(c)
  return c
 def collect(self):
  self.content=self.content+self.pile
  self.pile=[]

