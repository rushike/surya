import math

M_SUN = 1.989e30
M_EARTH = 5.972e24
G = 6.6743e-11

rd = 147.11e6 # km
r = []

def gravity(rd):
  return G * M_SUN * M_EARTH / rd

# Assumption earth is moving tanget to sun at start
# Earth need to stay in orbit, so initial calculation will based of that
# Time unit is day

