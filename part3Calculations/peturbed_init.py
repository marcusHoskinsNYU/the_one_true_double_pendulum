import numpy as np 
import os
import sys
import matplotlib.pyplot as plt


# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from integrators import rk4, omegaDots 
path = os.getcwd()



def generate_nearby_points(fiducial, num_points, perturbation_scale=1e-3):
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



def get_traj(r0, num=10, e = 0.01):

    """
    evaluates the trajectories of the set of 11 initial conditions and writes them to results so we may plot them individually
    """
    p1 = generate_nearby_points(r0, num, e)
    #print('p1',p1)

    # Store trajectories for fiducial and nearby points
    trajectories = []
    count = 0
    # Integrate the fiducial trajectory
    fiducial_trajectory = rk4.rk4(tf=t_final, h=dt, f=f, r = r0)
    trajectories.append(fiducial_trajectory)
    np.savetxt( f'{path}/results/poincare_dat/1fid_rk4_{t_final}s_{r0[0]:.2f}_{r0[1]:.2f}_{r0[2]:.3f}_{r0[3]:.3f}_{dt*1e6}us_timesteps.csv', fiducial_trajectory, delimiter=',', header='theta1,theta2,omega1,omega2,t', comments='', fmt='%f')
    #Integrate each nearby point
    count += 1
    for point in p1:
        print(f'getting trajectory number {count} with rk4')
        count += 1
        traj = rk4.rk4(tf=t_final, h=dt, f=f, r=point)
        trajectories.append(traj)
        print("saving file: ", f'{path}/results/poincare_dat/1_rk4_{t_final}s_{point[0]:.2f}_{point[1]:.2f}_{point[2]:.3f}_{point[3]:.3f}_{dt*1e6}us_timesteps.csv')
        np.savetxt( f'{path}/results/poincare_dat/1_rk4_{t_final}s_{point[0]:.2f}_{point[1]:.2f}_{point[2]:.3f}_{point[3]:.3f}_{dt*1e6}us_timesteps.csv', traj, delimiter=',', header='theta1,theta2,omega1,omega2,t', comments='', fmt='%f') 

    return trajectories

def compute_distances(trajectories, plot = False):
    """
    Compute distances between the fiducial trajectory and perturbed trajectories.

    Returns:
        np.ndarray: Array of distances [N, num_points].
    """
    print(f'getting distances and plotting')
    perturbed_trajs = trajectories[1:]
    fiducial_traj = trajectories[0]
    time_vals = fiducial_traj.shape[0]

    distances = []
    for traj in perturbed_trajs:
        # Compute Euclidean distance between fiducial and perturbed trajectory at each time step
        distance = np.sqrt(np.sum((fiducial_traj - traj)**2, axis=1))
        distances.append(distance)

    if plot:
        # Time vector
        time_data = np.linspace(0, time_vals * dt, time_vals)  # Generate time values assuming a constant dt
        for dist in distances:
            plt.plot(time_data, dist)
        plt.xlabel('Time (s)')
        plt.ylabel('Distance')
        plt.title('Distance between Fiducial and Perturbed Trajectories')
        plt.show()

    return distances

from scipy.stats import linregress

def compute_lyapunov_exponent(distances, dt, fit_start=0, fit_end=None, plot=True):
    """
    Compute the largest Lyapunov exponent using the growth rate of distances.

    distances: List of arrays, where each array is the distance over time for one perturbed trajectory.
    dt: Time step used in the integration.
    fit_start: Index to start the fit (to exclude transient behavior).
    fit_end: Index to end the fit (to avoid saturation).
    plot: Whether to plot ln(distance) vs. time and the fit.

    Returns:
        lyapunov_exponents: List of estimated Lyapunov exponents for each perturbed trajectory.
    """
    time = np.arange(len(distances[0])) * dt
    lyapunov_exponents = []

    for distance in distances:
        # Restrict to the fit region
        log_distance = np.log(distance[fit_start:fit_end])
        time_fit = time[fit_start:fit_end]

        # Perform linear regression
        slope, intercept, r_value, p_value, std_err = linregress(time_fit, log_distance)
        lyapunov_exponents.append(slope)  # Slope corresponds to lambda

        if plot:
            plt.plot(time_fit, log_distance, label='ln(d(t))')
            plt.plot(time_fit, slope * time_fit + intercept, label=f'Fit: λ = {slope:.3f}')
            plt.xlabel('Time (s)')
            plt.ylabel('ln(distance)')
            plt.legend()
            plt.title('Lyapunov Exponent Estimation')
            plt.show()

    return lyapunov_exponents



#fiducial initial conditions for stationary point 1
theta1=0
theta2=np.pi/4
omega1=0
omega2=0
t_final = 1000
dt = .001
f = rk4.f

r1=np.array([ theta1  , theta2 , omega1, omega2], np.float64)
trajectories = get_traj(r1)  # Assuming this function returns a list of fiducial and perturbed trajectories
distances = compute_distances(trajectories) 

fit_start = 100  # Skip initial transient
fit_end = 1000   # Adjust as needed
lyapunov_exponents = compute_lyapunov_exponent(distances, dt, fit_start=fit_start, fit_end=fit_end)
print("Estimated Lyapunov exponents:", lyapunov_exponents)


'''








#fiducial initial conditions for stationary point 2
theta1=0
theta2=np.pi
omega1=0
omega2=0.1

r2=np.array([ theta1  , theta2 , omega1, omega2], np.float64)
p2 = generate_nearby_points(r2, 10, 0.01)
print('p2',p2)


#fiducial initial conditions for stationary point 3
theta1=np.pi
theta2=0
omega1=0
omega2=0.1

r3=np.array([ theta1  , theta2 , omega1, omega2], np.float64)
p3 = generate_nearby_points(r3, 10, 0.1)
print('p3',p3)

'''