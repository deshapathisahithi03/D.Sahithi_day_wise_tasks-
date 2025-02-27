'''a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=b*b-4*a*c
e=2*a
l=d ** (1/2)
f=-b+l
g=-b-l
h=f / e
j=g / e
print(h)
print(j)'''

import cmath
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=cmath.sqrt(b*b-4*a*c)
e=2*a
f=(-b+d)/e
g=(-b-d)/e
print(f"the solutions are {f} and {g}")

import math
number=16
res=math.sqrt(number)
print(res)

import math
number=4.2
res=math.ceil(number)
print(res)
sol=math.floor(number)
print(sol)

import math
angle = math.radians(30)
result = math.sin(angle)
print("Sine of 30 degrees:", result)

import math
print("Value of Pi:", math.pi)

import math
print("Value of Euler's number (e):", math.e)