import cv2
import  numpy as np
imgz= cv2.imread("coke.jpg")
cavas = np.zeros((500,500,3),dtype="uint8")
cv2.rectangle(cavas,(100,150),(400,300),(255,255,255),-1)
cv2.imshow("..",cavas)
canny = cv2.Canny(cavas,125,175)
cv2.imshow("CAnny",canny)
contours_draw , heicrchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("no of contours",len(heicrchy))
cv2.drawContours(canny,contours_draw,0,(255,255,255),4)

cv2.imshow("cannyz",canny)
cnts =contours_draw
cnts = cnts[0]
x,y,w,h = cv2.boundingRect(cnts)
cv2.rectangle(cavas, (x, y), (x + w, y + h), (36,255,12), 5)
cv2.imshow("cavass",cavas)
f= cavas
#newimg = cv2.resize(imgz,(h,w),interpolation=cv2.INTER_CUBIC)
#newcavna= np.equal(newimg,dtype="uint8")
#cv2.imshow("newcava",newcavna)
#f= np.where(f==0 ,imgz,f)
#cv2.imshow("Mask2",f)

cv2.waitKey(0)


""""
#cnts = contours_draw
#cnts = cnts[0] if len(cnts) == 2 else cnts[1]
##    x,y,w,h = cv2.boundingRect(c)
 #   cv2.putText(cavas, str(w), (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
 #   cv2.rectangle(cavas, (x, y), (x + w, y + h), (36,255,12), 1)
cv2  .imshow("CAnva",cavas)
cv2.imshow("CAnva2",canny)
cv2.waitKey()

"""