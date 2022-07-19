import cv2

# haarcascade 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# 이미지 불러오기
img = cv2.imread('startup.png')
img1 = cv2.imread('Pengsu.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 얼굴 찾기
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    img[y: y + h, x: x + w] = cv2.resize(img1, (w, h), interpolation=cv2.INTER_NEAREST)

    
# 영상 출력
cv2.imshow('image', img)

key = cv2.waitKey(0)
cv2.destroyAllWindows()