from geomdl import compatibility
from geomdl import BSpline
from geomdl import CPGen
from geomdl import multi
from geomdl import utilities
from geomdl import construct
from geomdl.visualization import VisVTK


ctrlpts = [
    [[-25.0, -25.0, -10.0], [-25.0, -15.0, -5.0], [-25.0, -5.0, 0.0], [-25.0, 5.0, 0.0], [-25.0, 15.0, -5.0], [-25.0, 25.0, -10.0]],
    [[-15.0, -25.0, -8.0], [-15.0, -15.0, -4.0], [-15.0, -5.0, -4.0], [-15.0, 5.0, -4.0], [-15.0, 15.0, -4.0], [-15.0, 25.0, -8.0]],
    [[-5.0, -25.0, -5.0], [-5.0, -15.0, -3.0], [-5.0, -5.0, -8.0], [-5.0, 5.0, -8.0], [-5.0, 15.0, -3.0], [-5.0, 25.0, -5.0]],
    [[5.0, -25.0, -3.0], [5.0, -15.0, -2.0], [5.0, -5.0, -8.0], [5.0, 5.0, -8.0], [5.0, 15.0, -2.0], [5.0, 25.0, -3.0]],
    [[15.0, -25.0, -8.0], [15.0, -15.0, -4.0], [15.0, -5.0, -4.0], [15.0, 5.0, -4.0], [15.0, 15.0, -4.0], [15.0, 25.0, -8.0]],
    [[25.0, -25.0, -10.0], [25.0, -15.0, -5.0], [25.0, -5.0, 2.0], [25.0, 5.0, 2.0], [25.0, 15.0, -5.0], [25.0, 25.0, -10.0]]
]
print(len(ctrlpts))
print(len(ctrlpts[0]))
print(len(ctrlpts[0][0]))

# Generate control points grid for Surface #1
sg01 = CPGen.Grid(15, 10, z_value=10.0)
sg01.generate(8, 8)
# Create a BSpline surface instance
surf01 = BSpline.Surface()

# Set degrees
surf01.degree_u = 3
surf01.degree_v = 3

# Get the control points from the generated grid
surf01.ctrlpts2d = compatibility.generate_ctrlptsw2d(ctrlpts)
print(surf01.ctrlpts_size_u)
print(surf01.ctrlpts_size_v)
# Set knot vectors
surf01.knotvector_u = utilities.generate_knot_vector(surf01.degree_u, surf01.ctrlpts_size_u)
surf01.knotvector_v = utilities.generate_knot_vector(surf01.degree_v, surf01.ctrlpts_size_v)

# Generate control points grid for Surface #2
sg02 = CPGen.Grid(15, 10, z_value=8.0)
sg02.generate(8, 8)

# Create a BSpline surface instance
surf02 = BSpline.Surface()

# Set degrees
surf02.degree_u = 3
surf02.degree_v = 3

# Get the control points from the generated grid
surf02.ctrlpts2d = compatibility.generate_ctrlptsw2d(ctrlpts)

# Set knot vectors
surf02.knotvector_u = utilities.generate_knot_vector(surf02.degree_u, surf02.ctrlpts_size_u)
surf02.knotvector_v = utilities.generate_knot_vector(surf02.degree_v, surf02.ctrlpts_size_v)

# Generate control points grid for Surface #3
sg03 = CPGen.Grid(15, 10, z_value=2.0)
sg03.generate(8, 8)

# Create a BSpline surface instance
surf03 = BSpline.Surface()

# Set degrees
surf03.degree_u = 3
surf03.degree_v = 3

# Get the control points from the generated grid
surf03.ctrlpts2d = compatibility.generate_ctrlptsw2d(ctrlpts)

# Set knot vectors
surf03.knotvector_u = utilities.generate_knot_vector(surf03.degree_u, surf03.ctrlpts_size_u)
surf03.knotvector_v = utilities.generate_knot_vector(surf03.degree_v, surf03.ctrlpts_size_v)

# Construct the parametric volume
pvolume = construct.construct_volume('w', surf01, surf02, surf03, degree=1)

# Construct the isosurface
surfiso = construct.extract_isosurface(pvolume)
msurf = multi.SurfaceContainer(surfiso)

# Render the isourface
msurf.vis = VisVTK.VisSurface(VisVTK.VisConfig(ctrlpts=False, legend=False))
msurf.delta = 0.05
msurf.render(evalcolor=["skyblue", "cadetblue", "crimson", "crimson", "crimson", "crimson"])