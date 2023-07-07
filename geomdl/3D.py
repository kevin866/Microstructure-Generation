from geomdl import BSpline
from geomdl import multi

from geomdl import BSpline
from geomdl import utilities
from geomdl import construct
from geomdl.visualization import VisVTK as vis
from random import randint
#sha = Sphere()
#sha.evaluate()
# Create a 3-dimensional B-spline Curve
curve = BSpline.Volume()

# Set degree
curve.degree_u = 3
curve.degree_v = 3
curve.degree_w = 3
curve.ctrlpts_size_u=8
curve.ctrlpts_size_v=8
curve.ctrlpts_size_w=8
# Set control points
#
curve.ctrlpts = [[float(randint(0, 100)) for _ in range(3)] for _ in range(512)]
#curve.ctrlpts = tools.random_digits(3,6,6)
#tools.random_digits(3,6,6)
#

#
#print(curve.ctrlpts)
# Set knot vector
curve.knotvector_u = utilities.generate_knot_vector(curve.degree_u, curve.ctrlpts_size_u)
curve.knotvector_v = utilities.generate_knot_vector(curve.degree_v, curve.ctrlpts_size_u)
curve.knotvector_w = utilities.generate_knot_vector(curve.degree_w, curve.ctrlpts_size_u)
#print(curve.knotvector_w)

# Set evaluation delta (controls the number of curve points)
curve.delta_u = 0.025
curve.delta_v = 0.025
curve.delta_w = 0.025
curve.evaluate()

from matplotlib import cm

# Plot the control points grid and the evaluated surface
curve.vis = vis.VisVoxel()
#curve.render(colormap = cm.cool)
# Voxelize the volume
pvolume = curve
pvolume.vis = vis.VisVoxel(vis.VisConfig(ctrlpts=False))

#pvolume.render(evalcolor="firebrick", num_procs=16)

# Extract the isosurface
surfvol = construct.extract_isosurface(pvolume)
msurf = multi.SurfaceContainer(surfvol)

# Visualize the isosurface
msurf.vis = vis.VisSurface(vis.VisConfig(ctrlpts=False))
msurf.delta = 0.05
msurf.render(evalcolor=["skyblue", "cadetblue", "crimson", "crimson", "crimson", "crimson"])