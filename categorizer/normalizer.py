import categorizer
import numpy as np
import pandas as pd
import json
import nltk
from nltk.corpus import stopwords


class Normalizer():

    def __init__(self, src, dataframe=pd.DataFrame(), lang='english'):
        self.src = src
        self.data = dataframe
        nltk.download('stopwords')
        self.stop = stopwords.words(lang)


    def load_file_json(self):
        with open(self.src, encoding="utf8") as f:
            data = f.readlines()
            data = [json.loads(line) for line in data]
        self.data = pd.DataFrame(data)


    def describe(self):
        print(self.data.info())
        print(self.data.head(100))


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

