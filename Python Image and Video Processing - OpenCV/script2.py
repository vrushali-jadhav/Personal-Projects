import glob
import cv2

files = glob.glob('InputFiles/*.jpg')
i=0
for file in files:
    img = cv2.imread(file,0)
    re = cv2.resize(img,(100,100))
    cv2.imshow("fileNameToDisplay",re)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()
    cv2.imwrite("InputFiles/resized_"+str(i)+".jpg",img)
    i=i+1