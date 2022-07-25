import cv2
import numpy as np

img = cv2.imread('startup.png')
res = cv2.resize(img, dsize=(500, 300), interpolation=cv2.INTER_CUBIC)

cv2.imshow('startup.png', res)
cv2.imwrite('startup.jpg', res) 

cv2.waitKey(0)
cv2.destroyAllWindows()