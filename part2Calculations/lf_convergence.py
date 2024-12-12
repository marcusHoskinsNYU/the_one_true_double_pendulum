import numpy as np
import matplotlib.pyplot as plt

'''
To test convergence, Im going to take the rk4 integrator with 10_us time steps and say that that is "the real" answer. I am then going to compare the theta1 values of rk4 integrations with larger timeseteps to the "real" answer 

'''

path='/Users/Krishna/Documents/repositories/the_one_true_double_pendulum'

savepath='/Users/Krishna/Documents/repositories/the_one_true_double_pendulum/figures/leapfrog_convergence'
#I am going to use the rk4 integrator with 10us timesteps as the 'true' solution of the double pendulum, because the timesteps are so small.
rk4_10us_timesteps=np.loadtxt(f'{path}/results/partb_rk4_80s_10.0us_timesteps.csv', delimiter=',', skiprows=1)

#now I am going to compare 10us to much larger timesteps. I am going to try 500us, 1500us, 2000us etc.. and see how far off they are from the 10us timestep prediction
#timesteps=np.array([500.0,1500.0,2000.0,2500.0,3000.0]) in microseconds

timesteps=np.arange(500,3500,500)

files=[]
rk4_10us_filtered=[]

tfinal=30

#first im going to 
for i in range(len(timesteps)):

    file=np.loadtxt(f'{path}/results/leapfrog_part2/partb_leapfrog_15s_{timesteps[i]}us_timesteps.csv', delimiter=',', skiprows=1)
    files.append(file)

    #to compare the 10us timesteps to the larger timesteps, I need the arrays of thetas and omegas to be the same size. 
    #If I am comparing 500us timesteps to 10 us timesteps, I need to only take every 50th value of the rk4 integrator output
    
    rk4_10us_timesteps_filtered=rk4_10us_timesteps[ ::int(timesteps[i]/10) , : ]
    rk4_10us_filtered.append(rk4_10us_timesteps_filtered)
  
    #debugging code to make sure the timesteps are the same for the two arrays. the 4th column of arrays corresponds to the timesteps column, so I am printing out all the timesteps and making sure they are the same
    # print(timesteps[i])
    # print(rk4_10us_timesteps_filtered[:,4])
    # print(file[:,4])

tfinal=50
q=1

def plot_err(timesteps=timesteps, files=files, q=1, tfinal=50):
    '''
    makes a plot of error vs time for an given a list of rk4 integrator outputs at different timesteps

    INPUTS:

    timesteps: np.array 
    a 1d array of timestep sizes that you are going to plot. The step sizes are in units of microseconds

    files:list
    a list of Nx5 np arrays which contain the ouput of the rk4 integration for each timestep. N length of the rk4 integration and there are 5 columns because we have theta1,theta2,omega1,omega2, and time.

    q:int
    the phase space variable that you want to plot
    0=theta1, 1=theta2, 2=omega1, 3=omega2

    tfinal:int

    the length in time in seconds that you want to plot. If you only want to plot the first 10sec, set tfinal to 10

    '''
    plt.figure(figsize=(12, 10))

    for i in range(len(timesteps)):


        final_step=int(tfinal*1e6/timesteps[i])

        err=np.abs(files[i][:final_step,q]-rk4_10us_filtered[i][ : final_step,q])
        
        plt.plot( files [i][:final_step,4] , err, label=f'step size ={timesteps[i]/1000}ms')

    x=['theta 1', 'theta 2', 'omega 1', 'omega 2']        
    units=['radians', 'radians', 'radians/s', 'radians/s']

    plt.subplots_adjust(left=0.2)
    plt.ylabel(f'|{x[q]} Error| ({units[q]})')
    plt.xlabel('time (s)')
    plt.title(f'Leapfrog Integrator Error for Different Timesteps over {tfinal}s')
    plt.legend()
    plt.savefig(f'{savepath}/leapfrog_integrator_{x[q]}Err_{tfinal}s.png')

    plt.clf()



#ok so it seems like it starts getting "interesting around 10s" im going to take the rms err and plot it as a function of step size

def plot_rms_err(timesteps=timesteps, files=files, q=1, tfinal=10,log=False ):
    '''
    makes a plot of rms error vs for an given a list of rk4 integrator outputs at different timesteps, over a given time interval (tfinal)

    INPUTS:

    timesteps: np.array 
    a 1d array of timestep sizes that you are going to plot. The step sizes are in units of microseconds

    files:np.array 
    an NxMx5 output of the rk4 integration for each timestep. N is the number of different timesteps sizes you are plotting, M length of the rk4 integration and there are 5 columns because we have theta1,theta2,omega1,omega2, and time.

    q:int
    the phase space variable that you want to plot
    0=theta1, 1=theta2, 2=omega1, 3=omega2

    tfinal:int

    the length in time in seconds that you want to plot. If you only want to plot the first 10sec, set tfinal to 10

    log:bool

    set to true to make a log log plot

    '''
    plt.figure(figsize=(12, 10))


    rms=[]
    for i in range(len(timesteps)):
        final_step=int(tfinal*1e6/timesteps[i])
        
        x=['theta 1', 'theta 2', 'omega 1', 'omega 2']
        units=['radians', 'radians', 'radians/s', 'radians/s']
        

        rms.append( np.sqrt( np.mean( (files[i][: final_step,q]-rk4_10us_filtered[i][ : final_step,q])**2 ) ) )
    
    if log==True:
        plt.scatter(np.log(timesteps/1000), np.log(rms))
        plt.xlabel('log [step size (ms)]')
        plt.ylabel(f'log [ root mean squared error of {x[q]} ({units[q]}) ]')

        plt.title(f'log log plot of leapfrog root mean squared error after {tfinal}s')
        plt.savefig(f'{savepath}/leapfrog_{x[q]}_log_rms_err_vs_stepsize_after_{tfinal}s.png')
        
    else:
        plt.scatter(timesteps/1000, rms)
        plt.xlabel('step size (ms)')
        plt.ylabel(f'root mean squared error of {x[q]} ({units[q]})')

        plt.title(f'root mean squared error after {tfinal}s')
        plt.savefig(f'{savepath}/leapfrog_{x[q]}_log_rms_err_vs_stepsize_after_{tfinal}s.png')



plot_err(timesteps=timesteps, files=files, q=3, tfinal=4)

#plot_rms_err(timesteps=timesteps, files=files, q=3, tfinal=4,log=False )


    


