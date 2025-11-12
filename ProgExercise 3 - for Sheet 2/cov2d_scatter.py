import numpy as np
from math import *
import matplotlib.pyplot as plt

# FILL THIS FUNCTION
def rot_cov(angle, scale_x, scale_y):
    cov = [[1, 0], [0, 1]]
    # Build rotation matrix R and diagonal scale matrix D, then compute R D R^T
    # angle in radians, scale_x/scale_y are treated as variances along local axes
    R = np.array([[cos(angle), -sin(angle)], [sin(angle), cos(angle)]], dtype=float)
    D = np.array([[scale_x, 0.0], [0.0, scale_y]], dtype=float)
    C = R.dot(D).dot(R.T)
    return [[float(C[0,0]), float(C[0,1])], [float(C[1,0]), float(C[1,1])]]
    
def extract_angles_from_cov(cov):
    angle1 = 0
    angle2 = 0
    
    # Convert to numpy array and get eigenvectors (principal axes)
    C = np.array(cov, dtype=float)
    eigvals, eigvecs = np.linalg.eig(C)
    # eigvecs columns are eigenvectors. Compute angle of each eigenvector
    v1 = eigvecs[:,0]
    v2 = eigvecs[:,1]
    angle1 = np.arctan2(v1[1], v1[0])
    angle2 = np.arctan2(v2[1], v2[0])
    # Normalize angles to be between -pi/2 and pi/2 for comparison
    # and make sure angle1 <= angle2
    a1 = angle1
    a2 = angle2
    if a2 < a1:
        a1, a2 = a2, a1
    print("Angle 1:", a1*180/pi)
    print("Angle 2:", a2*180/pi)
    print("Difference:", (a2-a1)*180/pi)
    return a1, a2

# Build data
mean = [0, 0]
cov = [[22, 7],[7,4]]
# cov = rot_cov(30*pi/180, 5, 1)
print(cov)
extract_angles_from_cov(cov)

# Make a scatter plot of 1000 points following the mean and covariance
x, y = np.random.multivariate_normal(mean, cov, 1000).T

# ...and plot
fig = plt.figure()
ax = fig.add_subplot()
ax.scatter(x, y)
ax.axis("equal")
plt.show()
