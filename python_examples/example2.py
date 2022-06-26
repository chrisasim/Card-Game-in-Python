#from winsound import Beep
from random import *
for i in range(20):
 freq=randint(1200, 20000)
 print(freq, "Hz")
# Beep(freq, 200)


from calendar import *
print(calendar(2022))

a=calendar(2022)
my_file=open("example1.odt", "w", encoding="utf-8")
my_file.write(a)
my_file.write("Python does everything, the improtant thing is to knwo how to use it!")
my_file.close()


my_file = open("example1.odt", "r", encoding="utf-8")
calendarfile = my_file.read()
print(calendarfile)
my_file.close()

