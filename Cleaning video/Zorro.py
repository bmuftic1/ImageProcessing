#Student: Belma Muftic

#Student number: D17127216

#Assignment number: 2 

#Assignment objective: Clean out the Zorro video

#
#       STEP-BY-STEP
#			(sorry in advance for the length of it)
#
#
# 1.  import needed packages
# 		1.1  please find the comment MAIN, since the step-by-step will start there
#		1.2  the division of frames into scenes is given below the PERFORMANCE section
#
# 2.  call function grabFrames() which will convert the video into a sequence of images in the folder 'frames'; this is needed for further processing
#	 (more specific, for calculating the difference between the frames)
#
# 3. SCENE 1: 
#		3.1  The first (aka 0-th) frame needs to be processed separately, since it does not have a predecessor, so we call the independentFrame(i)
#				3.1.1  Read in the i-th frame
#				3.1.2  Call the noJitter(I) function, which returns the denoised image I
#				3.1.3  Call the saveFrame(i,I) function, which saves the i-th frame in the folder 'filtered'
#
#		3.2  Call the scene1(i, previous) function, where previous is the (i-1)-th frame
#				3.2.1  Read in the current (i-th) frame
#				3.2.2  Find the absolute difference between the two images; this will show where the blips are, as they will have high absolute difference values due to a sudden change of color
#				3.2.3  Get the width and the height of the image
#				3.2.4  Find the areas with a big color change (where the values of the channels is greater than [60,60,60])
#				3.2.5  Once found, replace them and the surrounding pixels of picture i with the values of those pixels of picture (i-1); the surrounding pixels need to be replaced in order to create a more clear image
#				3.2.5  Return the modified i-th picture
#
#		3.3  Make the acquired, modified picture the previous one (since the modified value needs to be compared to the next image)
#	
#		3.4  Call the noJitter(I) function, which returns the denoised image I
#
#		3.5  Call the saveFrame(i,I) function, which saves the i-th frame in the folder 'filtered'
#
#		3.6  Repeat for all other frames steps 3.2 - 3.5
#
# 4.  Call independentFrame(i) for frames 37 and 38, since they have scene-overlapping
#
# 5.  SCENE 2:
#		5.1  Call the scene2(i) function
#				5.1.1  Read in the i-th image
#				5.1.2  i have no idea why i did what i did
#
#
#		5.2  In case the frame number is 87, call function specialScene2()
#				5.2.1  Read in the 86-th and 87-th frame
#				5.2.2  Find the absolute difference between the two images; this will show where the blips are, as they will have high absolute difference values due to a sudden change of color
#				5.2.3  Get the width and the height of the image
#				5.2.4  Find the areas with a big color change (where the values of the channels is greater than [120,120,120])
#				5.2.5  Once found, replace them and the surrounding pixels of picture i with the values of those pixels of picture (i-1); the surrounding pixels need to be replaced in order to create a more clear image
#				5.2.5  Call the noJitter(I) function, which returns the denoised image I
#				5.2.6  Call the saveFrame(i,I) function, which saves the i-th frame in the folder 'filtered'
#				5.2.7  Read in the 88-th frame
#				5.2.8  Repeat steps 5.2.2 - 5.2.6 for frames 87 and 88 (where the 87th frame is the image that has the replaced values, but is still jittered)
#				5.2.9  Return acquired image
#				
#		5.3  In case the frame is 87, increment value of i (since the specialScene2() function has processed one more frame), and continue to the next iteration
#
#		5.4  In case the frame is not 87, call the noJitter(I) function, which returns the denoised image I
#
#		5.5  In case the frame is not 87, call the saveFrame(i,I) function, which saves the i-th frame in the folder 'filtered'
#
# 6.  Call independentFrame(i) for frames 90 and 91, since they have scene-overlapping  
#
# 7.  SCENE 3:
#		7.1  Call independentFrame(i) for frame 92, and save the returned value
#		7.2  Call the createBinaryScene3and5(I) function, where I is the image returned in the previous step
#				3.2.1  Make a copy of the image
#				3.2.2  Turn the image to grayscale (in order to make a binary image)
#				3.2.3  Draw a green and a red line, which represent the area in which the man in the frames is moving, so that we exclude him from further processing
#				3.2.4  Get the height and width of the image
#				3.2.5  Make a black image by multiplying the grayscale with 0
#				3.2.6  Turn the area between the two lines to white, as well as the lines
#				3.2.7  Return the negative binary image
#		7.3  Find the ROI of the image from 3.1 with the binary mask from 3.2
#		7.4  Call the scene3and5(i, ROIf, B, P) function, where ROIf is the ROI from 3.3, B is the binary image from 3.2 and P is the (i-1)th frame	
#				3.4.1  Read in the i-th image
#				3.4.2  Find the ROI of the image from the previous step with the B mask
#				3.4.3  Find the absolute difference between the two images; this will show where the blips are, as they will have high absolute difference values due to a sudden change of color
#				3.4.4  Create a binary image (using multiple thresholds) for the image showing the absolute difference
#				3.4.5  Do a dilation to spread the ROI, i.e. the blip area
#				3.4.6  Find the ROI of the acquired mask and the image P
#				3.4.7  Find the ROI of the acquired negative mask and the i-th image
#				3.4.8  Combine the to images to return the end result
#		7.5  Call the noJitter(I) function, which returns the denoised image I
#		7.6  Call the saveFrame(i,I) function, which saves the i-th frame in the folder 'filtered'	
#		7.7  Repeat steps 3.2 - 3.6 for all other values
#
# 8.  Call independentFrame(i) for frames 145 and 146, since they have scene-overlapping
#
# 9.  SCENE 4:
#		9.1  Call function scene4()
#				9.1.1  Read in the 179-th frame
#				9.1.2  Find the binary mask (using multiple thresholds) and dilate it to extract the text
#				9.1.3  Find the ROI of the image from 9.1.1 using the mask from 9.1.2
#				9.1.4  Return the found ROI
#		9.2  Save the ROI the appropriate number of times (this will result in the steadiness of the text)
#		
# 10. SCENE 5:
#		10.1  Repeat steps for SCENE 3, with the difference that the independent frame is 250
#
# 11. SCENE 6:
#		11.1  Call the independentFrame(i) function for all frames to get rid of the jitter
#
# 12. SCENE 7:
#		12.1  Call independentFrame(i) for frame 287 and save the returned value
#		12.2  Call the scene7(i, P) function, where P is the (i-1)th image
#				12.2.1  Read in the i-th frame and turn it into grayscale
#				12.2.2  Initialize the needed parameters (points for rectangles, color of rectangle, etc)
#				12.2.3  If Zorro is not jumping, initialize the parameters so they form a white rectangle in the upper left corner
#				12.2.4  If Zorro is jumping, apply the sharpening filter and return the filtered image
#				12.2.5  If Zorro is fleeing from the scene, initialize the parameters so they form a white rectangle in the upper half of the frame
#				12.2.6  If Zorro left the scene, initialize the parameters so they form two black rectangles in the lower right corner
#				12.2.7  Find the ROIs of the i-th and (i-1)th images using the mask from previous steps
#				12.2.8  Find the absolute difference between the two images; this will show where the blips are, as they will have high absolute difference values due to a sudden change of color
#				12.2.9  Find the binary mask (using multiple thresholds) of the difference image
#				12.2.10 Find the white areas of the binary mask
#				12.2.11 Once found, replace them and the surrounding pixels of picture i with the values of those pixels of picture (i-1); the surrounding pixels need to be replaced in order to create a more clear image
#				12.2.12 Return the acquired image
#		12.3  Call the noJitter(I) function, which returns the denoised image I
#		12.4  Call the saveFrame(i,I) function, which saves the i-th frame in the folder 'filtered'	
#		12.5  Repeat steps 12.2 - 12.4 for all other values
#
#
# 13. SCENE 8:
#		13.1  Call independentFrame(i) for frame 417, 418 and 419, and save the last returned value
#		13.2  Call the scene8(i, P) function, where P is the (i-1)th frame
#				13.2.1  Read in the i-th picture and get the width and the height of the picture
#				13.2.2  Turn the image to grayscale and create a black binary image
#				13.2.3  Draw a full, white rectangle on the binary image according to the specific points
#				13.2.4  Find the ROIs of the i-th and (i-1)th images using the mask from 13.2.3
#				13.2.5  Find the absolute difference between the two images; this will show where the blips are, as they will have high absolute difference values due to a sudden change of color
#				13.2.6  Find the binary mask (using multiple thresholds) of the difference image
#				13.2.7  Find the white areas of the binary mask
#				13.2.8  Once found, replace them and the surrounding pixels of picture i with the values of those pixels of picture (i-1); the surrounding pixels need to be replaced in order to create a more clear image
#				13.2.9  Return the acquired image
#		13.3  Call the noJitter(I) function, which returns the denoised image I
#		13.4  Call the saveFrame(i,I) function, which saves the i-th frame in the folder 'filtered'	
#		13.5  Repeat steps 13.2 - 13.4 for all other values
#
# 14. Call independentFrame(i) for frame 480, since it has scene-overlapping 
#
# 15. SCENE 9:
#		15.1  Call the scene9Pre() function to get rid of the blibs in the first frame of the scene
#				15.1.1  Read in the frames 481 and 482
#				15.1.2  Find the absolute difference between the two images; this will show where the blips are, as they will have high absolute difference values due to a sudden change of color
#				15.1.3  Find the areas with a big color change (where the values of the channels is greater than [55,55,55])
#				15.1.4  Once found, replace them and the surrounding pixels of picture i with the values of those pixels of picture (i-1); the surrounding pixels need to be replaced in order to create a more clear image
#				15.1.5  Return acquired image
#		15.2  Call the noJitter(I) function, which returns the denoised image I
#		15.3  Call the saveFrame(i,I) function, which saves the i-th frame in the folder 'filtered'	
#		15.4  Read in the i-th frame
#		15.5  Create a sharpening kernel
#		15.6  Apply the sharpening kernel to the image to reduce the imperfections
#		15.7  Call the noJitter(I) function, which returns the denoised image I
#		15.8  Call the saveFrame(i,I) function, which saves the i-th frame in the folder 'filtered'	
#		15.9  Repeat steps 15.4-15.8 for all other frames
#		15.10 Call independentFrame(i) for frame 515, since it has scene-overlapping
#
# 16. SCENE 10:
#		16.1  Read in the i-th image
#		16.2  Call the fixJitterScene10(i, P) function, where P is the image from 16.1
#				16.2.1  Read in the frame
#				16.2.2  Depending on the frame number, parts of the image from the previous step are used to cover parts from P
#				16.2.3  The modified image P is returned
#
#		16.3  Create a sharpening kernel
#		16.4  Apply the sharpening kernel to the image to reduce the imperfections
#		16.5  Call the noJitter(I) function, which returns the denoised image I
#		16.6  Call the saveFrame(i,I) function, which saves the i-th frame in the folder 'filtered'	
#		16.7  Repeat steps 16.1-16.6 for all other frames
#
# 17. Call independentFrame(i) for frames 547 and 548, since they have scene-overlapping
#
# 18. SCENE 11:
#		18.1  Create a sharpening kernel
#		18.2  Apply the sharpening kernel to the image to reduce the imperfections
#		18.3  Call the noJitter(I) function, which returns the denoised image I
#		18.4  Call the saveFrame(i,I) function, which saves the i-th frame in the folder 'filtered'	
#		18.5  Repeat steps 18.1-18.4 for all other frames
#
# 19. SCENE 12:
#		19.1  Read in the i-th image
#		19.2  Call the fixJitterScene10(i, P) function, where P is the image from 19.1
#				19.2.1  Read in the frame
#				19.2.2  Depending on the frame number, parts of the image from the previous step are used to cover parts from P
#				19.2.3  The modified image P is returned
#
#		19.3  Create a sharpening kernel
#		19.4  Apply the sharpening kernel to the image to reduce the imperfections
#		19.5  Call the noJitter(I) function, which returns the denoised image I
#		19.6  Call the saveFrame(i,I) function, which saves the i-th frame in the folder 'filtered'	
#		19.7  Repeat steps 16.1-16.6 for all other frames
#
# 20. Call independentFrame(i) for frame 620, since it has scene-overlapping 
#
# 21. SCENE 13:
#		21.1  Read in the i-th image and get the height and width
#		21.2  Darken the pixels which have a value above [190,190,190] to reduce too much lightening on some parts of the picture
#		21.3  Create a sharpening kernel
#		21.4  Apply the sharpening kernel to the image to reduce the imperfections
#		21.5  Call the noJitter(I) function, which returns the denoised image I
#		21.6  Call the saveFrame(i,I) function, which saves the i-th frame in the folder 'filtered'	
#		21.7  Repeat steps 16.1-16.6 for all other frames
#
# 22. SCENE 14:
#		22.1  Read in the i-th image 
#		22.2  Apply the bilateral filter
#		22.3  Call the noJitter(I) function, which returns the denoised image I
#		22.4  Call the saveFrame(i,I) function, which saves the i-th frame in the folder 'filtered'
#
# 23. Call the videoMaker() function
#		23.1  Read the first image from the folder 'filtered', and get the height and width
#		23.2  Initialize the VideoWriter
#		23.3  Write in all the frames from the folder 'fildered' to create a 'finalZorro.avi' video
#
#
# 24. Read in the first frame and multiply it by zero to turn it into black
#
# 25. Use the putText function to write a note for the user that the algorithm has finished
#
#
#
#
#		PERFORMANCE
#
# 1. Complexity: O(n^3), since the replacement of the blips is O(n^2), and it is called inside a for loop
#
# 2. Complexity consequences: the algorithm is slow since it has to process all the frames
#
# 3. Overall: 
# 		3.1 there are some magic numbers which were neccessary for the final result
#		3.2 majority of the larger blips were eliminated, some smaller blips remained
#		3.3 the jitter is gone
#		3.4 the quality of the video has increased
#		3.5 the scene with the text is not "jumpy" 
#		3.6 the comparison between frames shows changes, but they are not clearly visible on the video, please look at the folder 'examples for comparison' to see the actual changes
#
#
#
#		SCENES
#
#	Scene 			Frames
#	  1				[0,36]
#	  2				[39,89]
#	  3				[92,144]
#	  4				[147,248]
#	  5				[250,265]
#	  6				[266,286]
#	  7				[287,416]
#	  8				[419,479]
#	  9				[481,514]
#	  10			[516,546]
#	  11			[549,588]
#	  12			[589,619]
#	  13			[621,665]
#	  14			[666,703]
#
#
#


