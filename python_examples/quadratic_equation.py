a=input("a=")
b=input("b=")
c=input("c=")
print("I solve the following equation:")
a=int(a)
b=int(b)
c=int(c)
if a==0:
 if b==0:
  if c==0:
   print("Equation is undefined")
  else:
   x=-c/b
   print("Equation is impossible to be solved")
else:
 diak=b*b-4*a*c
 print("Discriminant equals to =")
 if diak<0:
   print("Equation does not have real values")
 if diak==0:
   print("Equation has one double solution")
 r = diak**0.5
 x1=(-b-r)/(2*a)
 x2=(-b+r)/(2*a)
 print(x1)
 print(x2)



def diakrinousa(a,b,c):
 return b*b-4*a*c

print(diakrinousa(4,2,-1))


def remainder(x,y):
 z=x//y
 r=x-z*y
 return r

def check_odd_or_even(x):
 y=remainder(x,2)
 if y==0:
   return 'even'
 else:
   return 'odd'

print(remainder(3,4))
print(check_odd_or_even(5))
for x in [0,1,2,3,4,5,6,7,8,9]:
 print('For x=', x, 'f(x)', x, 'which is the identical function')


L = list(range(-3,4))
print(L)
def is_prime(n):
 if n<2:
   return('no')
 else:
   for x in range(2, n-1):
     if remainder(n,x)==0:
       return('no')
   return('yes')


for t in range(20):
  print(t, is_prime(t))
