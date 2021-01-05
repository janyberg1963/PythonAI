
import cv2


trained_face_data= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
test = trained_face_data.load('AIFace/haarcascade_frontalface_default.xml')
print (test)

#img=cv2.imread('AIFace\craploadoffaces.png')


webcam = cv2.VideoCapture(0)


while True:
    
    successfull_frame_read, frame = webcam.read()


    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for (x, y, w, h) in face_coordinates:
    
        cv2.rectangle(frame,(x, y),(x+w,y+h), (0, 255, 0 ), 2)

    cv2.imshow('Lookforface', frame)
    key = cv2.waitKey(1)


    if key==81 or key==113:
        break

print("code completed")

"""




print(face_coordinates)

cv2.imshow('Lookforface', img)
cv2.waitKey()

print("Code Completed")


"""
