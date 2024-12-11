import numpy as np
import matplotlib.pyplot as plt

'''
To test convergence, Im going to take the rk4 integrator with 10_us time steps and say that that is "the real" answer. I am then going to compare the theta1 values 

'''

path='/Users/Krishna/Documents/repositories/the_one_true_double_pendulum'


#I am going to use the rk4 integrator with 10us timesteps as the 'true' solution of the double pendulum, because the timesteps are so small it is overkill for how accurate it is.
rk4_10us_timesteps=np.loadtxt(f'{path}/results/partb_rk4_80s_10.0us_timesteps.csv', delimiter=',', skiprows=1)

#now I am going to compare 10us to much larger timesteps. I am going to try 500us, 1500us, 2000us etc.. and see how far off they are from the 10us timestep prediction
timesteps=np.array([500.0,1500.0,2000.0,2500.0,3000.0]) #in microseconds



files=[]
rk4_10us_filtered=[]


for i in range(len(timesteps)):

    file=np.loadtxt(f'{path}/results/partb_rk4_80s_{timesteps[i]}us_timesteps.csv', delimiter=',', skiprows=1)
    files.append(file)

    #to compare the 10us timesteps to the larger timesteps, I need the arrays of thetas and omegas to be the same size. 
    #If I am comparing 500us timesteps to 10 us timesteps, I need to only take every 50th value of the rk4 integrator output
    
    rk4_10us_timesteps_filtered=rk4_10us_timesteps[ ::int(timesteps[i]/10) , : ]
    rk4_10us_filtered.append(rk4_10us_timesteps_filtered)
  

    #debugging code to make sure the timesteps are the same for the two arrays. the 4th column of arrays corresponds to the timesteps column, so I am printing out all the timesteps and making sure they are the same
    # print(timesteps[i])
    # print(rk4_10us_timesteps_filtered[:,4])
    # print(file[:,4])

    #now I can compare n timesteps to the 10us rk4 output. I have to pick some value to compare so I guess I will pick theta1
    err=np.abs(file[:,1]-rk4_10us_timesteps_filtered[:,1])
    plt.plot(file[:,4],err,label=f'step size ={timesteps[i]/1000}ms')


plt.ylabel('|Theta 1 Error| (radians)')
plt.xlabel('time (s)')
plt.title('Rk4 Integrator Error for Different Timesteps over 80s')
plt.legend()
plt.savefig(f'{path}/figures/rk4_integrator_theta1Err_80s.png')

plt.clf()
# now I want to just plot the first 10s

tfinal=15
q=1
for i in range(len(timesteps)):
    final_step=int(tfinal*1e6/timesteps[i])

    err=np.abs(files[i][:final_step,q]-rk4_10us_filtered[i][ : final_step,q])
    
    plt.plot( files [i][:final_step,4] , err, label=f'step size ={timesteps[i]/1000}ms')
    
plt.subplots_adjust(left=0.2)
plt.ylabel('|Theta 2 Error| (radians/s)')
plt.xlabel('time (s)')
plt.title(f'Rk4 Integrator Error for Different Timesteps over {tfinal}s')
plt.legend()
plt.savefig(f'{path}/figures/rk4_integrator_omega2Err_{tfinal}s.png')

plt.clf()

#ok so it seems like it starts getting "interesting around 10s" im going to take the rms err and plot it as a function of step size

rms=[]
for i in range(len(timesteps)):
    final_step=int(tfinal*1e6/timesteps[i])

    rms.append( np.sqrt( np.mean( (files[i][: final_step,q]-rk4_10us_filtered[i][ : final_step,q])**2 ) ) )
     
    
plt.scatter(np.log(timesteps/1000), np.log(rms))
plt.xlabel('log step size (ms)')
plt.ylabel('log root mean squared error of theta 2')
plt.savefig(f'{path}/figures/rk4_theta2_rms_err_vs_stepsize_after_{tfinal}s_logplot.png')

#ok that kind of looks exponential.


    