import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui


def grabFrames():
	camera = cv2.VideoCapture("Zorro.mp4")
	(grabbed, I) = camera.read()

	frame=0
	while grabbed:
		name = './frames/Frame{}.jpg'.format(frame)
		cv2.imwrite(name, I)
		frame = frame+1
		(grabbed, I) = camera.read()

def saveFrame(i, I):
	cv2.imwrite('./filtered/Frame{}.jpg'.format(i), I)

def noJitter(I):
	temp = cv2.fastNlMeansDenoisingColored(I, None, 10,10,7,21)
	return temp

def independentFrame(i):
	p = cv2.imread('./frames/Frame{}.jpg'.format(i))
	I = noJitter(p)
	saveFrame(i,I)
	return p

def scene1(i, previous):
	current = cv2.imread('./frames/Frame{}.jpg'.format(i))
	difference = cv2.absdiff(previous, current)
	h,w,d = previous.shape
	for j in range (0, h):
		for k in range (0,3*w/4-35):
			if(difference[j,k][0]>60 or difference[j,k][1]>60 or difference[j,k][2]>60):
				current[j-5:j+5,k-5:k+5]=previous[j-5:j+5,k-5:k+5]

	return current

def scene2(i):
	current = cv2.imread('./frames/Frame{}.jpg'.format(i))
	temp = current[:,110:743]
	filterk = np.array([[-0.2,-0.2,-0.2],[-0.2,2.4,-0.2],[-0.2,-0.2,-0.2]])
	currentN=current
	currentN[:,110:743] = cv2.filter2D(temp, ddepth=-1, kernel=filterk)
	return currentN

