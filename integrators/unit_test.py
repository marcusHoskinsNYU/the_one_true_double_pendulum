from rk4 import rk4
import numpy as np
import matplotlib.pyplot as plt


'''
For this unit test, I am going to use my integrator to evaluate: dx/dt=v, dv/dt=-w^2x
we know this should return x(t)=x0cos(wt), v(t)=-w*v0*sin(wt), 
so we are going run the integrator and make sure the |error| is less than dt**4

'''

tfinal=20
dt=10^-4
tvals=np.arange(0.0,tfinal,dt)
w=4
x0=1
v0=0

acceptable_err= 1e-12

def sho(r):

    x=r[0]
    v=r[1]
    fx=v
    fv=-w*w*x
    return( np.array([fx,fv]))


def test_integrator():



    rk4_results=rk4(tf=tfinal, h=dt, f=sho, r=[x0,v0])
    
    xt=rk4_results[:,0]
    vt=rk4_results[:,1]

    #check that x(t)=cos(wt)
 
    assert( all( np.abs( xt - x0 * np.cos( w * tvals ) ) < acceptable_err) )
    print(f'theta error below {acceptable_err}')


    #check that v(t)=-w*sin(wt)

    assert( all( np.abs(vt + w * v0 * np.sin(w*tvals) )  < acceptable_err)) 

    print(f'omega error below {acceptable_err}')


test_integrator()