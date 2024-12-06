import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

path='/Users/Krishna/Documents/repositories/the_one_true_double_pendulum'

'''
#if you are not krishna, then uncomment this code

path=os.path.dirname(cwd)
'''
m=1
g=9.8# m/s
l=0.4

filename='partb_rk4_20s_1.0ms_timesteps.csv'

rk4_20ms_tsteps= np.loadtxt(f'{path}/results/partb_rk4_20s_20.0ms_timesteps.csv',delimiter=',', skiprows=1)
rk4_2ms_tsteps = np.loadtxt(f'{path}/results/partb_rk4_20s_2.0ms_timesteps.csv', delimiter=',', skiprows=1)
rk4_1ms_tsteps = np.loadtxt(f'{path}/results/partb_rk4_20s_1.0ms_timesteps.csv', delimiter=',', skiprows=1)
rk4_200us_tsteps= np.loadtxt(f'{path}/results/partb_rk4_20s_0.2ms_timesteps.csv', delimiter=',', skiprows=1)

rk4_500us_tsteps=np.loadtxt(f'{path}/results/partb_rk4_20s_500.0us_timesteps.csv', delimiter=',', skiprows=1)

def H(file,l=.4):

    theta1, theta2, omega1, omega2, tList=file[:,0], file[:,1], file[:,2], file[:,3], file[:,4]
    V= -m * g * l * ( 2*np.cos(theta1) + np.cos(theta2))
    T= m * l * l * ( np.power(omega1,2) + .5 * np.power(omega2,2) + omega1*omega2 * np.cos(theta1-theta2) )
    return(T+V)



# plt.plot(rk4_20ms_tsteps[:,4],H(rk4_20ms_tsteps))
# plt.plot(rk4_2ms_tsteps[:,4],H(rk4_2ms_tsteps))
# plt.plot(rk4_1ms_tsteps[:,4],H(rk4_1ms_tsteps))
plt.plot(rk4_500us_tsteps[:,4],H(rk4_500us_tsteps))


4
plt.show()