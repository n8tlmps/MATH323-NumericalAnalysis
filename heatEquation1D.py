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
a = 110
length = 50 #mm
time = 4 #seconds
nodes = 10

"""
How to choose Delta x and Delta t
    Smaller Delta x --> better precision

To ensure stability, the time step Delta t must be chosen carefully.
    Delta t <= 0.5 * (Delta x)^2 / alpha
Derived from the stability analysis of this finite difference scheme and ensures that the numerical solution remains stable
"""
# Initialization
dx = length / nodes
dt = 0.5 * dx**2 / a
t_nodes = int(time/dt)
# temperature at boundaries must be known at any time
# AND distribution starting the simulation must be known

u = np.zeros(nodes) + 20 # plate is initailly at 20 degrees C

# Boundary Conditions
u[0] = 100
u[-1] = 100

# Visualizizing with a plot
fig, axis = plt.subplots()
pcm = axis.pcolormesh([u], cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)
axis.set_ylim([-2,3])
# Simulating
counter = 0
while counter < time:
    w = u.copy()
    for i in range(1, nodes - 1):
        u[i] = dt * a * (w[i - 1] - 2 * w[i] + w[i + 1]) / dx ** 2 + w[i]
    counter += dt
    print("t: {:.3f} [s], Average temperature: {:.2f} Celsius".format(counter, np.average(u)))

    # Updating the plot
    pcm.set_array([u])
    axis.set_title("Distribution at t: {:.3f} [s].".format(counter))
    plt.pause(0.01)


plt.show()