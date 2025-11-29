import numpy as np
import matplotlib.pyplot as plt

# 1. Simulate Sensor Data (Distance over Azimuth)
# We create 360 azimuth readings (0 to 360 degrees)
azimuths_deg = np.linspace(0, 360, 360)  

# Convert degrees to radians for numpy math functions
azimuths_rad = np.radians(azimuths_deg)
  
# Create dummy distances (simulating a circular room with some noise)
# "10" is the base radius, and we add random noise
distances = 10 + np.random.normal(0, 0.5, size=len(azimuths_rad))  

# Let's add a fake rectangular obstacle closer to the sensor between 45 and 90 degrees
distances[45:90] = 5.0 + np.random.normal(0, 0.1, size=45)

# 2. Convert Polar to Cartesian (The Math Part)
# x = r * cos(theta)
# y = r * sin(theta)
x = distances * np.cos(azimuths_rad)
y = distances * np.sin(azimuths_rad)

# 3. Plot the Data
plt.figure(figsize=(8, 8))

# Plot the detected points
plt.scatter(x, y, s=10, label='Detected Obstacles')

# Plot the sensor itself at the origin (0,0)
plt.scatter(0, 0, color='red', marker='x', s=100, label='Sensor Position')

plt.title("Sensor Scan: Polar to Cartesian Conversion")
plt.xlabel("X Distance (meters)")
plt.ylabel("Y Distance (meters)")
plt.grid(True)
plt.legend()

# Ensure the aspect ratio is equal so circles don't look like ovals
plt.axis('equal')

plt.show()
