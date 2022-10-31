from cmath import sqrt
import math

#ENV 

G = 6.673*(10**-11)
PI = math.pi

#1

def get_gravity(
  m: float, r: float) -> float:
  return G*(m/r**2)

#2

def get_density(
  m: float, r: float) -> float:
  return m/((4/3)*PI*(r**3))

#3

def sec_law_kepler(
  l: float, m: float, t: float) -> float:
  return (l/(2*m))*t

#4

def third_kepler_law(
  r: float, m: float) -> float:
  return sqrt((4*(PI**2)/G*m)*(r**3))
  