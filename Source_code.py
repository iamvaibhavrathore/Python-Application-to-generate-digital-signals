# -- coding: utf-8 --
"""
Created on Wed Nov  2 23:20:56 2022

@author: Vaibhav Rathore
"""

import matplotlib.pyplot as plt
import numpy as np
import math
plt.close('all')

# impulse
n=np.arange(-10,10)
l=np.size(n)
imp=np.zeros(l)e
ind=np.where(n==0)
imp[ind]=1
plt.stem(n,imp)
plt.title('Impulse Signal')
plt.xlabel('Sample index')
plt.ylabel('Amplitude')
plt.grid(True)

# unit step
stp=np.zeros(l)
ind=np.where(n>=0)
plt.figure(2)
stp[ind]=1
plt.stem(n,stp,'r--')
plt.title('Unit Step Signal')
plt.xlabel('Sample Number')
plt.ylabel('Amplitude')
plt.grid(True)

# ramp
ramp =np.zeros(l)
ind=np.where(n>=0)
ramp[ind]=n[ind]
plt.figure(3)
plt.stem(n,ramp,'g--')
plt.title('Ramp Signal')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.grid(True)

# sine wave

# digital
n=np.arange(-100,100)
x=np.sin(0.1*n)
plt.figure(4)
plt.stem(n,x)
plt.title('digital sinosuidal signal')
plt.xlabel('Sample Number')
plt.ylabel('Amplitude')
plt.grid('True')

# analog
Fs=100
n=np.arange(0,2,1/Fs)
f=2
plt.figure(5)
y=np.sin(2*math.pi*f*n)
plt.plot(n,y)
plt.title('Analog sinusoidal signal')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.grid(True)

#exponential
a=0.9
n=np.arange(-10,50)
z=a*n
plt.figure(6)
plt.stem(n,z)
plt.title('Exponential signal')
plt.xlabel('sample number')
plt.ylabel('amplitude')
plt.grid(True)

#continuous time signals

t = np.linspace(-8, 8, 1000)
x = np.sinc(t)
plt.figure(7)
plt.plot(t, x, '-b')
plt.title(r'x(t) = sinc(t)')
plt.xlabel(r't (in s)')
plt.grid()

#rectangular pulse
def p(t):
    """Basic rectangular pulse"""
    return 1 * (abs(t) < 0.5)
#triangular pulse
def pt(t):
    """ Basic triangular pulse"""
    return (1 - abs(t)) * (abs(t) < 1)
#sign function
def sgn(t):
    """Sign function"""
    return 1 * (t >= 0) - 1 * (t < 0)

functions = [p, pt, sgn]

t = np.linspace(-2, 2, 1000)

plt.figure(8)
for i, function in enumerate(functions, start=1):
    plt.subplot(2, 2, i)
    plt.plot(t, function(t), '-b')
    plt.ylim((-1.1, 1.1))
    plt.title(function.__doc__)
plt.tight_layout()
plt.show()
