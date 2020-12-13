#Read a Video Stream from Camera(Frame by Frame)

import cv2

cap=cv2.VideoCapture(0) #0 stands for default webcam

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if ret==False: #if the image is not captured properly
        continue

    #cv2.imshow("Video Frame ",frame)
    cv2.imshow(" Gray Video Frame ",gray)

    #Wait for user input - q , then stop the loop

    key_pressed=cv2.waitKey(1) & 0xFF #cv2.waitKey(1) gives 32 bit number but ord('q') has 8 bits number 
                                      #so we are using logical and with 8 bits of 1 => 0xFF => to get last 8 bits
    if key_pressed==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
