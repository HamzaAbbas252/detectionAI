from PIL import Image
import cv2
import numpy as np
# Opening the primary image (used in background)
img1 = Image.open(r"C:\Users\HP\Downloads\depositphotos_13280842-stock-photo-tv-screen-white.jpg")
v2= cv2.imread("coke.jpg")
v3= np.zeros((500,500,3),dtype="uint8")

cv2.imshow("blank",v3)
cv2.imshow("v2z",v2)
v2.paste(v3.resize(500,500),(0,0))
cv2.imshow("blank",v3)
cv2.imshow("v2z",v2)


cv2.waitKey(0)
# Opening the secondary image (overlay image)
img2 = Image.open(r"C:\Users\HP\Downloads\ca722833e2d1f37eb75e130ffb438082.jpg").convert("RGBA")

# Pasting img2 image on top of img1
# starting at coordinates (0, 0)
#img1.paste(img2.resize((500,550)) , (0, 0,), mask=img2)
v2.paste(img2.resize((500,500)),(0,0))
cv2.imshow("v2",v2)
# Displaying the image
img1.show()