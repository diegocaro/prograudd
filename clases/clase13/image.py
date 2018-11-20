from skimage import io
from skimage.color import rgb2gray

import numpy as np
import matplotlib.pyplot as plt

image = io.imread('mandrill.jpg')
print('type(image):', type(image))
print('image.shape', image.shape)

bw = rgb2gray(image)
print('type(bw):', type(bw))
print('bw.shape', bw.shape)

plt.figure()
plt.imshow(image)

plt.figure()
plt.imshow(bw, cmap=plt.cm.gray)

plt.figure()
plt.imshow(bw.T, cmap=plt.cm.gray)

plt.show()