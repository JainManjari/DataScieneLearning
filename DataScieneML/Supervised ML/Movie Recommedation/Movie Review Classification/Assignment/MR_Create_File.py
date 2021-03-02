import pandas as pd
import numpy as np


from nltk.stem.snowball import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


#Reading data
df=pd.read_csv("Train.csv")
df_test=pd.read_csv("Test.csv").iloc[:,:].values.reshape(-1,)

X=df.iloc[:,0].values

Y=df.iloc[:,1].values
Y[Y=="pos"]=1
Y[Y=="neg"]=0


# Function Initiation
ps=PorterStemmer()
tokenizer=RegexpTokenizer(r'\w+')


sw=set(stopwords.words('english'))


def mytokenizer(text,i):
    text=text.lower()
    text=text.replace("<br /><br />"," ")
    words=tokenizer.tokenize(text)
    words=[w for w in words if w=="not" or w not in sw]
    words=[ps.stem(w) for w in words]
    print(i,end=" ")
    return " ".join(words)


X_clean=[mytokenizer(X[i],i) for i in range(X.shape[0])]
print()
X_test_clean=[mytokenizer(df_test[i],i) for i in range(df_test.shape[0])]


X_clean_df=pd.DataFrame(X_clean)

X_clean_df.to_csv("Cleaned_X.csv",index=None)

Y_df=pd.DataFrame(Y)

Y_df.to_csv("Y.csv",index=None)

X_test_df=pd.DataFrame(X_test_clean)

X_test_df.to_csv("X_test_Clean.csv",index=None)




