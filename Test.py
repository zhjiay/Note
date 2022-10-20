import numpy as np
import math

anchor_x = 1291
anchor_y = 2372
angle=0.1
valuex=np.array(39000)
valuey=np.array(2372)

pointx=1291
pointy=2372

nRotatex = (valuex-pointx)*math.cos(angle) - (valuey-pointy)*math.sin(angle) + pointx
nRotatey = (valuex-pointx)*math.sin(angle) + (valuey-pointy)*math.cos(angle) + pointy

print(nRotatex,nRotatey)