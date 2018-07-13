import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui
from fractions import gcd


f = easygui.fileopenbox()
I = cv2.imread(f)

b,g,r = I[1,1]


lowerR = (b-20, g-20, r-20)
upperR = (b+45, g+45, r+45)


B = cv2.inRange(I, lowerR, upperR)


B=255-B

shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
nm = cv2.morphologyEx(B,cv2.MORPH_OPEN, shape)
B=nm

B, contours,_ = cv2.findContours(B, mode = cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)

contours = sorted(contours, key = cv2.contourArea, reverse=True)

I = cv2.drawContours(I,contours, contourIdx=-1, color=(0,0,255), thickness=3)

ellipse = cv2.fitEllipse(contours[0])
(x, y), (MA, ma), angle = cv2.fitEllipse(contours[0])
cv2.ellipse(I, ellipse, color=(0,255,0), thickness=3)

major = max(ma,MA)
minor=min(ma,MA)

major = round(major)
minor = round(minor)

major = int (major)
minor = int (minor)

GCD = gcd(major,minor)

major = major/GCD
minor = minor/GCD


I = I*0

I = cv2.resize(I, dsize=(400, 100))

message = "Aspect ratio is "+str(major)+":"+str(minor)

cv2.putText(I, message, (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)

cv2.imshow("Message: Result", I)
key = cv2.waitKey(0)