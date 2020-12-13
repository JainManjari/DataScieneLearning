'''
1) Read, show video stream and capture images
2) Detect faces and show bounding box
3) Flatten the largest face (grayscale: to save memory) and store it as numpy array
4) Repeat this process for multiple people to get training data

'''

import cv2
import numpy as np

#Initialize camera
cap=cv2.VideoCapture(0)


#Detect Faces
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

#Data Storage
count=0
face_data=[]
data_path="./data/"


file_name=input("Enter the name of the person: ")

while True:

    ret,frame=cap.read()

    if ret==False:
        continue
    
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(frame,1.3,5)

    #sort the face having the largest frame => x,y,w,h => area=> w*h => f[2]*f[3]
    faces=sorted(faces,key=lambda f: f[2]*f[3],reverse=True)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(1,1,255),2)
        #Extract the Region of Interest
        offset=10
        face_section=gray_frame[y-offset:y+h+offset,x-offset:x+w+offset]   #y,x
        face_section=cv2.resize(face_section,(100,100))
        cv2.imshow("Face Section ",face_section)

        count+=1
        #Stored every 10th Face
        if count%10==0:
            #Stored the face
            face_data.append(face_section)
            print(len(face_data))


    
    cv2.imshow("Video Frame ",frame)
  

    key_pressed=cv2.waitKey(1) & 0xFF

    if key_pressed==ord('q'):
        break


#Convert our face list data into numpy array
face_data=np.array(face_data)
face_data=face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)


#Save this data into file
np.save(data_path+file_name+".npy",face_data)
print("Data successfully saved at "+data_path+file_name+".npy")

cap.release()
cv2.destroyAllWindows()