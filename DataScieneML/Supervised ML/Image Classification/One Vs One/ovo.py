import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import os
from pathlib import Path
from keras.preprocessing import image
#import tensorflow

# ### Data Preparation and Reading
p=Path("../images")
dirs=p.glob("*")
#labels=[]

dir={
    "cat":0,
    "dog":1,
    "horse":2,
    "human":3
}

img_data=[]
labels=[]

for folder_name in dirs:
    #print(folder_name)
    label=str(folder_name).split("/")[-1][:-1]
    #labels.append(label)

    for img_path in folder_name.glob("*.jpg"):
        img=image.load_img(img_path,target_size=(100,100)) 
        img_array=image.img_to_array(img)
        img_data.append(img_array)
        labels.append(dir[label])


print(len(img_data)," for label ",len(labels))

#Convert Image_data and labels to numpy array
img_data=np.array(img_data,dtype="float32")/255.0
labels=np.array(labels)

print(img_data.shape,labels.shape)


import random

data=list(zip(img_data,labels))
random.shuffle(data)

#Unzip
img_data[:],labels[:]=zip(*data)

## Visualise this data
def draw_img(img):
    plt.imshow(img)
    return


#draw_img(image_data[0])


# SVM Class
class SVM:
    
    def __init__(self,C=1.0):
        self.C=C
        self.W=0
        self.b=0
        
        
    def hingeLoss(self,W,b,X,Y):
        m=X.shape[0]
        loss=0.0
        loss+=0.5*np.dot(W,W.T)
        
        for i in range(m):
            ti=Y[i]*(np.dot(W,X[i].T))+b
            loss+=self.C*(max(0,1-ti))
        
        return loss[0][0]
        
    
    def fit(self,X,Y,batch_size=100,learning_rate=0.001,max_itr=300):
        no_of_features=X.shape[1]
        no_of_samples=X.shape[0]
        
        c=self.C
        
        #Initiatize the model parameters
        W=np.zeros((1,no_of_features))
        bias=0
        
        #print(self.hingeLoss(W,bias,X,Y))
        
        #Training Here
        #Weight and Bias update rule
        
        losses=[]
        
        for i in range(max_itr):
            l=self.hingeLoss(W,bias,X,Y)
            losses.append(l)
            ids=np.arange(no_of_samples)
            np.random.shuffle(ids)
            
            #Batch Gradient Descent with random shuffling
            for batch_start in range(0,no_of_samples,batch_size):
                #Assume Zero Gradient
                gradw=0
                gradb=0
                
                #Iterate over all examples in the batch size
                for j in range(batch_start,batch_start+batch_size):
                    if j <no_of_samples:
                        i=ids[j]
                        ti=Y[i]*(np.dot(W,X[i].T)+bias)
                        
                        if ti>=1:
                            gradw+=0
                            gradb+=0
                            
                        else:
                            gradw+=c*Y[i]*X[i]
                            gradb+=c*Y[i]
                
                #Gradient for the batch is ready, Update Weight and bias
                
                W=W-learning_rate*W+learning_rate*gradw
                bias=bias+learning_rate*gradb
            
        
        self.W=W
        self.b=bias
        return W,bias,losses






M=img_data.shape[0]

img_data=img_data.reshape(M,-1)

print(img_data.shape,labels.shape)

Classes=len(np.unique(labels))
print(Classes)



def classWiseData(X,Y):
    data={}
    
    for i in range(Classes):
        data[i]=list()
        
    for i in range(X.shape[0]):
        data[Y[i]].append(X[i])
        
    for k in data.keys():
        data[k]=np.array(data[k])
    return data

data=classWiseData(img_data,labels)
print(data[0])


def getDataPairsForSVM(d1,d2):
    
    '''Combined datas of two classes into one'''
    
    l1,l2=d1.shape[0],d2.shape[0]
    samples=l1+l2
    features=d1.shape[1]
    
    data_pair=np.zeros((samples,features))
    data_labels=np.zeros((samples,))
    
    data_pair[:l1,:]=d1
    data_pair[l1:,:]=d2
    
    data_labels[:l1]=-1
    data_labels[l1]=+1
    
    return data_pair,data_labels

def classWiseData(X,Y):
    data={}
    
    for i in range(Classes):
        data[i]=[]
        
    for i in range(X.shape[0]):
        data[Y[i]].append(X[i])
        
    for k in data.keys():
        data[k]=np.array(data[k])
    return data

def trainSVMs(X,Y):
    svm=SVM()
    svm_classifiers={}
    
    #data=classWiseData(X,Y)
    
    for i in range(Classes):
        svm_classifiers[i]={}
        
        for j in range(i+1,Classes):
            Xpair,Ypair=getDataPairsForSVM(data[i],data[j])
            wts,bias,loss=svm.fit(Xpair,Ypair)
            svm_classifiers[i][j]=(wts,bias)
    
    return svm_classifiers


svm_classifiers=trainSVMs(img_data,labels)
#Parameters for cats and dogs

cat_dogs=svm_classifiers[0][1]
print(cat_dogs[0].shape) #weights
print(cat_dogs[1]) #bias


## Predictions
def binaryPredict(x,w,b):
    z=np.dot(x,w.T)+b
    if z>=0:
        return 1
    else:
        return -1


def predict(x):
    count=np.zeros((Classes,))
    
    for i in range(Classes):
        for j in range(i+1,Classes):
            w,b=svm_classifiers[i][j]
            #Take a majority prediction
            z=binaryPredict(x,w,b)
            if z==1:
                count[j]+=1
            else:
                count[i]+=1
                
    #print(count)
    return np.argmax(count)
            

for i in range(700,800,6):
    print("predict for ",i," ith",predict(img_data[i])," ",labels[i])
