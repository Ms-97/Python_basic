
import cv2
import random

labels = ["곽금규m",
          "곽동석m",
          "기민혁m",
          "김미정m",
          "김민수m",
          
          "김성겸m",
          "김유미m",
          "박건영m",
          "박성우m",
          "박수빈m",
          
          "박수현m",
          "박지영m",
          "심재린m",
          "양형주m",
          "윤재열m",
          
          "이상권m",
          "이혜림m",
          "장재훈m",
          "조정현m",
          "채희진m",
          
          "최재혁m",
          "한재웅m",
          "한태훈m"
          ]

dirs = [
        "00",
        "01",
        "02",
        "03",
        "04",
        
        "05",
        "06",
        "07",
        "08",
        "09",
        
        "10",
        "11",
        "12",
        "13",
        "14",
        
        "15",
        "16",
        "17",
        "18",
        "19",
        
        "20",
        "21",
        "22"
      ]

reverses = [
        True,
        True,
        True,
        False,
        True,
        
        True,
        False,
        True,
        False,
        True,
        
        True,
        False,
        True,
        True,
        True,
        
        True,
        True,
        True,
        True,
        False,
        
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
                
            resize_img = cv2.resize(img_save, (32, 32))    
                
            cv2.imwrite("{}/{}/{}.png".format(path,dir,count), resize_img)    
            
            count += 1
            # if count > 5:
            #     break
        
        vidcap.release()
        
    except:
        pass    

for i in range(23):
    saveImage(labels[i],dirs[i],reverses[i])




