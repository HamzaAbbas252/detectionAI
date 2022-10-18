import cv2
import numpy as np


ad1= cv2.imread("pepsi.jpg")
ad2 = cv2.imread("coke.jpg")
img= cv2.imread("p3.jpg")

def greencolordetectionCnn(frame):
    img = frame

    # blankimg = np.zeros((img.shape[0],img.shape[1],3),dtype="uint8")

    image = cv2.imread("pepsi.jpg")
    ad2 = cv2.imread("coke.jpg")
    blankedimg = cv2.resize(ad2, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_AREA)
    blankedimg[:] = 0, 0, 0

    image = cv2.resize(image, (240, 170), 3)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_range = np.array([45, 45, 70])
    upper_range = np.array([70, 255, 255])
    mask = cv2.inRange(hsv, lower_range, upper_range)

    cv2.imshow("mask", mask)
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(len(cnts))
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        if (x + w - x) > 40 | (y + h - y) > 3:
            retAdd = ad2
            retAdd = cv2.resize(ad2, (w, h))

            # cv2.rectangle(blankedimg, (x, y), (x + w, y + h), (36, 255, 12), 2)

            blankedimg[y:y + h, x:x + w] = retAdd
            # cv2.imshow("blankedeeee",blankedimg)

            # cv2.rectangle(img, (x, y), (x + w, y + h), (36, 255, 12), 2)

    cv2.imshow("mask", img)

    res = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("image2", res)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    f = img - res
    f = np.where(f == 0, blankedimg, f)
    cv2.imshow("Mask2", f)
    return f

def bluecolordetectionCnn(frame):
        img = frame

        # blankimg = np.zeros((img.shape[0],img.shape[1],3),dtype="uint8")

        ad1d = cv2.imread("pepsi.jpg")
        image = cv2.imread("coke.jpg")
        \
        blankedimg = cv2.resize(ad1, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_AREA)
        blankedimg[:] = 0, 0, 0

        image = cv2.resize(image, (240, 170), 3)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_range = np.array([110, 50, 50])
        upper_range = np.array([130, 255, 255])

        mask = cv2.inRange(hsv, lower_range, upper_range)

        cv2.imshow("mask", mask)
        cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print(len(cnts))
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            if (x + w - x) > 40 | (y + h - y) > 3:
                retAdd = ad1
                retAdd = cv2.resize(ad1, (w, h))

                # cv2.rectangle(blankedimg, (x, y), (x + w, y + h), (36, 255, 12), 2)

                blankedimg[y:y + h, x:x + w] = retAdd
                # cv2.imshow("blankedeeee",blankedimg)

                # cv2.rectangle(img, (x, y), (x + w, y + h), (36, 255, 12), 2)

        cv2.imshow("mask", img)

        res = cv2.bitwise_and(img, img, mask=mask)

        cv2.imshow("image2", res)
        cv2.imshow("image", img)
        cv2.waitKey(0)
        f = img - res
        f = np.where(f == 0, blankedimg, f)
        cv2.imshow("Mask2", f)
        return f
semicut= greencolordetectionCnn(img)
cv2.imshow("Semi",semicut)
cv2.waitKey(0)
FINAL = bluecolordetectionCnn(semicut)
cv2.imshow("Final",FINAL)


cv2.waitKey()
cv2.destroyAllWindows()
