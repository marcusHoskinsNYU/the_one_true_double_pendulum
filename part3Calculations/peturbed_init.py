import numpy as np 
import os
import sys
import matplotlib.pyplot as plt
print('Initializing...\n')

#Add the parent directory to sys.path otherwise i cant import rk4
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from integrators import rk4 
path = os.getcwd()

"""
This program examines the degree of chaos of the double pendulum system in three different behavior regimes. 
We examine the system near these three staionary points of lowest energy:
     1) both pendulums straight down (stable)
     2) top pendulum down, bottom pendulum up (unstable)
     3) top pendulum up, bottom pendulum down (unstable)
We begin with a fidicial set of initial conditions with energy slightly higher than these stationary points.

Then we ligtly perturb these conditions with generate_nearby_points() to create a number of sets of initial conditions
within the desired regime to compare the motion after some time. 

get_traj() will pass these initial conditions through the rk4 algorithm to simulate the trajectory of each system. 
Also passes trajectory data to a file in results/poincare_dat

compute_distances () reads in an array of all trajectories (including the fiducial trajectory) and computes the euclidian
distance between the perturbed systems and the fiducial system at each time and will plot the distances for each perturbed system 
also outports the distance data to results/distance_data

At the bottom of this file you can find the steps to run this program 
"""

def generate_nearby_points(fiducial, num_points, perturbation_scale=1e-4):
    """
    Generate nearby initial conditions around a fiducial point.

        fiducial: array of initial conditions [theta1, theta2, omega1, omega2].
        num_points: Number of nearby points to generate.
        perturbation_scale: Magnitude of random perturbation.
    """
    print("generating nearby points...")
    perturbations = np.random.uniform(
        -perturbation_scale, perturbation_scale, size=(num_points, len(fiducial))
    )
    return fiducial + perturbations

def get_traj(r0, num, f, perturbation_scale):

    """
    evaluates the trajectories of the set of 11 initial conditions and writes them to results so we may plot them individually
    """
    p1 = generate_nearby_points(r0, num, perturbation_scale)
    #print('p1',p1)

    # Store trajectories for fiducial and nearby points
    trajectories = []
    count = 0
    # Integrate the fiducial trajectory
    fiducial_trajectory = rk4.rk4(tf=t_final, h=dt, f=func, r = r0)
    trajectories.append(fiducial_trajectory)
    #np.savetxt( f'{path}/results/poincare_dat/1fid_rk4_{t_final}s_{r0[0]:.2f}_{r0[1]:.2f}_{r0[2]:.3f}_{r0[3]:.3f}_{dt*1e6}us_timesteps.csv', fiducial_trajectory, delimiter=',', header='theta1,theta2,omega1,omega2,t', comments='', fmt='%f')
    
    #Integrate each nearby point
    count += 1
    for point in p1:
        print(f'getting trajectory number {count} with rk4')
        count += 1
        traj = rk4.rk4(tf=t_final, h=dt, f=func, r=point)
        trajectories.append(traj)
        #print("saving file: ", f'{path}/results/poincare_dat/1_rk4_{t_final}s_{point[0]:.2f}_{point[1]:.2f}_{point[2]:.3f}_{point[3]:.3f}_{dt*1e6}us_timesteps.csv')
        #np.savetxt( f'{path}/results/poincare_dat/1_rk4_{t_final}s_{point[0]:.2f}_{point[1]:.2f}_{point[2]:.3f}_{point[3]:.3f}_{dt*1e6}us_timesteps.csv', traj, delimiter=',', header='theta1,theta2,omega1,omega2,t', comments='', fmt='%f') 

    return trajectories

def compute_distances(stationary_idx, trajectories, plot = False, save_file =  None):
    """
    Compute distances between the fiducial trajectory and perturbed trajectories.
    And Plots

    Returns:
        np.ndarray: Array of distances [N, num_points].
    """
    print(f'getting distances and plotting')
    perturbed_trajs = trajectories[1:]
    fiducial_traj = trajectories[0]
    time_vals = len(fiducial_traj)

    distances = []
    
    for traj in perturbed_trajs:
        # Compute Euclidean distance between fiducial and perturbed trajectory at each time step
        distance = np.sqrt(np.sum((fiducial_traj - traj)**2, axis=1))
        distances.append(distance)

    if save_file:
        print(f'saving distances to file')
        header = ','.join([f"Dist_to_point_{i+1}" for i in range(len(perturbed_trajs))])
        np.savetxt(save_file, distances, delimiter=",", header=header, comments='', fmt='%f')
        print(f"Distances saved to {save_file}")
    
    if plot:
        plotindex = 1
        # Time vector
        time_data = np.linspace(0, time_vals * dt, time_vals)  # Generate time values assuming a constant dt
        for dist in distances:
            plt.plot(time_data, dist)
            plt.xlabel('Time (s)')
            plt.ylabel('Euclidean Distance')
            plt.title(f'Distance between Fiducial and Perturbed Trajectories for region: {stationary_idx}')
            plt.show()
            plotindex += 1

    return distances


def runrunrun (stationary_idx, theta1, theta2, omega1, omega2, t_final, dt, num, f = rk4.f, perturbation_scale = 1e-4,):
    print(f'running\ntotal time = {t_final},\ndt = {dt},\nStationary point # {stationary_idx}\n')

    r1=np.array([ theta1  , theta2 , omega1, omega2], np.float64)
    trajectories = get_traj(r1, num, f , perturbation_scale)  

    output_dir = f"{path}/results/distance_data"
    os.makedirs(output_dir, exist_ok=True)

    # Save distances
    distances_file = f"{output_dir}/{stationary_idx}distances_rk4_{t_final}s_{dt*1e6}us_timesteps.csv"
    compute_distances(stationary_idx, trajectories, plot=True, save_file=distances_file)
    print(f"Distances saved to: {distances_file}")

"Below are three set of conditions for the three stationary points we are examining"
"Uncomment the one you wish to examine"


"""
#######################  begin stationary point 1: ###################
func = rk4.f

theta1=0
theta2=np.pi/60 # perturb by 3 degrees to get small motion 
omega1=0
omega2=0

stationary_idx = 1
t_final = 50
dt = .001
perturbationsize=1e-4
num = 10
runrunrun(stationary_idx, theta1, theta2, omega1, omega2,t_final, dt, num, func, perturbation_scale=perturbationsize )
########################## end stationary point 1 #######################
"""


"""
#######################  begin stationary point 2: ###################
func = rk4.f

theta1=0
theta2=np.pi
omega1=0
omega2=0.001

stationary_idx = 2
t_final = 50
dt = .001
perturbationsize=1e-4
num = 10
runrunrun(stationary_idx, theta1, theta2, omega1, omega2,t_final, dt, num, func, perturbation_scale=perturbationsize )
#######################  end stationary point 2: ###################
"""

#"""
#######################  begin stationary point 3: ###################
func = rk4.f
theta1=np.pi
theta2=0
omega1=0
omega2=0.001

stationary_idx = 3
t_final = 50
dt = .001
perturbationsize=1e-4
num = 10
runrunrun(stationary_idx, theta1, theta2, omega1, omega2,t_final, dt, num, func, perturbation_scale=perturbationsize )
########################## end stationary point 3 #######################
#"""

