import categorizer
import numpy as np
import pandas as pd
import json
import nltk
import matplotlib.pyplot as plt
import matplotlib
from nltk.corpus import stopwords
import textblob         
from textblob import TextBlob
from textblob import Word

        


class Analyzer():

    def __init__(self, dataframe=pd.DataFrame(), lang='english'):
        self.data = dataframe
        nltk.download('stopwords')
        nltk.download('wordnet')
        self.stop = stopwords.words(lang)

    def word_count(self):
        self.data['word_count'] = self.data['text'].apply(lambda x: len(str(x).split(" ")))
        patches = plt.hist(self.data['word_count'], 150, density=1, facecolor='g', alpha=0.75)
        plt.xlabel('Word count')
        plt.ylabel('probability densit')
        plt.title('Histogram of word amount')
        plt.xlim(0, 50)
        plt.grid(True)
        plt.show()
        