def specialScene2():
	p = cv2.imread('./frames/Frame86.jpg')
	current = cv2.imread('./frames/Frame87.jpg')
	difference = cv2.absdiff(p,current)
	h,w,d = p.shape
 	for j in range (0, h):
 		for k in range (0,w):
 			if(difference[j,k][0]>120 and difference[j,k][1]>120 and difference[j,k][2]>120):
 				current[j-5:j+5,k-5:k+5]=p[j-5:j+5,k-5:k+5]
 	I = noJitter(current)
	saveFrame(87,I)
	p = current
	current = cv2.imread('./frames/Frame88.jpg')

	difference = cv2.absdiff(p,current)
	h,w,d = p.shape
	for j in range (0, h):
		for k in range (0,w):
			if(difference[j,k][0]>120 and difference[j,k][1]>120 and difference[j,k][2]>120):
				current[j-5:j+5,k-5:k+5]=p[j-5:j+5,k-5:k+5]

	I = noJitter(current)
	saveFrame(88,I)

 	return current

def createBinaryScene3and5(I):

	save=I.copy()
	G = cv2.cvtColor(save, cv2.COLOR_BGR2GRAY)
	cv2.line(img = save, pt1=(185,479), pt2 = (350,0), color=(0,255,0), thickness=3)
	cv2.line(img = save, pt1=(475,0), pt2 = (853,468), color=(0,0,255), thickness=3)
	h,w,d = I.shape

	B = G*0

	green=0
	for j in range (0,h):
		for k in range(0,w):
			if (save[j,k][0]==0 and save[j,k][1]==255 and save[j,k][2]==0):
				green=1
				continue
			elif(save[j,k][0]==0 and save[j,k][2]==255 and save[j,k][1]==0):
				green=0
				break
			if(green==1):
				B[j,k]=255

	B[np.where((save==[0,255,0]).all(axis=2))] = 255
	B[np.where((save==[0,0,255]).all(axis=2))] = 255
	B = 255-B
	return B

