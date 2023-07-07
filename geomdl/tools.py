from random import randint
from geomdl import BSpline
from geomdl import utilities
from geomdl import BSpline
from geomdl import multi

from geomdl import construct
from geomdl.visualization import VisVTK as vis
from random import randint
def random_digits(x):
    if len(x) == 1:
        return [float(randint(0, 10)) for _ in range(x[0])]
    return [random_digits(x) for _ in range(x.pop())]


def generate_surface(ctrlpts, degree_u, degree_v):
    # Create a BSpline surface
    surf = BSpline.Surface()

    # Set degrees
    surf.degree_u = degree_u
    surf.degree_v = degree_v

    # Set control points
    surf.ctrlpts2d = ctrlpts

    # Set knot vectors
    surf.knotvector_u = utilities.generate_knot_vector(degree_u, len(ctrlpts))
    surf.knotvector_v = utilities.generate_knot_vector(degree_v, len(ctrlpts[0]))
    #surf.knotvector_u = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0,4.0]
    #surf.knotvector_v = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0,4.0]

    # Set evaluation delta
    surf.delta = 0.025

    # Evaluate surface points
    surf.evaluate()

    # Import and use Matplotlib's colormaps
    from matplotlib import cm

    # Plot the control points grid and the evaluated surface
    surf.vis = vis.VisSurface()
    surf.render(colormap=cm.cool)

def generate_volume(u_size,v_size,z_size, degree_u, degree_v, degree_w, offset):
    vol = BSpline.Volume()

    # Set degree
    vol.degree_u = degree_u
    vol.degree_v = degree_v
    vol.degree_w = degree_w
    vol.ctrlpts_size_u=u_size
    vol.ctrlpts_size_v=v_size
    vol.ctrlpts_size_w=z_size
    # Set control points
    #
    vol.ctrlpts = [[float(randint(0, 10))-50.0 for _ in range(3)] for _ in range(u_size*v_size*z_size)]+[[float(randint(0, 10))+50.0 for _ in range(3)] for _ in range(u_size*v_size*z_size)]
    #print(vol.ctrlpts)
    #curve.ctrlpts = tools.random_digits(3,6,6)
    #tools.random_digits(3,6,6)
    #

    #
    #print(curve.ctrlpts)
    # Set knot vector
    vol.knotvector_u = utilities.generate_knot_vector(vol.degree_u, vol.ctrlpts_size_u)
    vol.knotvector_v = utilities.generate_knot_vector(vol.degree_v, vol.ctrlpts_size_u)
    vol.knotvector_w = utilities.generate_knot_vector(vol.degree_w, vol.ctrlpts_size_u)
    #print(curve.knotvector_w)

    # Set evaluation delta (controls the number of curve points)
    vol.delta_u = 0.025
    vol.delta_v = 0.025
    vol.delta_w = 0.025
    vol.evaluate()

    from matplotlib import cm

    # Plot the control points grid and the evaluated surface
    vol.vis = vis.VisVoxel()
    
    #curve.render(colormap = cm.cool)
    # Voxelize the volume
    vol.vis = vis.VisVoxel(vis.VisConfig(ctrlpts_offset = offset))

    vol.render(evalcolor="firebrick", num_procs=16)

    # Extract the isosurface
    surfvol = construct.extract_isosurface(vol)
    msurf = multi.SurfaceContainer(surfvol)

    # Visualize the isosurface
    msurf.vis = vis.VisSurface(vis.VisConfig(ctrlpts=False))
    msurf.delta = 0.05
    msurf.render(evalcolor=["skyblue", "cadetblue", "crimson", "crimson", "crimson", "crimson"])
    return