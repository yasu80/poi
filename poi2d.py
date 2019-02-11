#coding:utf-8
import matplotlib.pyplot as plt

log = open('result.csv', 'w')

#cells_x = 50↲
cells_x = 1
cells_y = 10 #calcuration field↲

dx = 0.02
dy = 0.02

mu = 1
rho = -1
h = dy * cells_y
pressure_grad_x = 0.01

dpi_output = 3200
dpi_monitor = 192

result = [0 for i in range(cells_y + 1)]

def poi2d(y_arg):
  return 100000 * (y_arg - h) * y_arg * pressure_grad_x / (2 * rho * mu)

def savegraph():
  gridwidth = 1
  fig = plt.figure()
  x = 0
  y = 0
  for y in range(1,cells_y):
      plt.quiver(x,y,
      result[y],
      0.0,
      width = 0.01,
      color='red',angles='xy',scale_units='xy', scale=10) # ベクトル場をプロット
  plt.xlim([-1,1]) # 描くX
  plt.ylim([-1,cells_y+1]) # 描くy

  plt.gca().yaxis.set_tick_params(which='right', direction='out', bottom=False, top=True, left=False, right=True)

  plt.grid()
  plt.xlabel("X-axis")
  plt.ylabel("Y-axis")
  plt.savefig("result.png")
  plt.close()

for i in range (0,cells_x):
  for j in range (1,cells_y):
     y = dy * j
     result[j] = poi2d(y)
     log.write('\nx, ' + str(i) + ' y, ' + str(j) + ' vx, ' + str(result[j]))
savegraph()

log.close()



