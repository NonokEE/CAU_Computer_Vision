import numpy as np
import cv2
import matplotlib.pyplot as plt

hist_bin = 32

def norm_gradient(src):
    
    x_forward = np.concatenate([src[:, 1:], src[:, -1:]], axis = 1)
    x_backward = np.concatenate([src[:, :1], src[:, :-1]], axis = 1)
    Dx = np.subtract(x_forward, x_backward)/2

    y_forward = np.concatenate([src[1:, :], src[-1:, :]])
    y_backward = np.concatenate([src[:1, :], src[:-1, :]])
    Dy = np.subtract(y_forward, y_backward)/2

    norm_gradient = np.sqrt(np.add(np.square(Dx), np.square(Dy)))
    
    return norm_gradient

def gradient_histogram_cv(src_list):
    hist_list = []

    for i in range(len(src_list)):
        print(f"- {i+1}th -")
        src = cv2.cvtColor(src_list[i], cv2.COLOR_BGR2GRAY)
        grd = norm_gradient(src)
        hist = cv2.calcHist([grd], [0], None, [int(256/hist_bin)], [0, 360])
        hist_list.append(hist)
        plt.plot(hist)
        plt.show()