import cv2
import matplotlib.pyplot as plt
import os

front_eyes_cascade=cv2.CascadeClassifier("frontalEyes35x16.xml")
nose_cascade=cv2.CascadeClassifier("Nose18x15.xml")

path="Photos/"

for filename in os.listdir(path):

    img=cv2.imread(path+filename)
    #img2=cv2.imread("Before.png")
    glasses=cv2.imread("glasses.png",cv2.IMREAD_UNCHANGED)
    glasses=cv2.cvtColor(glasses,cv2.COLOR_BGRA2RGBA)
    mustache=cv2.imread("mustache.png",cv2.IMREAD_UNCHANGED)
    mustache=cv2.cvtColor(mustache,cv2.COLOR_BGRA2RGBA)



    eyes=front_eyes_cascade.detectMultiScale(img,1.1,5)
    nose=nose_cascade.detectMultiScale(img,1.1,5)

    x,y,w,h=eyes[0]
        #cv2.imshow("Eyes ",eyes_section)
    glasses=cv2.resize(glasses,(w-10,h+10))

    for i in range(glasses.shape[0]):
        for j in range(glasses.shape[1]):
            if(glasses[i,j,3]>0):
                img[y+i,x+j,:]=glasses[i,j,:-1]


    
    x,y,w,h=nose[0]
    mustache=cv2.resize(mustache,(w+20,h-12))

    for i in range(mustache.shape[0]):
        for j in range(mustache.shape[1]):
            if(mustache[i,j,3]>0):
                img[y+i+35,x+j,:]=mustache[i,j,:-1]


    #cv2.imshow("Filter Detection ",img)
    #cv2.waitKey(1000)
    new_file=filename[:-4]+"_filter"+".jpg"
    print(new_file)
    cv2.imwrite("./Filter Photos/"+new_file,img)



#cv2.waitKey(0)
cv2.destroyAllWindows()