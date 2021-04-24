
import cv2
import os

srcImg = cv2.imread("italy.jpg")
dstImg = cv2.xphoto.oilPainting(srcImg, 3, 1)

os.makedirs('result', exist_ok=True)

print("write processed image")
cv2.imwrite("result/italy-oilPainted.jpg",dstImg)


