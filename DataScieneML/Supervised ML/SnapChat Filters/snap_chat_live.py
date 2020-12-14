import cv2
import matplotlib.pyplot as plt

front_eyes_cascade=cv2.CascadeClassifier("frontalEyes35x16.xml")
nose_cascade=cv2.CascadeClassifier("Nose18x15.xml")



cap=cv2.VideoCapture(0)

while True:

    ret,frame=cap.read()

    if ret==False:
        continue

    glasses=cv2.imread("glasses.png",cv2.IMREAD_UNCHANGED)
    glasses=cv2.cvtColor(glasses,cv2.COLOR_BGRA2RGBA)
    mustache=cv2.imread("mustache.png",cv2.IMREAD_UNCHANGED)
    mustache=cv2.cvtColor(mustache,cv2.COLOR_BGRA2RGBA)
    eyes=front_eyes_cascade.detectMultiScale(frame,1.1,5)
    noses=nose_cascade.detectMultiScale(frame,1.1,5)

    for (x,y,w,h) in eyes:
        glasses=cv2.resize(glasses,(w-10,h+10))
        for i in range(glasses.shape[0]):
            for j in range(glasses.shape[1]):
                if(glasses[i,j,3]>0):
                    frame[y+i,x+j,:]=glasses[i,j,:-1]

    
    # for (x,y,w,h) in noses:
    #     mustache=cv2.resize(mustache,(w+10,h-20))
    #     for i in range(mustache.shape[0]):
    #         for j in range(mustache.shape[1]):
    #             if(mustache[i,j,3]>0):
    #                 frame[y+i+40,x+j,:]=mustache[i,j,:-1]

    
    cv2.imshow("Image ",frame)

    key=cv2.waitKey(1) & 0xFF

    if key==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()


