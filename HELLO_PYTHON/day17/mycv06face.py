import cv2

img1 = cv2.imread('startup.png')

print("img1",img1)
cv2.imshow('img1', img1)


cv2.waitKey(0)
cv2.destroyAllWindows()