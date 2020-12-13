'''
1) Load the Training data:
    a) x - values stored in the numpy array
    b) y - values we need to assign to each person
2) Read video using opencv
3) Extract faces from it
4) Use KKN to predict the face of the test data
5) Map the predicted id to the name of user
6) Display the predictions on the screen - bounding box and name

'''

import cv2
import numpy as np
import os


######   KKN  #################
def KKN(train,test_point,K=5):
    res=[]
    
    for i in range(train.shape[0]):
        x=train[i,:-1]
        y=train[i,-1]
        dist=(np.sum((x-test_point)**2)**0.5)
        res.append((dist,y))
    
    res=sorted(res)
    res=np.array(res[:K])
    labels=np.unique(res[:,1],return_counts=True)
    ind=np.argmax(labels[1]) 
    return labels[0][ind]


#Initialize camera
cap=cv2.VideoCapture(0)

#Detect Faces
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

#Data Storage
count=0
data_path="./data/"
face_data=[]
labels=[]


class_id=0

names={} #mapping btw id and name

#Data Preparation

for fx in os.listdir(data_path):
    if fx.endswith(".npy"):
        names[class_id]=fx.split(".npy")[0]
        data_item=np.load(data_path+fx)
        face_data.append(data_item)

        #Create label 
        target=class_id*np.ones((data_item.shape[0],))
        class_id+=1
        labels.append(target)

face_dataset=np.concatenate(face_data,axis=0)
face_labels=np.concatenate(labels,axis=0)

print(face_dataset.shape)
print(face_labels.shape)

face_labels=face_labels.reshape(-1,1)

print(face_labels.shape)

train_dataset=np.concatenate((face_dataset,face_labels),axis=1)

print(train_dataset.shape)

#Testing
while True:
    
    ret,frame=cap.read()

    if ret==False:
        continue
    
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(frame,1.3,5)

    for (x,y,w,h) in faces:
        #Extract the Region of Interest
        offset=10
        face_section=gray_frame[y-offset:y+h+offset,x-offset:x+w+offset]   #y,x
        face_section=cv2.resize(face_section,(100,100))

        #Predict the output
        out=KKN(train_dataset,face_section.flatten())

        #show in cv2
        pred_name=names[int(out)]
        cv2.putText(frame,pred_name,(x,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2,cv2.LINE_AA)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(1,1,255),2)
    
    cv2.imshow("Video Frame ",frame)
  

    key_pressed=cv2.waitKey(1) & 0xFF

    if key_pressed==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()


