
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

path='/Users/Krishna/Documents/repositories/the_one_true_double_pendulum'

'''
#if you are not krishna, then uncomment this code

path=os.path.dirname(cwd)
'''

filename='partb_rk4_20s_0.2_ms_timesteps.csv'

dp = np.loadtxt(f'{path}/results/{filename}', delimiter=',', skiprows=1)

skip=100

theta1, theta2, tList=dp[::skip,0], dp[::skip,1], dp[::skip,4]


#chatgpt correction:

fig, ax = plt.subplots() 
L = 0.4
width = 2.5
length = 3
ax.set_xlim((-L * length, L * length))
ax.set_ylim((-width * L, width * L))
ax.set_xlabel('x position (meters)')
ax.set_ylabel('y position (meters)')

line1, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)
p1, = ax.plot([], [], 'bo', markersize=10)
p2, = ax.plot([], [], 'ro', markersize=10)

# Calculating pendulum positions
m1_xvals = L * np.sin(theta1)
m1_yvals = -L * np.cos(theta1)
m2_xvals = m1_xvals + L * np.sin(theta2)
m2_yvals = m1_yvals - L * np.cos(theta2)

def init():
    p1.set_data([], [])
    p2.set_data([], [])
    line1.set_data([], [])
    line2.set_data([], [])
    return p1, p2, line1, line2

def animate(i):
    print(f"Animating frame {i+1}/{len(tList)}")  # Debugging 

    # Update masses (ensure to pass the values as sequences)
    p1.set_data([m1_xvals[i]], [m1_yvals[i]])  #point mass 1
    p2.set_data([m2_xvals[i]], [m2_yvals[i]])  #point mass 3
    
    # Update rods (pass sequences for line data)
    line1.set_data([0, m1_xvals[i]], [0, m1_yvals[i]]) 
    line2.set_data([m1_xvals[i], m2_xvals[i]], [m1_yvals[i], m2_yvals[i]])
    
    return p1, p2, line1, line2
anim = FuncAnimation(fig, animate, init_func=init, frames=len(tList), blit=True)

# Save the animation
anim.save(f"{path}/animations/{filename}_animation.gif", writer="pillow", fps=100)


