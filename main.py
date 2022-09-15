# Lab02bvst.py
# This is the Student-Starting file of the
# Lab02b PI Approximation program.
# This version approximates PI with a 6-sided polygon.
#
import math
#
# Initialize Variables
sides = 6
AB = 1.0
AD = 2.0
#
# Compute PI for 6-Sided Polygon
perimeter = AB * sides
pi = perimeter / AD
#
# Program Output
print("PI Approximation Program Results")
print("Number of sides  ",sides)
print("PI Approximation ",pi)
print("Python's Math.pi  ",math.pi)