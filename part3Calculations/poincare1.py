import numpy as np
import matplotlib.pyplot as plt
import os
from plot_poincare import poincare_section

path = os.getcwd()


"""
Fiducial initial conditions:
theta1= 0
theta2= np.pi/4 
omega1=0
omega2=0
"""

fiducial =  np.loadtxt(f'{path}/results/part3_rk4_1000s_0.00_0.52_0.000_0.000_1000.0us_timesteps.csv', delimiter=',', skiprows=1)
'''
file1 = np.loadtxt(f'{path}/results/', delimiter=',', skiprows=1)
file2 = np.loadtxt(f'{path}/results/', delimiter=',', skiprows=1)
file3 = np.loadtxt(f'{path}/results/', delimiter=',', skiprows=1)
file4 = np.loadtxt(f'{path}/results/', delimiter=',', skiprows=1)
file5 = np.loadtxt(f'{path}/results/', delimiter=',', skiprows=1)
file6 = np.loadtxt(f'{path}/results/', delimiter=',', skiprows=1)
file7 = np.loadtxt(f'{path}/results/', delimiter=',', skiprows=1)
file8 = np.loadtxt(f'{path}/results/', delimiter=',', skiprows=1)
file9 = np.loadtxt(f'{path}/results/', delimiter=',', skiprows=1)
file10 = np.loadtxt(f'{path}/results/', delimiter=',', skiprows=1)
'''
poincare_section(fiducial, .4, 1,0)