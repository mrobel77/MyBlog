import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


total_points = 10000


inside_x = []
inside_y = []
outside_x = []
outside_y = []

# Initialize count of points inside the quarter circle
count = 0

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Function to initialize the plot
def init():
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    return ax,

# Function to update the plot with each frame
def update(frame):
    global count
    
    x = np.random.rand()
    y = np.random.rand()
    
    if x**2 + y**2 <= 1:
        inside_x.append(x)
        inside_y.append(y)
        count += 1
    else:
        outside_x.append(x)
        outside_y.append(y)
    
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.scatter(inside_x, inside_y, color='green', s=8)
    ax.scatter(outside_x, outside_y, color='red', s=8)
    
    # Calculate and display the current estimate of π
    pi = 4 * count / (frame + 1)
    ax.set_title(f'Estimation of π: {pi:.5f} after {frame+1} points')

    return ax,

# Create the animation
ani = FuncAnimation(fig, update, frames=total_points, init_func=init, blit=True, interval=0.001, repeat=False)

print(4 * count /total_points)
# Display the animation
plt.show()
