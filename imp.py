import cv2

srcImg = cv2.imread("italy.jpg")
dstImg = cv2.xphoto.oilPainting(srcImg, 3, 1)
cv2.imwrite("italy-oilPainted.jpg",dstImg)
