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