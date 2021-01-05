#here is code to check the output
import cv2
face_cascade=cv2.CascadeClassifier(r"C:\Users\jeffa\OneDrive\Desktop\temp1\classifier\cascade.xml")###path of cascade file
test = face_cascade.load(r"C:\Users\jeffa\OneDrive\Desktop\temp1\classifier\cascade.xml")
print (test)



## following is an test image u can take any image from the p folder in the temp folder and paste address of it on below line 

try:
    img= cv2.imread("AIFace\cup.jpg")
    img= cv2.resize(img,(1500,1500))
except Exception as e:
    print(str)

###path of image file which we want to detect
#resized = cv2.resize(img,(400,200))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,6.5,17)#try to tune this 6.5 and 17 parameter to get good result 
##if not getting good result try to train new cascade.xml file again deleting other file expect p and n in temp folder
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()