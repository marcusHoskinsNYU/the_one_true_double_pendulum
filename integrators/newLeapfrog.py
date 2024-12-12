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
    # dt: the size of each time step taken
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

        # For each time step we evolve using equations 8.63a and 8.63b from Newman:

        omega1 = omega1 + dt * f1(w1HalfOmega, w2HalfOmega, w1HalfTheta, w2HalfTheta)
        omega2 = omega2 + dt * f2(w1HalfOmega, w2HalfOmega, w1HalfTheta, w2HalfTheta)
        theta1 = theta1 + dt * w1HalfOmega
        theta2 = theta2 + dt * w2HalfOmega

        w1HalfOmega = w1HalfOmega + dt * f1(omega1, omega2, theta1, theta2)
        w2HalfOmega = w2HalfOmega + dt * f2(omega1, omega2, theta1, theta2)
        w1HalfTheta = w1HalfTheta + dt * omega1
        w2HalfTheta = w2HalfTheta + dt * omega2

    return theta1List, theta2List, omega1List, omega2List, tList


theta1=np.pi/2
theta2=np.pi/2
omega1=0
omega2=0

initial_vals=np.array([ theta1 , theta2 , omega1, omega2], np.float64) # a vector of our initial conditions for x, y, vx and vy

'''

dt=0.05
t_final=80

partb=leapfrog(initial_vals,t_final=t_final,dt=dt)
np.savetxt(f'partb_leapfrog_{t_final}s_{dt*1e3}ms_timesteps.csv', partb, delimiter=',', header='theta1,theta2,omega1,omega2,t', comments='', fmt='%f') 
'''
tsteps=np.arange(500,3500,100) #microseconds


# for timestep in tsteps:
#     partb=np.column_stack(leapfrog(r=initial_vals.copy(), t_final=t_final, dt=timestep*1e-6, ))
#     np.savetxt( f'{path}/results/leapfrog/partb_leapfrog_{t_final}s_{timestep}us_timesteps.csv', partb, delimiter=',', header='theta1,theta2,omega1,omega2,t', comments='', fmt='%f') 
