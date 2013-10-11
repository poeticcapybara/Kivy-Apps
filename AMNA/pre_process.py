from pylab import *
import os

os.system('convert -quality 100 personen.pdf personen.jpg')
im = imread('personen.jpg')
y = (15.,2450.)
x = (295.,3220.)
ny = 3
nx = 6

photos = []
for j in range(ny):
    photo = im[x[0]:x[0]+(x[1]-x[0])*1.065/nx,y[0]+(y[1]-y[0])/ny*j:y[0]+(y[1]-y[0])/ny*(j+1),:]
    photos.append(photo)
x = (x[0]+(x[1]-x[0])*1.065/nx,x[1])
for j in range(ny):
    for i in range(nx-1):
        photo = im[x[0]+(x[1]-x[0])/(nx-1)*i:x[0]+(x[1]-x[0])/(nx-1)*(i+1),y[0]+(y[1]-y[0])/ny*j:y[0]+(y[1]-y[0])/ny*(j+1),:]
        photos.append(photo)


for i,photo in enumerate(photos):
    imsave('%.2d.jpg'%i,photo)
os.remove('personen.jpg')
