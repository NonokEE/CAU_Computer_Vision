import cv2
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

### Click and get patch for 1st.jpg

coord1 = []
coord2 = []

def getCoord_1(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coord1.append((y,x))
        print(x, y)

def getCoord_2(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coord2.append((x,y))
        print(x, y)

image1_cv = cv2.imread("1st.jpg")

cv2.namedWindow("1st", cv2.WINDOW_NORMAL)
cv2.resizeWindow("1st", 1000, 800)
cv2.setMouseCallback("1st", getCoord_1)

cv2.imshow("1st", image1_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(coord1)



patch1 = [image1_cv[coord1[i][0]-4:coord1[i][0]+4, coord1[i][1]-4:coord1[i][1]+4] for i in range(len(coord1))]

for i in range(len(patch1)):
    wname = "1st_" + str(i)

    cv2.namedWindow(wname, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(wname, 500, 500)
    cv2.setMouseCallback(wname, getCoord_1)

    cv2.imshow(wname, patch1[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows()