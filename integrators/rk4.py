import numpy as np
import numpy as np
import math
import matplotlib.pyplot as plt
import os

path='/Users/Krishna/Documents/repositories/the_one_true_double_pendulum'


#if you are not krishna, then uncomment this code:
#path=os.path.dirname(cwd)




'''
Convention:

r[0]=theta1
r[1]=theta2
r[2]=omega1
r[3]=omega2

'''

g = 9.81
l=.4

def f(r):
    theta1=r[0]
    theta2=r[1]
    omega1=r[2]
    omega2=r[3]

    num1 = - ( (omega1**2) * np.sin(2*theta1 - 2*theta2) + 2 * (omega2**2)*np.sin(theta1-theta2) + (g/l)*(np.sin(theta1 - 2*theta2) + 3*np.sin(theta1)))
    den1 = 3 - np.cos(2*theta1 - 2*theta2)

    num2 = 4 * np.float64((omega1**2)) * np.sin(theta1 - theta2) + np.float64((omega2**2)) * np.sin(2*theta1-2*theta2) + (2*g/l)*(np.sin(2*theta1 - theta2) - np.sin(theta2))
    den2 = 3 - np.cos(2 * theta1 - 2 * theta2)

    
    f_theta1=omega1 
    f_theta2=omega2  
    f_omega1=num1/den1
    f_omega2=num2/den2

    return np.array([f_theta1,f_theta2,f_omega1, f_omega2])

#Default initial conditions from Newman Page 400 Problem 8.15 part b
theta1=np.pi/2
theta2=np.pi/2
omega1=0
omega2=0

initial_vals=np.array([ theta1 , theta2 , omega1, omega2], np.float64) # a vector of our initial conditions for x, y, vx and vy



def rk4(t: float, N: int, f, r: np.ndarray):
    """
    4th-order RK integrator with linear step size.

    Inputs:
    t  = final time value
    N  = number of time steps
    f  = function representing the differential equation
    r  = initial state [theta1, theta2, omega1, omega2]

    Outputs:
    Returns an Nx5 array of [theta1, theta2, omega1, omega2, t].
    """
    h = t/ N
    tpoints = np.arange(0, t, h)
    results = np.zeros((N, len(r)+1))

    for i, t in enumerate(tpoints):
        # Store current state and time
        results[i, :] = [*r, t]

        # Runge-Kutta steps
        k1 = h * f(r)
        k2 = h * f(r + 0.5 * k1)
        k3 = h * f(r + 0.5 * k2)
        k4 = h * f(r + k3)

        # Update state
        r = r + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return results

N_steps=2000
t_final=20

deltaT=t_final/N_steps
partb=rk4(t=t_final, N=N_steps,  f=f,r=initial_vals.copy())
np.savetxt( f'{path}/results/partb_rk4_{t_final}s_{deltaT*1000}ms_timesteps.csv', partb, delimiter=',', header='theta1,theta2,omega1,omega2,t', comments='', fmt='%f') 