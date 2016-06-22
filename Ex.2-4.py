#2 
import math
r=float(input('Enter the radius'))
print('The area of the circle = ',math.pi*r**2)
#3
c=float(input('Enter Celsius value (C)'))
print('Fahrenheit = ',9/5*c+32,'F')
#4
i=int(input('Enter the intial B bacteria number'))
t=float(input('Enter time (in minutes)'))
if t<2:
    print('After ',t,' minutes we would have ',i,' bacterias')
elif t%2==0:
    print('After ',t,' minutes we would have ',i*2**(t/2),' bacterias')
else:
    print('After ',t,' minutes we would have ',i*2**(t//2),' bacterias')
