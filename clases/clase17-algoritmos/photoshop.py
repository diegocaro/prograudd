from skimage import io
from skimage.color import rgb2gray

import numpy as np
import matplotlib.pyplot as plt
# images from
# http://dsphotographic.com/2006/12/how-to-remove-tourists-from-your-photos/
files = ['02-fewer-people.jpg','04-second-image.jpg','05-third-image.jpg']

images = []
for f in files:
    images.append(io.imread(f))

x,y,z=images[0].shape
m = np.zeros(shape=(x,y,z),dtype=np.int)
for i in range(x):
    for j in range(y):
        l = []
        for k in range(len(files)):
            l.append(images[k][i,j])
        m[i,j] = np.median(np.array(l),axis=0).astype(np.int)
    
plt.figure()
plt.imshow(m)
plt.show()