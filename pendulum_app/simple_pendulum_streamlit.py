import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit UI
st.title("Simple Pendulum Simulation 🌗")

length = st.slider("Pendulum Length (m)", 0.1, 5.0, 1.0, 0.1)
mass = st.slider("Mass (kg)", 0.1, 10.0, 1.0, 0.1)
theta0_deg = st.slider("Initial Angle (degrees)", -90, 90, 30)
g = st.slider("Gravity (m/s²)", 1.0, 20.0, 9.8, 0.1)

# Time control
t_max = 10
t_slider = st.slider("Time (s)", 0.0, float(t_max), 0.0, step=0.05)

theta0 = np.radians(theta0_deg)
omega = np.sqrt(g / length)
theta = theta0 * np.cos(omega * t_slider)

x = length * np.sin(theta)
y = -length * np.cos(theta)

# Plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-length - 0.2, length + 0.2)
ax.set_ylim(-length - 0.2, 0.2)
ax.set_title("Pendulum at t = {:.2f}s".format(t_slider))
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.plot([0, x], [0, y], 'o-', lw=2, color='darkblue')
ax.plot(x, y, 'ro')  # bob

st.pyplot(fig)
