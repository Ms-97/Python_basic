import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
from day30face5.cnn_load import Load

# labels = ["곽금규",
#           "곽동석",
#           "기민혁",
#           "김미정",
#           "김민수",
#
#           "김성겸",
#           "김유미",
#           "박건영",
#           "박성우",
#           "박수빈",
#
#           "박수현",
#           "박지영",
#           "심재린",
#           "양형주",
#           "윤재열",
#
#           "이상권",
#           "이혜림",
#           "장재훈",
#           "조정현",
#           "채희진",
#
#           "최재혁",
#           "한재웅",
#           "한태훈"
#           ]

labels = ["곽금규",
          "곽동석",
          "김민수",
          "심재린",
          "조정현"
          ]
#
# dirs = [
#         "00",
#         "01",
#         "02",
#         "03",
#         "04"
#       ]

cascade_filename = 'face.xml'
cascade = cv2.CascadeClassifier(cascade_filename)

cnn = Load();
# train_images = np.load("train_image.npy")
# train_labels = np.load("train_label.npy")

# 자른 이미지 넣기


def imgDetector(img, cascade):

    # 영상 압축
    img = cv2.resize(img, dsize=None, fx=1.0, fy=1.0)
    # 그레이 스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    # cascade 얼굴 탐지 알고리즘 
    results = cascade.detectMultiScale(gray,  # 입력 이미지
                                       scaleFactor=1.2,  # 이미지 피라미드 스케일 factor
                                       minNeighbors=5,  # 인접 객체 최소 거리 픽셀
                                       minSize=(2, 2)  # 탐지 객체 최소 크기
                                       )        
    
    for i, box in enumerate(results):
        
        # cv2.imwrite("train_images/{}.png".format(i), box)   
        
        x, y, w, h = box
        
        # n = 80
        # n2 = 160
        # x2 = x - n
        # y2 = y - n * 2
        # w2 = w + n2
        # h2 = h + n2 * 2
        
        # 자른 이미지 크롭
        # cropped = img[y2:y2 + h2, x2:x2 + w2]
        cropped = img[y:y + h, x:x + w]
        
        # 크롭 이미지 저장
        cv2.imwrite("test_image/{}.jpg".format(i), cropped)
        
        # 크롭이미지 불러오기
        img_save = cv2.imread("test_image/{}.jpg".format(i))
        
        # 크롭이미지 리사이즈
        resize_img = cv2.resize(img_save, (128, 128))
        
        # 리사이즈 이미지 불러오기
        cv2.imwrite("train_image/{}.jpg".format(i), resize_img)
        
        # npy파일 만들기
        train_image = np.empty((0, 0, 0), np.uint8)
        train_image = np.append(train_image, cv2.imread('train_image/' + '{}.jpg'.format(i)))
        train_image = train_image.reshape((1, 128, 128, 3))
        np.save("train_image.npy", train_image)
        train_images_npy = np.load("train_image.npy")
        # npy파일 불러오기
        num = cnn.getNum(train_images_npy);
        print(num)
        
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), thickness=1)
        
        color_coverted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(color_coverted)
        
        draw = ImageDraw.Draw(img_pil)
        # 인덱스 변경하면 끝
        draw.text((x, y - 30), labels[num], font=ImageFont.truetype("./HMKMM.TTF", 24), fill=(255, 255, 255))

        numpy_img = np.array(img_pil)
        img = cv2.cvtColor(numpy_img, cv2.COLOR_RGB2BGR)
    # 사진 출력
     
    cv2.imshow('facenet', img)  
    cv2.waitKey(10000)


img = cv2.imread('4.png')
resize_img = cv2.resize(img, (4000, 3000))
# print("img", type(resize_img))

imgDetector(resize_img, cascade)

cv2.waitKey(0)
cv2.destroyAllWindows()
