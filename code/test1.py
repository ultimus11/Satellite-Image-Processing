import imageio
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline

# load the image
pic = imageio.imread('satimg.jpg')
plt.figure(figsize = (10,10))
plt.imshow(pic)
plt.show()

print(f'Shape of the image {pic.shape}')
print(f'hieght {pic.shape[0]} pixels')
print(f'width {pic.shape[1]} pixels')

# Only Red Pixel value , higher than 180
pic = imageio.imread('satimg.jpg')
red_mask = pic[:, :, 0] < 180

pic[red_mask] = 0
plt.figure(figsize=(15,15))
plt.imshow(pic)
plt.show()
imageio.imwrite("red.jpg",pic)
print("red")

# Only Green Pixel value , higher than 180
pic = imageio.imread('satimg.jpg')
green_mask = pic[:, :, 1] < 180


pic[green_mask] = 0
plt.figure(figsize=(15,15))
plt.imshow(pic)
plt.show()
imageio.imwrite("green.jpg",pic)

print("green")
# Only Blue Pixel value , higher than 180
pic = imageio.imread('satimg.jpg')
blue_mask = pic[:, :, 2] < 180

pic[blue_mask] = 0
plt.figure(figsize=(15,15))
plt.imshow(pic)
plt.show()
imageio.imwrite("blue.jpg",pic)

print("blue")
# Composite mask using logical_and
pic = imageio.imread('satimg.jpg')
final_mask = np.logical_and(red_mask, green_mask, blue_mask)
pic[final_mask] = 40
plt.figure(figsize=(15,15))
plt.imshow(pic)
plt.show()
imageio.imwrite("composite.jpg",pic)

print("composite")