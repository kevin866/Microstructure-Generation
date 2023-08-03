from geomdl import BSpline
from geomdl.visualization import VisVTK
import iga

# Create a 3D NURBS curve representing the shape of the object
curve = BSpline.Curve()

# Set the control points (modify this according to your shape)
control_points = [[0, 0, 0], [1, 3, 2], [2, 2, 4], [3, 0, 3]]
curve.degree = 3
curve.ctrlpts = control_points

# Generate the NURBS curve
curve.knotvector = curve.knotvector.generate(curve.degree, len(curve.ctrlpts))
curve.delta = 0.01
curve.evaluate()

# Create a 3D NURBS surface by extruding the 3D NURBS curve along the Z-axis
surface = BSpline.Surface()
surface.degree_u = curve.degree
surface.degree_v = 1  # Keep it linear in the V direction for an extrusion
surface.ctrlpts_size_u = len(curve.ctrlpts)
surface.ctrlpts_size_v = 2  # Number of extrusion steps (can be modified for a smoother surface)
surface.ctrlpts = [p for p in curve.ctrlpts for _ in range(surface.ctrlpts_size_v)]

# Generate the NURBS surface
surface.knotvector_u = surface.knotvector.generate(surface.degree_u, len(surface.ctrlpts))
surface.knotvector_v = surface.knotvector.generate(surface.degree_v, surface.ctrlpts_size_v)
surface.delta = 0.01
surface.evaluate()

# Create a 3D NURBS volume by sweeping the 3D NURBS surface along the Y-axis
volume = BSpline.Volume()
volume.degree_u = surface.degree_u
volume.degree_v = surface.degree_v
volume.degree_w = 1  # Keep it linear in the W direction for a simple extrusion
volume.ctrlpts_size_u = len(surface.ctrlpts)
volume.ctrlpts_size_v = 2  # Number of extrusion steps (can be modified for a smoother volume)
volume.ctrlpts_size_w = 2  # Number of extrusion steps along W (can be modified for a smoother volume)
volume.ctrlpts = [p for p in surface.ctrlpts for _ in range(volume.ctrlpts_size_w)]

# Generate the NURBS volume
volume.knotvector_u = volume.knotvector.generate(volume.degree_u, len(volume.ctrlpts))
volume.knotvector_v = volume.knotvector.generate(volume.degree_v, volume.ctrlpts_size_v)
volume.knotvector_w = volume.knotvector.generate(volume.degree_w, volume.ctrlpts_size_w)
volume.delta = 0.01
volume.evaluate()

# You now have a 3D NURBS volumetric model represented by 'volume'
