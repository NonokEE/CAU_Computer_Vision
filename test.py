import cv2
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

coord1 = []
coord2 = []

def getCoord_1(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coord1.append((y,x))
        print(x, y)

image1_cv = cv2.imread("1st.jpg")

cv2.namedWindow("1st", cv2.WINDOW_NORMAL)
cv2.resizeWindow("1st", 1000, 800)
cv2.setMouseCallback("1st", getCoord_1)

cv2.imshow("1st", image1_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow("1st_1", cv2.WINDOW_NORMAL)
cv2.resizeWindow("1st_1", 500, 500)
cv2.setMouseCallback("1st_1", getCoord_1)

cv2.imshow("1st_1", image1_cv[coord1[0][0]-10:coord1[0][0]+10, coord1[0][1]-10:coord1[0][1]+10])
cv2.waitKey(0)
cv2.destroyAllWindows()