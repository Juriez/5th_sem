import numpy as np
import imageio
import matplotlib.pyplot as plt

input_img = "AMla.jpeg"
output_img = "final4.jpeg"
fp = open('output.txt', "r")   

trained_value = np.zeros(shape=(256,256,256))
new_img = np.empty(shape=(256, 256, 256), dtype=int).fill(0)
new_img = imageio.v2.imread(input_img)

#fp = open('output2.txt', 'r')

for i in range(256):
    for j in range(256):
        for k in range(256):
            val = fp.readline()
            trained_value[i][j][k] = float(val) 


height, width, _ = new_img.shape
T = 0.4

for x in range(height):
    for y in range(width):
        red = new_img[x, y, 0]
        green = new_img[x, y, 1]
        blue = new_img[x, y, 2]

        if (trained_value[red,green,blue] <= T):
            # image without skin is covered with WHITE
            new_img[x, y, 0] = 255
            new_img[x, y, 1] = 255
            new_img[x, y, 2] = 255

plt.imsave(output_img, new_img)
print("Done...")
