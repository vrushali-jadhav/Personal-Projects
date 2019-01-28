import cv2 

#0 as input here will take file as just black and white
img = cv2.imread('galaxy.jpg',0)

#img is a numpy array
print(type(img))
print(img)

#number of rows and columns
print(img.shape)

#number of dimensions
print(img.ndim)

#resize the image
#resizedImg = cv2.resize(img,(1000,500))

#to get the half the actual size of the image
halfSizeImage = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

#display the image
cv2.imshow("Galaxy1",halfSizeImage)

cv2.imwrite('NewGalaxy.jpg',halfSizeImage)

#wait for 2 secs. After that the window is closed
cv2.waitKey(10000)

#this will give an option to close the image
cv2.destroyAllWindows()