import cv2

import matplotlib.image as img
import matplotlib.pyplot as plt

image1 = img.imread("1st.jpg")
image1_cv = cv2.imread("1st.jpg")


plt.figure()
plt.imshow(image1_cv)
plt.show()