def scene3and5(i, ROIf, B, P):
	I = cv2.imread('./frames/Frame{}.jpg'.format(i))

	ROI = cv2.bitwise_and(I,I,mask=B)
	
	difference = cv2.absdiff(ROIf, ROI)

	lowerR = (55,55,55)
	upperR = (250,250,250)
	Bf = cv2.inRange(difference,lowerR, upperR)

	shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4,4))
	nm = cv2.dilate(Bf, shape)
	Bf=nm

	ROI1 = cv2.bitwise_and(P,P,mask=Bf)
	Bf = 255 - Bf
	ROI2 = cv2.bitwise_and(I,I,mask=Bf)

 	final = cv2.bitwise_or(ROI1, ROI2)

 	return final

def scene4():
	I = cv2.imread('./frames/Frame179.jpg')

	lowerR = (68,68,68)
	upperR = (250,250,250)
	B = cv2.inRange(I,lowerR, upperR)

	shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
	nm = cv2.dilate(B, shape)
	B=nm

	ROI = cv2.bitwise_and(I,I,mask=B)

	return ROI

def scene7(i, P):
	Ic = cv2.imread('./frames/Frame{}.jpg'.format(i))
	I=cv2.cvtColor(Ic, cv2.COLOR_BGR2GRAY)
	temp = 60
	ptA=0
	ptB=0
	C=0
	B=I*0
	h,w,d=Ic.shape
	if (i>286 and i<324):
		ptA=(0,13)
		ptB=(540,220)
		C=(255,255,255)
		cv2.rectangle(img=B, pt1=ptA, pt2=ptB, color=C, thickness=-1)

	elif (i>=324 and i<341):

		copy=Ic.copy()
		kernel = np.zeros((9,9), np.float32)
		kernel[4,4]=2.0
		boxFilter = np.ones((9,9), np.float32)/81.0
		f = cv2.fastNlMeansDenoisingColored(Ic, None, 8,8,7,17)
		kern=kernel-boxFilter
		f = cv2.filter2D(f, ddepth=-1,kernel=kern)

		return Ic
	elif (i>=341 and i<355):
		ptA = (0,0)
		ptB = (550,230)
		C=(255,255,255)
		cv2.rectangle(img=B, pt1=ptA, pt2=ptB, color=C, thickness=-1)

	elif(i>=355 and i<=417):
		ptA = (465,0)
		ptB = (w,h)
		temp=64
		C=(255,255,255)
		cv2.rectangle(img=B, pt1=ptA, pt2=ptB, color=C, thickness=-1)
		ptA = (210,440)
		ptB = (w,h)
		cv2.rectangle(img=B, pt1=ptA, pt2=ptB, color=C, thickness=-1)
		B = 255-B

	roi = cv2.bitwise_and(Ic,Ic,mask=B)
	roi2 = cv2.bitwise_and(P,P,mask=B)
	difference = cv2.absdiff(roi, roi2)


	lowerR = (temp,temp,temp)
	upperR = (255,255,255)
	Bf = cv2.inRange(difference,lowerR, upperR)
	for j in range (0,h):
		for k in range (0,w):
			if (Bf[j,k]==255):
				Ic[j-5:j+5,k-5:k+5]=P[j-5:j+5,k-5:k+5]-5
				Ic[np.where((Ic<[0,0,0]).all(axis=2))] = [0,0,0]

	return Ic

