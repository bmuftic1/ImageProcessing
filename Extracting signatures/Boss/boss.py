#Student: Belma Muftic

#Student number: D17127216

#Assignment number: 1.1

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


#convert image to greyscale
G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

#equalize the greyscale image
H=cv2.equalizeHist(G)


#find the binary image of the equalized greyscale
B = cv2.adaptiveThreshold(H, maxValue = 255, adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType = cv2.THRESH_BINARY, blockSize = 21, C = 35)

#invert the binary image
B = 255-B


#find the region of interest
ROI = cv2.bitwise_and(I,I, mask=B)

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