import cv2
import numpy as np

a = np.array([3,6,7,8,9,6,7,3,5,7])

b = np.divide(np.subtract(a, np.min(a)), np.max(a))
c = cv2.normalize(a, None, 0, max(b), cv2.NORM_MINMAX)
print(b)
print(c)
