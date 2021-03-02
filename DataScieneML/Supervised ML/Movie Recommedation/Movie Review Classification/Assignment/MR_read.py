import pandas as pd
import numpy as np

X=pd.read_csv("Cleaned_X.csv").values
X=X.reshape(-1,)
Y=pd.read_csv("Y.csv").values
Y=Y.reshape(-1,)

print(X.shape,type(X))
print(Y.shape,type(Y))

# Splitting data
from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=5,test_size=0.2)
print(X_train[0],Y_train[0])




from sklearn.feature_extraction.text import CountVectorizer

cv=CountVectorizer()

x_vec=cv.fit_transform(X_train)

xt_vec=cv.transform(X_test)


from sklearn.naive_bayes import MultinomialNB

mnb=MultinomialNB()

mnb.fit(x_vec,Y_train)

Y_predict=mnb.predict(x_vec)

print(mnb.score(x_vec,Y_train))

print(mnb.score(xt_vec,Y_test))
