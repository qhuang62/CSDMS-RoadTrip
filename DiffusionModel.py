"""One Dimensional Diffusion Model"""

#import libraries
import numpy as np #for arrays
import matplotlib.pyplot as plt #for plotting

D = 100 #diffusivity
Lx = 300 #domain size

#set model grid
dx = 0.5 #step size
x = np.arange(start=0, stop=Lx, step=dx)
nx = len(x)

#check value
#extract 1 value
x[1] #-1 will be the last value of array

#extarct range
x[0:5] #not including the last index so if want first 5 elements we need 5] not 4]

#shortcut
x[-5:] #last 5 

C = np.zeros_like(x)

#define 2 boundry conditions
C_left = 500 
C_right = 0

#
C[x <= Lx / 2] = C_left
C[x > Lx / 2] = C_right


plt.figure()
plt.plot(x, C, "r")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Initial Profile")


nt = 5000 #time step
dt = 0.5 * dx ** 2 / D ##dx^2


for t in range(0, nt): #range from 0 to 4999, nt-1
    C[1:-1] += D * dt / dx ** 2 * (C[:-2] - 2 * C[1:-1] + C[2:]) 
#C[1:-1] 2nd value of variable C to last value 
#+= updating the C[a,b] (leftside) by adding the rest (rightside of +=)
#see formula


plt.plot(x, C, "b")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Final Profile")

