import math

def generate_cylinder_control_points(radius, height, num_control_points):
    control_points = []
    theta = (2 * math.pi) / num_control_points
    
    for i in range(num_control_points):
        x = radius * math.cos(i * theta)
        y = radius * math.sin(i * theta)
        z = height / 2  # Choose any value for the z-coordinate
        
        control_points.append((x, y, z))
    
    return control_points

# Example usage
radius = 1.0
height = 2.0
num_control_points = 8

control_points = generate_cylinder_control_points(radius, height, num_control_points)
print(control_points)
