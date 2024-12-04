import numpy as np 
import matplotlib.pyplot as plt 
import imageio

img1 = np.array(imageio.imread('flag_7ae18c704272532658c10b5faad06d74.png'),dtype = np.int64) 
img2 = np.array(imageio.imread('lemur_ed66878c338e662d3473f0d98eedbd0d.png'),dtype = np.int64)
plt.imshow(img1 ^ img2)
plt.show()

