import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Streamlit UI
st.title("Simple Pendulum Simulation 🌗")

length = st.slider("Pendulum Length (m)", 0.1, 5.0, 1.0, 0.1)
mass = st.slider("Mass (kg)", 0.1, 10.0, 1.0, 0.1)
theta0_deg = st.slider("Initial Angle (degrees)", -90, 90, 30)
g = st.slider("Gravity (m/s²)", 1.0, 20.0, 9.8, 0.1)

theta0 = np.radians(theta0_deg)

# Solve pendulum equation using small angle approximation
t = np.linspace(0, 10, 1000)
omega = np.sqrt(g / length)
theta = theta0 * np.cos(omega * t)

x = length * np.sin(theta)
y = -length * np.cos(theta)

# Plot the pendulum motion
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-length - 0.2, length + 0.2)
ax.set_ylim(-length - 0.2, 0.2)
ax.set_title("Pendulum Motion")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")

line, = ax.plot([], [], 'o-', lw=2, color='darkblue')
trail, = ax.plot([], [], 'r--', lw=0.5)

def init():
    line.set_data([], [])
    trail.set_data([], [])
    return line, trail

def update(frame):
    line.set_data([0, x[frame]], [0, y[frame]])
    trail.set_data(x[:frame], y[:frame])
    return line, trail

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True)

st.pyplot(fig)
