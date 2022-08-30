
import cv2
import random

labels = ["곽금규",
          "곽동석",
          "김민수",
          "심재린",
          "조정현"
          ]

dirs = [
        "00",
        "01",
        "02",
        "03",
        "04"
      ]

reverses = [
        True,
        True,
        True,
        True,
        True
      ]


def saveImage(label,dir,reverse):
    try:
        vidcap = cv2.VideoCapture('movie/{}.mp4'.format(label))
        
        count = 0
        while(vidcap.isOpened()):
            ret, src = vidcap.read()
        
            height, width, channel = src.shape
            matrix = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
            dst = cv2.warpAffine(src, matrix, (width, height))
        
            print(dst.shape)
            img_save = None
            if reverse:
                img_save = dst
            else:
                img_save = src
                
            path = "" 
            if random.random() > 0.16:
                path = "train_image"  
            else:
                path = "test_image"  
                
            cascade_file = 'face.xml'
            cascade = cv2.CascadeClassifier(cascade_file)
            gray = cv2.cvtColor(img_save, cv2.COLOR_BGR2GRAY) 
            face_list = cascade.detectMultiScale(gray, minSize = (50,50)) 
            
            for idx,(x, y, w, h) in enumerate(face_list):
                cropped = img_save[y:y+h, x:x+w]
                resize_img = cv2.resize(cropped, (128, 128))        
                cv2.imwrite("{}/{}/{}.jpg".format(path,dir,count), resize_img)   
                break
                
            count += 1
            # if count > 5:
            #     break
        
        vidcap.release()
        
    except:
        pass    

for i in range(5):
    saveImage(labels[i],dirs[i],reverses[i])




