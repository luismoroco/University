import numpy as np
import matplotlib.pyplot as plt

def plot_figure(k_iter, m, n, u_mat, A, B):
  print(f'ITERACIONES: {k_iter} \n')
  x = np.array([i + 1 for i in range (m + 2)])
  y = np.array([i + 1 for i in range (n + 2)])
  X_m, Y_m = np.meshgrid(x, y)
  print(f'U_MAT: {u_mat}\n MALLA X: {X_m}\n MALLA Y: {Y_m}\n')

  plot_img = plt.figure(figsize = (A, B))
  img_ax = plt.axes(projection = '3d')
  img_hm = img_ax.plot_surface(X_m, Y_m, u_mat, cmap = plt.get_cmap('winter'))
  plot_img.colorbar(img_hm, ax = img_ax, shrink = 0.5, aspect = 5)
  img_ax.set_title('PROPAGACIÓN DEL CALOR')
  plt.show()

def calor_propagation_f(
  ua, ub, uc, ud, 
  n, m, h, error, r_value) -> None:

  if uc > ud or uc < 0 or ud < 0:
    print("DATOS INVÁLIDOS\n")
    return

  u_mat = np.zeros((n + 2, m + 2))

  for i in range(n + 2):
    u_mat[i][0] = uc 
    u_mat[i][m + 1] = ud

  for i in range(m + 2):
    u_mat[0][i] = ua
    u_mat[n + 1][i] = ud

  p = (ua + ub + uc + ud) / 4

  for i in range(1, n + 1):
    for j in range(1, m + 1):
      u_mat[i][j] = p
  
  k_iter: int = 0
  convergent: bool = False

  tmp_u_mat: any = 0
  while k_iter < h and (convergent is False):
    k_iter += 1
    tmp_u_mat = u_mat
    
    for i in range(1, n + 1):
      for j in range(1, m + 1):
        u_mat[i][j + 1] = ((1 - (2 * r_value)) * u_mat[i][j]) + (r_value * (u_mat[i + 1][j] - (2 * u_mat[i][j]) + u_mat[i - 1][j]))

    u_dif = u_mat - tmp_u_mat

    if np.linalg.norm(u_dif) < error:
      convergent = True
  
  if convergent is False:
    print("NO CONVERGE!\n")
  else:
    plot_figure(k_iter=k_iter, m=m, n=n, u_mat=u_mat, A=14, B=9)

# Example 
calor_propagation_f(80, 0, 20, 300, 4, 4, 100, 1, 8)
