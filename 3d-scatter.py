# Takes input from standard in. input should be a 
# number of lines where each line has the format
# 
# <DECIMAL NUMBER>, <DECIMAL NUMBER>, <DECIMAL NUMBER>
# 
# the three numbers will be interpreted as the x, y and z
# coordinates respectively of a point in 3d space. Each 
# line will be displayed as a point in a scatter plot.
# 
# Code is a modified version of https://matplotlib.org/stable/gallery/mplot3d/2dcollections3d.html#sphx-glr-gallery-mplot3d-2dcollections3d-py
# from the official matplotlib website.

from sys import stdin
import matplotlib.pyplot as plt

ax = plt.figure().add_subplot(projection='3d')


x = []
y = []
z = []
for line in stdin:
    line = line.split(",")
    x.append(float(line[0]))
    y.append(float(line[1]))
    z.append(float(line[2]))



ax.scatter(x, y, z, label='graph')

ax.legend()
#ax.set_xlim(0, 1)
#ax.set_ylim(0, 1)
#ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(elev=20., azim=-35, roll=0)

plt.show()

