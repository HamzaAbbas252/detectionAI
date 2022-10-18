import cv2
import numpy as np

img = cv2.imread("project1.jpg")
blankimg = np.zeros((img.shape[0],img.shape[1],3),dtype="uint8")
cv2.imshow("blank",blankimg)
cv2.imshow("Project1",img)
cv2.waitKey(0)
blur = img
newimg = blur
def missionblueScreen(img):
    # Convert BGR to HSV
    ad2 = cv2.imread("coke.jpg")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)


    ad2 = cv2.resize(ad2, (828,413),interpolation=cv2.INTER_AREA)

    f = newimg - res
    f = np.where(f == 0, ad2, f)
    # cv2.imshow("Mask",mask)
    cv2.imshow("Mask2", f)

    cv2.imshow('frame',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    return f

def missionGreenScreen(img):
    image = cv2.imread("pepsi.jpg")
    ad2 = cv2.imread("coke.jpg")


    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_range = np.array([40, 45, 70])
    upper_range = np.array([70, 255, 255])
    mask = cv2.inRange(hsv, lower_range, upper_range)

    res = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("image2",res)
    cv2.imshow("image",img)
    #image = cv2.resize(image, (828, 413), interpolation = cv2.INTER_AREA)
    ad2 =cv2.resize(ad2, (828, 413), interpolation = cv2.INTER_AREA)
    f = img - res
    cv2.imshow("ff",f)
    f = np.where(f == 0, ad2, f)
    # cv2.imshow("Mask",mask)
    newimg = f
    #cv2.imshow("Mask2", f)
    return f



#greeneffect = missionGreenScreen(img)
#cv2.imshow("FINAL",greeneffect)


SEMIeffect=missionblueScreen(blur)
cv2.imshow("SEMI",SEMIeffect)

greeneffect = missionGreenScreen(SEMIeffect)
cv2.imshow("FINAL",greeneffect)


cv2.waitKey(0)