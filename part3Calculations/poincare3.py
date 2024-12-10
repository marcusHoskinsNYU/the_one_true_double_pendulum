import numpy as np
import matplotlib.pyplot as plt
import os
from plot_poincare import poincare_section

path = os.getcwd()

"""
Fiducial initial conditions:
theta1=np.pi
theta2=0
omega1=0
omega2=0.1
"""

fiducial =  np.loadtxt(f'{path}/results/part3_rk4_1000s_3.14_0.00_0.000_0.100_1000.0us_timesteps.csv', delimiter=',', skiprows=1)

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
poincare_section(fiducial, .4, 3,0)