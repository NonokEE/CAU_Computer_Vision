import numpy as np
import cv2

def cv2_imshow(name: str, src):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 800, 800)
    cv2.moveWindow(name, 500, 100)

    cv2.imshow(name, src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

coord1 = []
coord2 = []
rec_size = 50

def getCoord_1(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coord1.append((y,x))
        print(x, y)

def getCoord_2(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coord2.append((y,x))
        print(x, y)

### 사각형 그리기

def rectangle_patch(src, coord):
    colors = [(0,0,255), (255,0,0), (0,255,0), (255,255,255)]
    t = src.copy()
    for i in range(len(coord)):
        t = cv2.rectangle(t, [coord[i][1]-rec_size, coord[i][0]-rec_size], [coord[i][1]+rec_size, coord[i][0]+rec_size], colors[i], 10)
    return t

###

image1 = cv2.imread("1st_shifted.jpg")

cv2.namedWindow("1st_shifted", cv2.WINDOW_NORMAL)
cv2.resizeWindow("1st_shifted", 800, 800)
cv2.moveWindow("1st_shifted", 500, 100)
cv2.setMouseCallback("1st_shifted", getCoord_1)

cv2.imshow("1st_shifted", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

image1_rec = rectangle_patch(image1, coord1)

##

image2 = cv2.imread("2nd.jpg")

cv2.namedWindow("2nd", cv2.WINDOW_NORMAL)
cv2.resizeWindow("2nd", 1000, 800)
cv2.moveWindow("2nd", 500, 100)
cv2.setMouseCallback("2nd", getCoord_2)

cv2.imshow("2nd", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

image2_rec = rectangle_patch(image2, coord1)

##

hap = np.concatenate([image1_rec, image2_rec], axis = 1)
cv2_imshow("test", hap)


hap = np.concatenate([image1, image2], axis = 1)
cv2_imshow("test", hap)