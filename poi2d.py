#coding:utf-8

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

def poi2d(y_arg):
  return (y_arg - h) * y_arg * pressure_grad_x / (2 * rho * mu)


for i in range (0,cells_x):
  for j in range (1,cells_y):
     y = dy * j
     log.write('\nx, ' + str(i) + ' y, ' + str(j) + ' vx, ' + str(poi2d(y)))

log.close()

