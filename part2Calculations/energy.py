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


rk4_10us_tsteps=np.loadtxt(f'{path}/results/partb_rk4_80s_10.0us_timesteps.csv', delimiter=',', skiprows=1)
rk4_10000us_tsteps=np.loadtxt(f'{path}/results/partb_rk4_80s_10000.0us_timesteps.csv', delimiter=',', skiprows=1)
rk4_100000us_tsteps=np.loadtxt(f'{path}/results/partb_rk4_80s_100000.0us_timesteps.csv', delimiter=',', skiprows=1)

def H(file,l=.4):

    theta1, theta2, omega1, omega2, = file[:,0], file[:,1], file[:,2], file[:,3]
    V= -m * g * l * ( 2*np.cos(theta1) + np.cos(theta2))
    T= m * l * l * ( np.power(omega1,2) + .5 * np.power(omega2,2) + omega1*omega2 * np.cos(theta1-theta2) )
    return(T+V)



plt.plot(rk4_10000us_tsteps[:,4],H(rk4_10000us_tsteps), label='Rk4, 10ms timesteps')
plt.plot(rk4_10us_tsteps[:,4],H(rk4_10us_tsteps), label='RK4, 10us timesteps')
plt.xlabel('time (s)')
plt.ylabel('Energy (Joules)')
plt.legend()
plt.title('Energy As a Function of Time with rk4 Integrator')
plt.savefig(f'{path}/figures/rk4_energy_vs_time.png')

plt.clf()

#now lets look at the leapfrog integrator




leapfrog_1000us_timestep=np.loadtxt(f'{path}/results/partb_leapfrog_80s_1000.0us_timesteps.csv', delimiter=',' , skiprows=1)
leapfrog_100us_timestep=np.loadtxt(f'{path}/results/partb_leapfrog_80s_100.0us_timesteps.csv', delimiter=',', skiprows=1)
leapfrog_10us_timestep=np.loadtxt(f'{path}/results/partb_leapfrog_80s_10.0us_timesteps.csv', delimiter=',', skiprows=1)

#plt.plot(leapfrog_1000us_timestep[:,4],H(leapfrog_1000us_timestep), label='Rk4, 10ms timesteps')
plt.plot(leapfrog_1000us_timestep[:,4],H(leapfrog_100us_timestep), label='Leapfrog, 100us timesteps')
plt.xlabel('time (s)')
plt.ylabel('Energy (Joules)')
plt.legend()
plt.title('Energy As a Function of Time with Leapfrog Integrator')
plt.savefig(f'{path}/figures/leapfrog_energy_vs_time.png')
plt.show()
plt.clf()