def scene8(i, P):
	I=cv2.imread('./frames/Frame{}.jpg'.format(i))
	h,w,d = I.shape
	G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
	B=G*0
	if (i<464):
		ptA = (0,0)
		ptB = (280,120)
	elif(i>=464):
		ptA=(0,0)
		ptB=(330,40)
	C=(255,255,255)
	cv2.rectangle(img=B, pt1=ptA, pt2=ptB, color=C, thickness=-1)
	
	roi1 = cv2.bitwise_and(I,I,mask=B)
	roi2 = cv2.bitwise_and(P,P,mask=B)
	difference=cv2.absdiff(roi1, roi2)

	lowerR = (38,38,38)
	upperR = (255,255,255)
	Bf = cv2.inRange(difference,lowerR, upperR)
	for j in range (0,h):
		for k in range (0,w):
			if (Bf[j,k]==255):
				I[j-5:j+5,k-5:k+5]=P[j-5:j+5,k-5:k+5]

	return I

def scene9Pre():
	P = cv2.imread('./frames/Frame481.jpg')
	I = cv2.imread('./frames/Frame482.jpg')

	difference = cv2.absdiff(I,P)

	h,w,d = P.shape

	for j in range (0, h):
		for k in range (0,w):
			if(difference[j,k][0]>55 and difference[j,k][1]>55 and difference[j,k][2]>55):
				P[j-6:j+6,k-5:k+5]=I[j-6:j+6,k-5:k+5]

	return P

