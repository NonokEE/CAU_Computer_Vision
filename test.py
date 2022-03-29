import cv2
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

dir_del = None
clicked_points = []

def getCoord(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


image1_cv = cv2.imread("1st.jpg")

cv2.namedWindow("1st", cv2.WINDOW_NORMAL)
cv2.resizeWindow("1st", 1000, 800)
cv2.setMouseCallback("1st", getCoord)

cv2.imshow("1st", image1_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(clicked_points)