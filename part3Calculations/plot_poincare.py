import numpy as np
import matplotlib.pyplot as plt
import os


path = os.getcwd()

def poincare_section(file, l = .4, i = 0 , k = 0):
    """
    this takes in a csv file from the RK4 and creates a poincare section 
    then it plots this to results/poincare_plots

    indices:
    i : what energy region
    k : what plot when we mass produce data. 
    
    """
    #read file and assign values
    theta1, theta2, omega1, omega2, time = file[:,0], file[:,1], file[:,2], file[:,3], file[:,4]

    #find indices where θ1 = 0 and w1 > 0
    poincare_indices = np.where((np.abs(theta1) < .035) & (omega1 > 0))[0] #error toleracnce is about 2 degrees 
    
    theta2_section = theta2[poincare_indices]
    omega2_section = omega2[poincare_indices]
    
   
    #Plot the Poincaré section
    plt.scatter(theta2_section, omega2_section, color='blue')
    plt.title(f"Poincaré Section: Point: {i} Plot: {k}  ")
    plt.xlabel("theta2")
    plt.ylabel("omega2")
    plt.grid(True)
    plt.savefig(f'{path}/results/poincare_plots/poincare_{i}_{k}', dpi=300, bbox_inches='tight')
    
    #plt.show()
    
