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

fiducial =  np.loadtxt(f'{path}/results/poincare_dat/1fid_rk4_1000s_0.00_0.79_0.000_0.000_1000.0us_timesteps.csv', delimiter=',', skiprows=1)

file1 = np.loadtxt(f'{path}/results/poincare_dat/1_rk4_1000s_-0.00_0.79_0.007_-0.004_1000.0us_timesteps.csv', delimiter=',', skiprows=1)
file2 = np.loadtxt(f'{path}/results/poincare_dat/1_rk4_1000s_-0.01_0.78_0.008_0.004_1000.0us_timesteps.csv', delimiter=',', skiprows=1)
file3 = np.loadtxt(f'{path}/results/poincare_dat/1_rk4_1000s_-0.01_0.79_-0.005_0.001_1000.0us_timesteps.csv', delimiter=',', skiprows=1)
file4 = np.loadtxt(f'{path}/results/poincare_dat/1_rk4_1000s_-0.01_0.79_0.000_-0.007_1000.0us_timesteps.csv', delimiter=',', skiprows=1)
file5 = np.loadtxt(f'{path}/results/poincare_dat/1_rk4_1000s_-0.01_0.79_0.007_-0.003_1000.0us_timesteps.csv', delimiter=',', skiprows=1)
file6 = np.loadtxt(f'{path}/results/poincare_dat/1_rk4_1000s_-0.01_0.79_0.009_0.005_1000.0us_timesteps.csv', delimiter=',', skiprows=1)
file7 = np.loadtxt(f'{path}/results/poincare_dat/1_rk4_1000s_0.00_0.79_-0.010_-0.006_1000.0us_timesteps.csv', delimiter=',', skiprows=1)
file8 = np.loadtxt(f'{path}/results/poincare_dat/1_rk4_1000s_0.00_0.80_0.008_0.001_1000.0us_timesteps.csv', delimiter=',', skiprows=1)
file9 = np.loadtxt(f'{path}/results/poincare_dat/1_rk4_1000s_0.01_0.78_-0.004_-0.003_1000.0us_timesteps.csv', delimiter=',', skiprows=1)
file10 = np.loadtxt(f'{path}/results/poincare_dat/1_rk4_1000s_0.01_0.79_-0.001_-0.009_1000.0us_timesteps.csv', delimiter=',', skiprows=1)

poincare_section(fiducial, .4, 1,0)
poincare_section(file1, .4, 1, 1)
poincare_section(file2, .4, 1, 2)
poincare_section(file3, .4, 1, 3)
poincare_section(file4, .4, 1, 4)
poincare_section(file5, .4, 1, 5)
poincare_section(file6, .4, 1, 6)
poincare_section(file7, .4, 1, 7)
poincare_section(file8, .4, 1, 8)
poincare_section(file9, .4, 1, 9)
poincare_section(file10, .4, 1, 10)