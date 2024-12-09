import numpy as np
import math
import os
from omegaDots import f1, f2

path='/Users/Krishna/Documents/repositories/the_one_true_double_pendulum'


#if you are not krishna, then uncomment this code:
#path=os.path.dirname(cwd)


def leapfrog(r, t_final, dt):
    # This function implements the leapfrog method of numerical integration
    #
    # INPUTS:
    # r[0], r[1]: initial thetas
    # r[2], r[3]: initial omegas
    # t_final: the final time to which the system is allowed to evolve
    # tSteps: the number of steps taken from the initial time (here assumed to be zero) to f_final
    #
    # OUTPUTS:
    # omega1List, omega2List: lists of the omegas at each time
    # theta1List, theta2List: lists of the thetas at each time
    # tList: the actual list of times

    t0 = 0

    theta1_init = r[0]
    theta2_init = r[1]
    omega1_init = r[2]
    omega2_init = r[3]
    
    tList = np.arange(t0, t_final, step=dt)

    omega1List = []
    omega2List = []
    theta1List = []
    theta2List = []

    # First step is to do half an Euler step for omega and theta
    w1HalfOmega = omega1_init + (dt/2) * f1(omega1_init, omega2_init, theta1_init, theta2_init)
    w2HalfOmega = omega2_init + (dt/2) * f2(omega1_init, omega2_init, theta1_init, theta2_init)
    w1HalfTheta = theta1_init + (dt/2) * omega1_init
    w2HalfTheta = theta2_init + (dt/2) * omega2_init


    omega1 = omega1_init
    omega2 = omega2_init
    theta1 = theta1_init
    theta2 = theta2_init

    for t in tList:
        # update lists
        omega1List.append(omega1)
        omega2List.append(omega2)
        theta1List.append(theta1)
        theta2List.append(theta2)

        # Now, for each time we evolve using equations 29 of ODE notes
        # first eqn
        k1_1Omega = dt * f1(omega1, omega2, theta1, theta2)
        k1_2Omega = dt * f2(omega1, omega2, theta1, theta2)
        k1_1Theta = dt * omega1
        k1_2Theta = dt * omega2
        # second eqn
        w1HalfOmega = w1HalfOmega + k1_1Omega
        w2HalfOmega = w2HalfOmega + k1_2Omega
        w1HalfTheta = w1HalfTheta + k1_1Theta
        w2HalfTheta = w2HalfTheta + k1_2Theta
        #third eqn
        k2_1Omega = dt * f1(w1HalfOmega, w2HalfOmega, w1HalfTheta, w2HalfTheta)
        k2_2Omega = dt * f2(w1HalfOmega, w2HalfOmega, w1HalfTheta, w2HalfTheta)
        k2_1Theta = dt * w1HalfOmega
        k2_2Theta = dt * w2HalfOmega
        # fourth eqn
        omega1 = omega1 + k2_1Omega
        omega2 = omega2 + k2_2Omega
        theta1 = theta1 + k2_1Theta
        theta2 = theta2 + k2_2Theta

    return omega1List, omega2List, theta1List, theta2List, tList


theta1=np.pi/2
theta2=np.pi/2
omega1=0
omega2=0

initial_vals=np.array([ theta1 , theta2 , omega1, omega2], np.float64) # a vector of our initial conditions for x, y, vx and vy


dt=0.00001
t_final=80

partb=leapfrog(initial_vals,t_final=t_final,dt=dt)
np.savetxt(f'{path}/results/partb_leapfrog_{t_final}s_{dt*1e6}us_timesteps.csv', partb, delimiter=',', header='theta1,theta2,omega1,omega2,t', comments='', fmt='%f') 