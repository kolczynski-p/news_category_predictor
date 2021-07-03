import categorizer
import numpy as np
import pandas as pd
import json
import nltk
from nltk.corpus import stopwords
import textblob         
from textblob import TextBlob
from textblob import Word

        


class Normalizer():

    def __init__(self, src, sampleSize, dataframe=pd.DataFrame(), lang='english'):
        self.src = src
        self.data = dataframe
        self.sampleSize=sampleSize
        nltk.download('stopwords')
        nltk.download('wordnet')
        self.stop = stopwords.words(lang)
        


    def load_file_json(self):
        with open(self.src, encoding="utf8") as f:
            data = f.readlines()
            data = [json.loads(line) for line in data]
        self.data = pd.DataFrame(data)
        self.data = self.data.sample(n=self.sampleSize, random_state=1)


    def describe(self):
        print(self.data.info())


    def concat_cols(self, target, cols):
        self.data[str(target)] = self.data[cols[0]] + ' ' + self.data[cols[1]]


    def drop_cols(self, cols):
        self.data = self.data.drop(columns=cols)


    def drop_stopwords(self, cols):
        stop = self.stop + [x.capitalize() for x in self.stop]
        for c in cols:
            self.data[c] = self.data[c].apply(lambda x: " ".join(x for x in x.split() if x not in stop))


    def to_lower(self, cols):
        for c in cols:
            self.data[c] = self.data[c].map(lambda x: x if type(x)!=str else x.lower())

    def drop_num(self, cols):
        for c in cols:
            self.data[c] = self.data[c].apply(lambda x: " ".join(x for x in x.split() if not x.isdigit() ))

    def drop_spec(self, cols):
        for c in cols:
            self.data[c] = self.data[c].str.replace('[^\w\s]','')

    def drop_rarest(self, amount):
            freq = pd.Series(' '.join(self.data['text']).split()).value_counts()
            freq = freq.where(freq>=amount)
            freq = freq.dropna()
            freq = list(freq.index)
            
            self.data['text'] = self.data['text'].apply(lambda x: " ".join(x for x in x.split() if x in freq))
    
    def lemmatize(self):
        
        self.data['text'] = self.data['text'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
    
    def n_grams(self,i,n):
        return TextBlob(self.data['text'][i]).ngrams(n)
    
    def data_detals(self):
       return 0




    