class card():
 def __init__(self, val, sym):
   self.value=val
   self.symbol=sym
   if self.symbol in "sc": self.color='B'
   else: self.color='R'
   if self.value in 'JQK': self.fig=True
   else: self.fig=False
 def __str__(self):
  return self.value+self.symbol
 def detailed_info(self):
  print('Aksia', self.value, 'symbol: ', self.symbol)
  print('color', self.color, 'figura', self.fig)

c1 = card('5', 'd')
#print(c1.value, c1.symbol, c1.color, c1.fig)
c1.detailed_info()
