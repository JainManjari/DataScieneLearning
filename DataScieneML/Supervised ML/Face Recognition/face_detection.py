#Read a Video Stream from Camera(Frame by Frame)

import cv2

cap=cv2.VideoCapture(0) #0 stands for default camera

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if ret==False: #if the image is not captured properly
        continue

    faces=face_cascade.detectMultiScale(frame,1.3,5) #scalingFactor 
                                                    #used to enlarge or dimished the image captured 
                                                    #1.3 means increase the image by 30% or 
                                                    #0.05 means decrease the image by 5%
                                                    #minNeigbhors should be btw 3-6, higher no will result in worse results

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) #img, pt1,pt2,color,thickness
    
    cv2.imshow("Video Frame ",frame)

    #Wait for user input - q , then stop the loop

    key_pressed=cv2.waitKey(1) & 0xFF #cv2.waitKey(1) gives 32 bit number but ord('q') has 8 bits number 
                                      #so we are using logical and with 8 bits of 1 => 0xFF => to get last 8 bits
    if key_pressed==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



