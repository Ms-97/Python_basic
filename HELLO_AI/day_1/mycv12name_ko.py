import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2

img = cv2.imread('startup.png')

fontpath = "HMFMPYUN.TTF"
font = ImageFont.truetype(fontpath, 50)
img_pil = Image.fromarray(img)
idraw = ImageDraw.Draw(img_pil)
idraw.text((480, 160),  "수지", font=font, fill=(255,50,255,0))


img = np.array(img_pil)
cv2.imshow("res", img)


cv2.waitKey()
cv2.destroyAllWindows()