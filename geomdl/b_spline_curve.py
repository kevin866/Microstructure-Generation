"""
from geomdl import CPGen
from geomdl import BSpline
from geomdl import utilities
from geomdl.visualization import VisMPL
from matplotlib import cm
from geomdl.visualization import VisVTK

# Generate a plane with the dimensions 50x100
surfgrid = CPGen.Grid(50, 100)

# Generate a grid of 25x30
surfgrid.generate(50, 60)

# Generate bumps on the grid
surfgrid.bumps(num_bumps=5, bump_height=20, base_extent=8)

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set degrees
surf.degree_u = 3
surf.degree_v = 3

# Get the control points from the generated grid
surf.ctrlpts2d = surfgrid.grid

# Set knot vectors
surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, surf.ctrlpts_size_u)
surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, surf.ctrlpts_size_v)

# Set sample size
surf.sample_size = 100

# Set visualization component
surf.vis = VisVTK.VisSurface(ctrlpts=False, legend=False)

# Plot the surface
surf.render(colormap=cm.terrain)
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2019
"""

from geomdl import BSpline
from geomdl import CPGen
from geomdl import utilities
from geomdl import construct
from geomdl import operations
from geomdl.visualization import VisVTK as vis


# Generate control points grid for Surface #1
sg01 = CPGen.Grid(15, 10, z_value=0.0)
sg01.generate(8, 10)

# Create a BSpline surface instance
surf01 = BSpline.Surface()

# Set degrees
surf01.degree_u = 2
surf01.degree_v = 3

# Get the control points from the generated grid
surf01.ctrlpts2d = sg01.grid

# Set knot vectors
surf01.knotvector_u = utilities.generate_knot_vector(surf01.degree_u, surf01.ctrlpts_size_u)
surf01.knotvector_v = utilities.generate_knot_vector(surf01.degree_v, surf01.ctrlpts_size_v)

# Generate control points grid for Surface #2
sg02 = CPGen.Grid(15, 10, z_value=1.0)
sg02.generate(8, 10)

# Create a BSpline surface instance
surf02 = BSpline.Surface()

# Set degrees
surf02.degree_u = 2
surf02.degree_v = 3

# Get the control points from the generated grid
surf02.ctrlpts2d = sg02.grid

# Set knot vectors
surf02.knotvector_u = utilities.generate_knot_vector(surf02.degree_u, surf02.ctrlpts_size_u)
surf02.knotvector_v = utilities.generate_knot_vector(surf02.degree_v, surf02.ctrlpts_size_v)

# Generate control points grid for Surface #3
sg03 = CPGen.Grid(15, 10, z_value=2.0)
sg03.generate(8, 10)

# Create a BSpline surface instance
surf03 = BSpline.Surface()

# Set degrees
surf03.degree_u = 2
surf03.degree_v = 3

# Get the control points from the generated grid
surf03.ctrlpts2d = sg03.grid

# Set knot vectors
surf03.knotvector_u = utilities.generate_knot_vector(surf03.degree_u, surf03.ctrlpts_size_u)
surf03.knotvector_v = utilities.generate_knot_vector(surf03.degree_v, surf03.ctrlpts_size_v)

# Generate control points grid for Surface #4
sg04 = CPGen.Grid(15, 10, z_value=3.0)
sg04.generate(8, 10)

# Create a BSpline surface instance
surf04 = BSpline.Surface()

# Set degrees
surf04.degree_u = 2
surf04.degree_v = 3

# Get the control points from the generated grid
surf04.ctrlpts2d = sg04.grid

# Set knot vectors
surf04.knotvector_u = utilities.generate_knot_vector(surf04.degree_u, surf04.ctrlpts_size_u)
surf04.knotvector_v = utilities.generate_knot_vector(surf04.degree_v, surf04.ctrlpts_size_v)


# Construct the parametric volume with a uniform knot vector
pvolume = construct.construct_volume('w', surf01, surf02, surf03, surf04, degree=2)

# Visualize volume
pvolume.vis = vis.VisVolume(vis.VisConfig(ctrlpts=True, evalpts=False))
pvolume.render()

# Knot vector refinement
operations.refine_knotvector(pvolume, [1, 1, 1])

# Visualize volume after knot insertions
pvolume.render()

# Good to have something here to put a breakpoint
pass

