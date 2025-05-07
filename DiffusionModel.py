#!/usr/bin/env python
# coding: utf-8

# ### Build a 1D diffusion model

# Wed May 7 CSDMS roadtrip class 1
# 
# we tried to code a 1-dimensional model of diffusion.

# #### Formula

# $$ \frac{\partial C}{\partial t} = D\frac{\partial^2 C}{\partial x^2} $$
# 
# discretized:
# 
# $$ C^{t+1}_x = C^t_x + {D \Delta t \over \Delta x^2} (C^t_{x+1} - 2C^t_x + C^t_{x-1}) $$

# the model assumes:
# 
# - constant diffusivity;
# - regular grid;
# - has a step funciton for an initial condition;
# - fixed boundary conditions.
#  
# C(x,t),rate of change of concentration, over time is proportional to the curvature (second derivative) of concentration over space.
# 
# D is the diffusion coefficient - a positive constant telling you how fast things spread out.
# 
# FTCS scheme by Slingerland and Kump (2011). 

# In[ ]:


#import libraries
import numpy as np #for arrays
import matplotlib.pyplot as plt #for plotting


# #### Set up parameteres
# 
# 2 fixed: diffusivity and the size of model domain

# In[ ]:


D = 100 #diffusivity
Lx = 300 #domain size


# In[ ]:


#set model grid
dx = 0.5 #step size
x = np.arange(start=0, stop=Lx, step=dx)
nx = len(x)


# In[ ]:


#check value
#extract 1 value
x[1] #-1 will be the last value of array


# In[ ]:


#extarct range
x[0:5] #not including the last index so if want first 5 elements we need 5] not 4]


# In[ ]:


#shortcut
x[-5:] #last 5 


# #### Set up initial conditions

# C is a step function with a high value of the left, a low value on the right, and a step at the center of domain

# In[ ]:


C = np.zeros_like(x)

#define 2 boundry conditions
C_left = 500 
C_right = 0

#
C[x <= Lx / 2] = C_left
C[x > Lx / 2] = C_right


# ##### plot initial profile

# In[ ]:


plt.figure()
plt.plot(x, C, "r")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Initial Profile")


# set the number of time steps in the model. calculate a stable time step using a stability criterion

# In[ ]:


nt = 5000 #time step
dt = 0.5 * dx ** 2 / D ##dx^2


# loop over time step of the model, solving the diffusion eqn using the FTCS scheme
# Note the use of array operations on the variable C.
# 
# The boundary conditions remain fixed in each time step

# In[ ]:


for t in range(0, nt): #range from 0 to 4999, nt-1
    C[1:-1] += D * dt / dx ** 2 * (C[:-2] - 2 * C[1:-1] + C[2:]) 
#C[1:-1] 2nd value of variable C to last value 
#+= updating the C[a,b] (leftside) by adding the rest (rightside of +=)
#see formula


# $$ \frac{\partial C}{\partial t} = D\frac{\partial^2 C}{\partial x^2} $$
# 

# ###### use of []

# In[ ]:


z = list(range(5))
z


# In[ ]:


z[1:-1]


# In[ ]:


z[:-2]


# In[ ]:


z[2:]


# #### Plot result

# In[ ]:


plt.plot(x, C, "b")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Final Profile")

