import dolfin as df
from __future__ import print_function
from fenics import *
from mshr import *
import numpy as np

diameter = 100.0 # mm
radius = diameter/2  
height = 33.33  # mm

detector = Cylinder(Point(0,0,height), Point(0,0,0), radius, radius)  # Create cylinder

# Geometry description:
ThickAl = 1;       # half thickness of charge and phonon circuits in mm
ThickSemi = 33.3;      # thickness of crystal in mm
WidthCin = 0.5; 
WidthC = 0.5         # WidthC = 0.020;   
WidthCout = 0.5;        # 2*9/13; # half width in mm
WidthP = 0.25;      # half width in mm
xC = np.linspace(3.2, 48, 15); 
xP = np.linspace(1.6, 46.4, 15);


# All Qinn_top charge lines
# Center cylinder (1)
cylinder = Cylinder(Point(0,0,ThickSemi+ThickAl), Point(0,0,ThickSemi-ThickAl), WidthCin, 32)
detector = detector - cylinder

# Middle lines (14 of them)
for n in range(0, 14):
    outer = Cylinder(Point(0, 0, ThickSemi-ThickAl), Point(0,0,ThickSemi+ThickAl), xC[n]+WidthC, 32)
    inner = Cylinder(Point(0, 0, ThickSemi-ThickAl), Point(0,0,ThickSemi+ThickAl), xC[n]-WidthC, 32)
    annulus = outer - inner
    detector = detector - annulus

# # Do Qout_top (1 of them)
outer = Cylinder(Point(0, 0, ThickSemi-ThickAl), Point(0,0,ThickSemi+ThickAl), xC[14]+WidthCout, 32)
inner = Cylinder(Point(0, 0, ThickSemi-ThickAl), Point(0,0,ThickSemi+ThickAl), xC[14]-WidthCout, 32)
annulus = outer - inner
detector = detector - annulus

domain = detector

mesh = generate_mesh(domain,32)
mesh_file = File("3Dworkaround_partial_thickness1.xml")
mesh_file << mesh
