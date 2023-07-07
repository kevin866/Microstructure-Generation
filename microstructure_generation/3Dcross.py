import pyvista as pv
import numpy as np

# Define cylinder parameters
radius = 1
height = 5

# Create the three cylinders representing each arm of the cross
cylinder1 = pv.Cylinder(center=(0, 0, 0), direction=(1, 0, 0), radius=radius, height=height)
cylinder2 = pv.Cylinder(center=(0, 0, 0), direction=(0, 1, 0), radius=radius, height=height)
cylinder3 = pv.Cylinder(center=(0, 0, 0), direction=(0, 0, 1), radius=radius, height=height)
print(cylinder1)
# Combine the cylinders to form a cross
cross = cylinder1 + cylinder2 + cylinder3

# Create the plotter
p = pv.Plotter()
p.add_mesh(cross, color="lightblue")

# Show the plot
p.show()