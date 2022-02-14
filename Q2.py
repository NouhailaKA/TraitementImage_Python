from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import cv2

# lien
image = Image.open('ImageTest.jpg')
imageTable = np.asarray(image)

plt.subplot(211)
plt.imshow(image)

color = ('r', 'g', 'b')
for i, col in enumerate(color):
    histograme = cv2.calcHist([imageTable], [i], None, [255], [0, 255])
    plt.subplot(212)
    plt.plot(histograme, color=col)
    plt.xlim([0, 255])
plt.show()