import numpy as np
import matplotlib.pyplot as plt

path='/Users/Krishna/Documents/repositories/the_one_true_double_pendulum/'

savepath='/Users/Krishna/Documents/repositories/the_one_true_double_pendulum/figures/rk4_vs_lf'

lf_result=np.loadtxt(f'{path}results/leapfrog_part2/partb_leapfrog_15s_500us_timesteps.csv', delimiter=',', skiprows=1)

rk4_result=np.loadtxt(f'{path}results/rk4_part2/partb_rk4_80s_500us_timesteps.csv', delimiter=',', skiprows=1)


x=['theta 1', 'theta 2', 'omega 1', 'omega 2']
units=['radians', 'radians', 'radians/s', 'radians/s']
        
# tfinal=10
# dt=500e-6
# final_step=int(tfinal/dt)
# plt.plot(rk4_result[:final_step,4],rk4_result[:final_step,q],label='rk4 integrator')

# plt.plot(lf_result[:final_step,4] , lf_result[:final_step,q],label='leapfrog integrator')

# plt.ylabel(f'{x[q]}  ({units[q]})')
# plt.xlabel('time (s)')
# plt.title('RK4 integrator vs Leapfrog Integrator with .5ms Timesteps')
# plt.legend()
# plt.savefig(f'{savepath}/rk4_and_lf_{x[q]}')
# plt.clf()
plt.figure(figsize=(12, 10))
q=3
tfinal=3
dt=500e-6
final_step=int(tfinal/dt)
err=lf_result[:final_step,q]-rk4_result[:final_step,q]
plt.plot(lf_result[:final_step,4] , err)
plt.ylabel(f'|RK4-LF| {x[q]}  ({units[q]})')
plt.xlabel('time (s)')
plt.title('Difference between RK4 and lf with .5ms Timesteps')
plt.savefig(f'{savepath}/rk4_lf_diff_{x[q]}_after{tfinal}s')
