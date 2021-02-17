#!/usr/bin/env python
# coding: utf-8

# ## Create a NLP Pipeline to clean review data
# 
# - Load Input file and read reviews
# - Tokenize
# - Remove stopwords
# - Performed stemming
# - Write clean data to output file

# ## NLTK



from nltk.stem.snowball import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

import sys

ps=PorterStemmer()
tokenizer=RegexpTokenizer(r'\w+')


sw=set(stopwords.words('english'))


def mytokenizer(text):
    text=text.lower()
    text=text.replace("<br /><br />"," ")
    words=tokenizer.tokenize(text)
    words=[w for w in words if w=="not" or w not in sw]
    words=[ps.stem(w) for w in words]
    return " ".join(words)



sample_text='''
            I loved this movie since I was 7 and I saw it on the opening day. It was so touching and beautiful. 
            I strongly recommend seeing for all. 
            It's a movie to watch with your family by far.
            <br /><br />My MPAA rating: PG-13 for thematic elements, prolonged scenes of disastor, 
            nudity/sexuality and some language.
           '''

print(mytokenizer(sample_text))




def getReviews(inputFile,outputFile):

    out =open(outputFile,"w",encoding="utf8")
    
    with open(inputFile,encoding="utf8") as f:
        sent=f.readlines()
        print("len ",len(sent))
        count=1
        for s in sent:
            new_s=mytokenizer(s)
            print(count,end=" ")
            count+=1
            print((new_s),file=out)


    out.close()




# Read Command Line Arguments

inputFile=sys.argv[1]
outputFile=sys.argv[2]

#python MR.py imdb_trainX.txt imdb_cleaned_xtrain.txt

getReviews(inputFile,outputFile)


