#Notes:
#All the OpenCV array structures are converted to-and-from Numpy arrays.
#OpenCV supports a lot of algorithms related to Computer Vision and Machine Learning
#OpenCV-Python is the Python API of OpenCV. It combines the best qualities of OpenCV C++ API and Python language.
#Numpy is a highly optimized library for numerical operations. It gives a MATLAB-style syntax. 
#All the OpenCV array structures are converted to-and-from Numpy arrays. 
#So whatever operations you can do in Numpy, you can combine it with OpenCV

import cv2, time, pandas
from datetime import datetime

#you can pass 0,1,2 depending on which camera of your laptop do you want to use
#you can also use a video file for this
video = cv2.VideoCapture(0)
first_frame = None
statusList = [None,None]
timesObjectRecorded = []
df = pandas.DataFrame(columns=["Start Time","End Time"]) 

while True:
    check, frame = video.read()
    
    #used to track how many times object entred the frame
    status = 0

    #print(check)
    print(frame)
    
    greyFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #we are blurring the images as this will smooth the images out and it would be easier to identify the difference 
    #(21,21): parameters of blurriness
    #0: standard deviation
    greyFrame = cv2.GaussianBlur(greyFrame,(21,21),0)
    
    #catch the 1st frame
    if first_frame is None:
        first_frame = greyFrame
        #continue
    
    #this frame would be the difference between 1st frame adn rest
    delta_frames =  cv2.absdiff(first_frame,greyFrame)

    #if the delta is more than 30, we want the pixels to be colored white
    colored_delta_frames = cv2.threshold(delta_frames,30,255,cv2.THRESH_BINARY)[1]

    #lets dilate the frames to remove black holes from the background (shodows being detected as objects)
    cv2.dilate(colored_delta_frames,None,iterations=2)

    (cnts,_)=cv2.findContours(colored_delta_frames.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour)<1000:
            continue
        status = 1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
    #when object enters the frame
    if statusList[-1]==1 and statusList[-2]==0:
        timesObjectRecorded.append(datetime.now())

    #when object exits the frame
    if statusList[-1]==0 and statusList[-2]==1:
        timesObjectRecorded.append(datetime.now())

    statusList.append(status)
    cv2.imshow("capturedViaCam",greyFrame)
    cv2.imshow("deltaImage",delta_frames)
    cv2.imshow("coloredDeltaImage",colored_delta_frames)
    cv2.imshow("coloredContouredDeltaImage",frame)

    #press any key and i t'll close the frame
    key = cv2.waitKey(1)
    if key==ord('q'):
        break

if status == 1:
    timesObjectRecorded.append(datetime.now())
print(statusList)
print(timesObjectRecorded)

for i in range(0,len(timesObjectRecorded),2):
    df = df.append({"Start Time":timesObjectRecorded[i],"End Time":timesObjectRecorded[i+1]},ignore_index=True)

df.to_csv("Time Recording.csv")
video.release()
cv2.destroyAllWindows()
