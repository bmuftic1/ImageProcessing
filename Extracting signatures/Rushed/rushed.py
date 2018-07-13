#Student: Belma Muftic

#Student number: D17127216

#Assignment number: 1.2

#Assignment objective: Find and crop the signature


#importing needed packages
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui


#opening the wanted image
f = easygui.fileopenbox()
I = cv2.imread(f)

#set the lower and upper range to find the paper (i.e. bright pixels)
lowerR = (200,200,200)
upperR = (255,255,255)

#get the binary image in the specified range
B = cv2.inRange(I,lowerR, upperR)

#due to the bright keyboard letters, erosion is needed so that only the paper would be left in the binary image
shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
nm = cv2.erode(B, shape)
B=nm

#find the sum values of each row
rowsSum=B.sum(axis=1)

#get the height and width of the image
h,w,d=I.shape

#initialize values
upperMostPixel=0
leftMost = 0
rightMost=w

#find the first pixel (from above) that is not black that indicates the top of the paper
for x in range (0, len(rowsSum)):
	if (rowsSum[x]!=0):
		upperMostPixel=x+50
		break

#find the first pixel (from left) that is not black that indicates the left side of the paper
for x in range(0,w):
	if (B[upperMostPixel,x]==255):
		leftMost=x
		break
#find the first pixel (from right) that is not black that indicates the right side of the paper
for x in range(w-1,0,-1):
	if(B[h-1, x]==255):
		rightMost=x
		break

#crop the paper
Crop = I[upperMostPixel:h, leftMost:rightMost]

#turn cropped image to greyscale
G = cv2.cvtColor(Crop, cv2.COLOR_BGR2GRAY)

#find the binary image with adaptive threshold
B = cv2.adaptiveThreshold(G, maxValue = 255, adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType = cv2.THRESH_BINARY, blockSize = 21, C = 30)

#invert the binary image
B = 255-B

#closing in order to "clean out" the image
shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
nm = cv2.morphologyEx(B,cv2.MORPH_CLOSE, shape)
B=nm

#find ROI from the Crop image according to mask B
ROI = cv2.bitwise_and(Crop, Crop, mask=B)

#get the height and width of the ROI
h,w,d = ROI.shape

#find the sum values of each row and column
#IDEA: the row/column that has a non-black pixel will have a sum that is greater than zero, thus, it is the first/last pixel to take for the cropping
rowsSum=B.sum(axis=0)
columnsSum=B.sum(axis=1)

#initialize values
upperMostPixel=1
lowerMostPixel=len(rowsSum)-1
leftMostPixel=1
rightMostPixel=len(columnsSum)-1

#find upper-most pixel by searching for the first pixel (from above) that has a row sum that is different from zero
for x in range (1, len(rowsSum)):
	if (rowsSum[x]!=0):
		upperMostPixel=x-1
		break

#find lower-most pixel by searching for the first pixel (from below) that has a row sum that is different from zero
#condition x!=len(rowsSum)-1 is there in case it tries to set the value of the found pixel to a value greater than the size of the image
for x in range (len(rowsSum)-1, 0, -1):
	if (rowsSum[x]!=0 & x!=len(rowsSum)-1):
		lowerMostPixel=x+1
		break

#find left-most pixel by searching for the first pixel (from left) that has a column sum that is different from zero
for x in range (1, len(columnsSum)):
	if (columnsSum[x]!=0):
		leftMostPixel=x-1
		break

#find right-most pixel by searching for the first pixel (from right) that has a column sum that is different from zero
#condition x!=len(columnsSum)-1 is there in case it tries to set the value of the found pixel to a value greater than the size of the image
for x in range (len(columnsSum)-1, 0, -1):
	if (columnsSum[x]!=0 & x!=len(columnsSum)-1):
		rightMostPixel=x+1
		break


#turn the black pixels to white
h,w,d = ROI.shape
for x in range (0, h):
	for y in range (0, w):
		#test if pixel is black
		if (ROI[x,y][0]==0 & ROI[x,y][1]==0 & ROI[x,y][2]==0):
			#if it is, turn it into white
			ROI[x,y]=(255,255,255)


#crop signature from original image
Ci = ROI[leftMostPixel:rightMostPixel, upperMostPixel:lowerMostPixel]

#show final image
cv2.imshow("signature", Ci)
key = cv2.waitKey(0)
