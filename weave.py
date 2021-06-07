import random
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

### CHANGE THIS ###
current_folder = 'Git/Fourier-Visualizer/Images/' # Change depending on your local setup
photos = ['bee.jpg', 'flowers.jpg', 'trees.jpg', 'forest.jpg', 'nebula.jpg', 'water.jpg', 'clouds.jpg', 'mountain.jpg', 'city.jpg', 'buildings.jpg']

A, B = (random.randint(0, len(photos)-1), random.randint(0, len(photos)-1))

# Good ones: (1, 4), (2, 6), (3, 5), (4, 5), (4, 6)


# Things to mess with
#A, B = (0, 1)
block_size = 1

img = Image.open(current_folder + photos[A])
img2 = Image.open(current_folder + photos[B])
img_array = np.array(img)
img2_array = np.array(img2)

n, m, channels = img_array.shape

for i in range(int(n/block_size)):
    for j in range(int(m/block_size)):
        if (i + j) % 2 == 0:
            img_array[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size, :] = np.zeros((block_size, block_size, 3)) #[np.zeros(block_size), np.zeros(block_size), [0, 0, 0]]
        else:
            img2_array[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size, :] = np.zeros((block_size, block_size, 3)) #[np.zeros(block_size), np.zeros(block_size), [0, 0, 0]]

plt.imshow(img_array + img2_array)
plt.show()
