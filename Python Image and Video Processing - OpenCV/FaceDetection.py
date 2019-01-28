import cv2

#use the haarcascade file to detect face
face_cascade = cv2.CascadeClassifier("data/haarcascades/haarcascade_frontalface_default.xml")

#read the file
img = cv2.imread("InputFiles/Face.jpg")

#convert it to greyscale as that increases accuracy
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#scale factor of 1.05 tells python to downscale the image by 5% of the original size (in a loop) and look for bigger faces in
#the image
face = face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)

for x,y,w,h in face:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

resized_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("detected",resized_img)
cv2.waitKey(10000)
cv2.destroyAllWindows()

