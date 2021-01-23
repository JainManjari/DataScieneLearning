from keras.datasets import mnist
import pandas as pd

(X_train,Y_train),(X_test,Y_test)=mnist.load_data()

X_train=X_train.reshape((X_train.shape[0],X_train.shape[1]*X_train.shape[2]))

df1=pd.DataFrame(X_train)

df1.to_csv("X_Train.csv",index=None)

df2=pd.DataFrame(Y_train)

df2.to_csv("Y_Train.csv",index=None)

X_test=X_test.reshape((X_test.shape[0],X_test.shape[1]*X_test.shape[2]))

df3=pd.DataFrame(X_test)

df3.to_csv("X_Test.csv",index=None)

df4=pd.DataFrame(Y_test)

df4.to_csv("Y_Test.csv",index=None)