import numpy as np
import matplotlib.pyplot as plt
from utilities import *

#control points
x = np.array([[-0.5,-2,0],[1,1,1],[2,2,2]])
y = np.array([[2,1,0],[2,0,-1],[2,1,1]])
z = np.array([[1,-1,2],[0,-0.5,2],[0.5,1,2]])

#number of cells for each direction
ncellu = 12
ncellw = 10

#total number of control points in u
uPTs = np.size(x, 0)
wPTs = np.size(x, 1)
#total number of subdivisions
n = uPTs-1
m = wPTs-1
#parametric var
u = np.linspace(0,1,ncellu)
w = np.linspace(0,1,ncellw)

#bernstein basis poly
b = []
d = []

xBezier = np.zeros((ncellu, ncellw))
yBezier = np.zeros((ncellu, ncellw))
zBezier = np.zeros((ncellu, ncellw))

#Binomial coefficients

def Ni(n,i):
    return np.math.factorial(n)/(np.math.factorial(i) * np.math.factorial(n-i))

def Mj(m,j):
    return np.math.factorial(m)/(np.math.factorial(j) * np.math.factorial(m-j))

#bernstein basis poly

def J(n, i, u):
    return np.matrix(Ni(n, i)* (u ** i) * (1-u)**(n-i))

def K(m, j, w):
    return np.matrix(Mj(m, j)* (w ** j) * (1-w)**(m-j))


# main loop
for i in range(0, uPTs):
    for j in range(0, wPTs):
        b.append(J(n, i, u))
        d.append(K(m, j, w))

        Jt = J(n, i, u).T


        xBezier = Jt * K(m, j, w) * x[i, j] + xBezier
        yBezier = Jt * K(m, j, w) * y[i, j] + yBezier
        zBezier = Jt * K(m, j, w) * z[i, j] + zBezier

"""
#plot
plt.figure(1)
plt.subplot(121)
for line in b:
    plt.plot(u, line.T)
plt.subplot(122)
for line in d:
    plt.plot(w, line.T)
plt.show()
"""

fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
ax.plot_surface(xBezier, yBezier, zBezier)
ax.scatter(x,y,z, edgecolors='face')
plt.show()