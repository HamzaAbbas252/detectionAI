import cv2
import numpy as np

""""
img1=cv2.imread("F1 (2).jpg")
img2=cv2.imread("F1 (3).jpg")
"""
"""
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
res = cv2.bitwise_or(img1,img2)
cv2.imshow("Res",res)
"""
import cv2
import numpy as np

ad= cv2.imread("coke.jpg",)
ad = cv2.resize(ad,(1500,50),interpolation=cv2.INTER_AREA)
cv2.imshow("ads",ad)
cv2.waitKey(0)