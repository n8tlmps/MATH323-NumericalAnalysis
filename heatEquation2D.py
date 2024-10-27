import numpy as np
import matplotlib.pyplot as plt


"""
Characteristics of the rod:
    length:
    diffusivity: how fast temperature travels the rod

Discrete elements:
    Spatial --> Delta x
    Temporal --> Delta t
"""
# Defining our problem
# finite difference method (FDM)
# 
a = 110
length = 50 #mm
time = 4 #seconds
nodes = 30

"""
How to choose Delta x and Delta t
    Smaller Delta x --> better precision

To ensure stability, the time step Delta t must be chosen carefully.
    Delta t <= 0.5 * (Delta x)^2 / alpha
Derived from the stability analysis of this finite difference scheme and ensures that the numerical solution remains stable
"""
# Initialization
dx = length / nodes
dy = length / nodes
dt = min(dx**2 / (4 * a), dy**2 / (4 * a)) # stability conditions
t_nodes = int(time/dt)
# temperature at boundaries must be known at any time
# AND distribution starting the simulation must be known

#update to 2D vector
u = np.zeros((nodes, nodes)) + 20 # plate is initailly at 20 degrees C

# Boundary Conditions
u[0, :] = 100 # top boundary
u[-1, :] = 100 # bottom boundary

# Visualizizing with a plot
fig, axis = plt.subplots()
pcm = axis.pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)

# Simulating
counter = 0
while counter < time:
    w = u.copy()
    for i in range(1, nodes - 1):
        for j in range(1, nodes - 1):
            d2_ux = (w[i-1, j] - 2*w[i,j] + w[i+1, j]) / dx**2
            d2_uy = (w[i, j-1] - 2*w[i,j] + w[i, j+1]) / dy**2

            u[i, j] = dt * a *(d2_ux + d2_uy) + w[i, j]
    counter += dt
    print("t: {:.3f} [s], Average temperature: {:.2f} Celsius".format(counter, np.average(u)))

    # Updating the plot
    pcm.set_array(u)
    axis.set_title("Distribution at t: {:.3f} [s].".format(counter))
    plt.pause(0.01)


plt.show()