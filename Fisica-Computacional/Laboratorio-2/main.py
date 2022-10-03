GRAVITY: float = 9.8 

def tension(m: float, x: float) -> float:
  return m*(x + GRAVITY)

def DCL(m1: any, m2: any) -> any:
  if m1 > m2:
    x: any = ((m1 - m2)/(m1 + m2))*GRAVITY
    t: any = tension(m1, x)
    return x, t

  if m2 > m1:
    x: any = ((m2 - m1)/(m1 + m2))*GRAVITY
    t: any = tension(m1, x)
    return x, t

  return 0, 0

"""
    PRUEBAS
"""

import random

m1_m2_lab: list = []

m1_arr: list = []
m2_arr: list = []
ac_arr: list = []
te_arr: list = []

for i in range(20):
  a = random.randrange(1, 100)
  b = random.randrange(1, 100)

  label_a_b: str = f'{a}, {b}'
  m1_m2_lab.append(label_a_b)

  ac, te = DCL(a, b)
  
  m1_arr.append(a)
  m2_arr.append(b)
  ac_arr.append(ac)
  te_arr.append(te)

from matplotlib import pyplot as plt 
import numpy as np

X = m1_m2_lab
Ygirls = ac_arr
Zboys = te_arr
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, Ygirls, 0.4, label = 'Aceleración')
plt.bar(X_axis + 0.2, Zboys, 0.4, label = 'Tensión')
  
plt.xticks(X_axis, X, rotation=90)
plt.xlabel("M1 y M2")
plt.ylabel("Valor")
plt.title("Ploteo de Aceleración y Tensión")
plt.legend()
plt.show()

