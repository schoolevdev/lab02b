# Lab02bvst.py
# This is the Student-Starting file of the
# Lab02b PI Approximation program.
# This version approximates PI with a 6-sided polygon.
#
from math import radians, sin, pi as mpi, degrees
#
# Initialize Variables
sides: int = 12
diameter: int = 2
interior_angle: float = 360 / sides
# get individual length of side using sine
side_length: float = sin(radians(interior_angle / 2))
# Compute PI for 6-Sided Polygon
pi = side_length * sides
#
# Program Output
print("PI Approximation Program Results")
print("Number of sides  ",sides)
print("PI Approximation ",pi)
print("Python's Math.pi  ",mpi)