def fixJitterScene12(i, P):
	if (i==599 or i==600):
		t = cv2.imread('./frames/Frame598.jpg')
		P[152:163,250:262]=t[152:163,250:262]
		return P
	return P

def fixJitterScene10(i, P):
	if (i==522 or i==523):
		t = cv2.imread('./frames/Frame521.jpg')
		P[44:52,539:548]=t[44:52,539:548]
		return P
	if (i>=541 and i<544):
		t = cv2.imread('./frames/Frame540.jpg')
		P[367:382,172:193]=t[367:382,172:193]
		return P

	return P

def videoMaker():
	I = cv2.imread('./filtered/Frame0.jpg')
	h,w,d=I.shape
	wr = cv2.VideoWriter('finalZorro.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 13, (w, h))
	wr.write(I)
	for i in range(1,704):
		I = cv2.imread('./filtered/Frame{}.jpg'.format(i))
		wr.write(I)
	wr.release()
	cv2.destroyAllWindows()

#
#MAIN
#
grabFrames()

#SCENE1
p=independentFrame(0)
for i in range (1,37):
	p=scene1(i,p)
	I = noJitter(p)
	saveFrame(i,I)

x = independentFrame(37)
x = independentFrame(38)

#SCENE2
for i in range (39,90):
	p=scene2(i)
	if(i==87):
		p = specialScene2()
		i=i+1
		continue
	I = noJitter(p)
	saveFrame(i,I)


x = independentFrame(90)
x = independentFrame(91)

#SCENE3
p = independentFrame(92)
B = createBinaryScene3and5(p)
for i in range(93,145):
	ROIf = cv2.bitwise_and(p,p,mask=B)
	p = scene3and5(i, ROIf, B, p)
	I = noJitter(p)
	saveFrame(i,I)

x = independentFrame(145)
x = independentFrame(146)

#SCENE4
I = scene4()
for i in range(147,249):
	saveFrame(i,I)


x = independentFrame(249)

#SCENE5
p = independentFrame(250)
B = createBinaryScene3and5(p)
for i in range(251,266):
	ROIf = cv2.bitwise_and(p,p,mask=B)
	p = scene3and5(i, ROIf, B, p)
	I = noJitter(p)
	saveFrame(i,I)

#SCENE6
for i in range(266,287):
	x = independentFrame(i)

#SCENE7
p = independentFrame(287)
for i in range(288, 417):
	p = scene7(i,p)
	I = noJitter(p)
	saveFrame(i,I)


#SCENE8
p = independentFrame(417)
p = independentFrame(418)
p = independentFrame(419)
for i in range(420, 480):
	p = scene8(i,p)
	I = noJitter(p)
	saveFrame(i,I)


x=independentFrame(480)

#SCENE9
P = scene9Pre()
P = noJitter(P)
saveFrame(481,P)

for i in range (482,515):
	Ic = cv2.imread('./frames/Frame{}.jpg'.format(i))
	copy=Ic.copy()
	kernel = np.zeros((9,9), np.float32)
	kernel[4,4]=2.0
	boxFilter = np.ones((9,9), np.float32)/81.0
	kern=kernel-boxFilter
	f = cv2.filter2D(Ic, ddepth=-1,kernel=kern)
	f=noJitter(f)
	saveFrame(i,f)

x=independentFrame(515)

#SCENE10
for i in range (516,547):
	Ic = cv2.imread('./frames/Frame{}.jpg'.format(i))
	Ic = fixJitterScene10(i,Ic)
	copy=Ic.copy()
	kernel = np.zeros((9,9), np.float32)
	kernel[4,4]=2.0
	boxFilter = np.ones((9,9), np.float32)/81.0
	kern=kernel-boxFilter
	f = cv2.filter2D(Ic, ddepth=-1,kernel=kern)
	f=noJitter(f)
	saveFrame(i,f)


x = independentFrame(547)
x = independentFrame(548)

#SCENE11
for i in range (549,589):
	Ic = cv2.imread('./frames/Frame{}.jpg'.format(i))
	copy=Ic.copy()
	kernel = np.zeros((9,9), np.float32)
	kernel[4,4]=2.0
	boxFilter = np.ones((9,9), np.float32)/81.0
	kern=kernel-boxFilter
	f = cv2.filter2D(Ic, ddepth=-1,kernel=kern)
	f=noJitter(f)
	saveFrame(i,f)


#SCENE12
for i in range (589,620):
	Ic = cv2.imread('./frames/Frame{}.jpg'.format(i))
	Ic = fixJitterScene12(i,Ic)
	copy=Ic.copy()
	kernel = np.zeros((9,9), np.float32)
	kernel[4,4]=2.0
	boxFilter = np.ones((9,9), np.float32)/81.0
	kern=kernel-boxFilter
	f = cv2.filter2D(Ic, ddepth=-1,kernel=kern)
	f=noJitter(f)
	saveFrame(i,f)


x = independentFrame(620)

#SCENE13
for i in range (621,666):
	Ic = cv2.imread('./frames/Frame{}.jpg'.format(i))
	h,w,d=Ic.shape
	
	Ic[np.where((Ic>[190,190,190]).all(axis=2))] = Ic[np.where((Ic>[190,190,190]).all(axis=2))] - 15

	copy=Ic.copy()
	kernel = np.zeros((9,9), np.float32)
	kernel[4,4]=2.0
	boxFilter = np.ones((9,9), np.float32)/81.0
	kern=kernel-boxFilter
	f = cv2.filter2D(Ic, ddepth=-1,kernel=kern)

	f=noJitter(f)
	saveFrame(i,f)


#SCENE14
for i in range(666, 704):
	I = cv2.imread('./frames/Frame{}.jpg'.format(i))
	I2 = cv2.bilateralFilter(I,9,61,61)
	f=noJitter(I2)
	saveFrame(i,f)


videoMaker()

I = cv2.imread('./frames/Frame0.jpg')
I=I*0
h,w,d=I.shape
cv2.putText(I, "DONE! Look for finalZorro.avi! Press any key to exit.", (5, h/2), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)

cv2.imshow('f', I)
key = cv2.waitKey(0)