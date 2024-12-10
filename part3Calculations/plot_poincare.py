import numpy as np
import matplotlib.pyplot as plt
import os

path = os.getcwd()

rk4_yuh = np.loadtxt(f'{path}/results/partc_rk4_80s_100.0us_timesteps.csv', delimiter=',', skiprows=1)
rk4_yuh2 = np.loadtxt(f'{path}/results/partb_rk4_400s_100.0us_timesteps.csv', delimiter=',', skiprows=1)

def poincare_section(file, l = .4):
    """
    Generate the Poincaré section for the system.
    reads in a file from results folder
    plots theta2 vs. omega2 for points in poincaire section

    """

    theta1, theta2, omega1, omega2, time = file[:,0], file[:,1], file[:,2], file[:,3], file[:,4]
    #find indices where θ1 = 0 and w1 > 0
    poincare_indices = np.where((np.abs(theta1) < 1e-3) & (omega1 > 0))[0]
    
    theta2_section = theta2[poincare_indices]
    omega2_section = omega2[poincare_indices]
    
    #Plot the Poincaré section
    plt.scatter(theta2_section, omega2_section, s=20, color='blue')
    plt.title("Poincaré Section: theta2 vs. omega2")
    plt.xlabel("theta2")
    plt.ylabel("omega2")
    plt.grid(True)
    plt.show()
'''
    plt.plot(time, theta2)
    plt.title("Poincaré Section: theta2 vs. time")
    plt.xlabel("time")
    plt.ylabel("theta2")
    plt.grid(True)
    plt.show()
'''
poincare_section(rk4_yuh2)