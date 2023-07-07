import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def bezier_vector_function(control_points, u_samples=50, v_samples=50, w_samples=50):
    """Generate a trivariate Bezier vector function from control points"""
    n, m, l = control_points.shape[0] - 1, control_points.shape[1] - 1, control_points.shape[2] - 1
    u = np.linspace(0, 1, u_samples)
    v = np.linspace(0, 1, v_samples)
    w = np.linspace(0, 1, w_samples)
    function_points = np.zeros((u_samples, v_samples, w_samples, 3))

    for i in range(u_samples):
        for j in range(v_samples):
            for k in range(w_samples):
                point = np.zeros(3)
                for p in range(n + 1):
                    for q in range(m + 1):
                        for r in range(l + 1):
                            coefficient = comb(n, p) * comb(m, q) * comb(l, r)
                            basis_u = u[i]**p * (1 - u[i])**(n - p)
                            basis_v = v[j]**q * (1 - v[j])**(m - q)
                            basis_w = w[k]**r * (1 - w[k])**(l - r)
                            point += coefficient * basis_u * basis_v * basis_w * control_points[p, q, r]
                function_points[i, j, k] = point

    return function_points

# Control points for a 2x2x2 grid
control_points = np.array([
    [[[-1, -1, -1], [0, -1, 0]],
     [[-1, -1, 1], [0, -1, 2]]],
    [[[-1, 1, -1], [0, 1, 0]],
     [[-1, 1, 1], [0, 1, 2]]]
])
"""rng = np.random.default_rng()
control_points = rng.random((2,2,2,3))"""

# Generate the vector function
function_points = bezier_vector_function(control_points)

# Extract the coordinates
u, v, w = np.meshgrid(np.linspace(0, 1, function_points.shape[0]),
                      np.linspace(0, 1, function_points.shape[1]),
                      np.linspace(0, 1, function_points.shape[2]))

x = function_points[..., 0]
y = function_points[..., 1]
z = function_points[..., 2]

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=u.flatten(), cmap='viridis')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Trivariate Bezier Vector Function')

# Show the plot
plt.show()
