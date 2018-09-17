import numpy as np
import pylab as pl

with open("../data/xy.dat" ,"r") as infile:
    x=[]
    y=[]
    for line in infile:
        x_,y_ = [float(w) for w in line.split()]
        x.append(x_)
        y.append(y_)

infile.close()

x=np.array(x)
y=np.array(y)

pl.plot(x,y)
pl.show()
