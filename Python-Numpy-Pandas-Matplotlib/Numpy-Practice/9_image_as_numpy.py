import numpy as np # y = mx + c
from PIL import Image


# Load image
img = Image.open('zuzu.jpg')
img_array = np.array(img)

print(img_array.shape)  # (height, width, 3)
print(img_array.dtype)  # uint8
print(img_array[0, 0])   # RGB values of the first pixel
print(img_array[0, 0, 0]) # Red channel value of the first pixel
print(img_array[0, 0, 1]) # Green channel value of the first pixel
print(img_array[0, 0, 2]) # Blue channel value of the first pixel
print(img_array[0, 0, 0] / 255.0) # Normalized Red channel value
print(img_array[0, 0, 1] / 255.0) # Normalized Green channel value      
print(img_array[0, 0, 2] / 255.0) # Normalized Blue channel value
