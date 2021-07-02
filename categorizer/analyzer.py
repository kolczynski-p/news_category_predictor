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

    def word_count(self, count, limit):
        self.data['word_count'] = self.data[count].apply(lambda x: len(str(x).split(" ")))
        patches = plt.hist(self.data['word_count'], 150, density=1, facecolor='g', alpha=0.75)
        plt.xlabel('Word count')
        plt.ylabel('probability densit')
        plt.title('Histogram of word amount')
        plt.xlim(0, limit)
        plt.grid(True)
        plt.show()

    def word_avg(self):
        words = {'Category':self.data['category'].unique(), 'Word_count':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 'Amount_of_cat':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
        unique_category = pd.DataFrame(words)
        unique_category.index = self.data['category'].unique()

        index = 0
        for a in self.data['category']:
            if a == self.data['category'][index]:
                unique_category['Word_count'][a] = unique_category['Word_count'][a] + self.data['word_count'][index]
                unique_category['Amount_of_cat'][a] = unique_category['Amount_of_cat'][a]+1
            index = index+1

        for a in unique_category['Category']:
            unique_category['Word_count'][a] = unique_category['Word_count'][a]/unique_category['Amount_of_cat'][a]   

        x=unique_category['Category']
        y=unique_category['Word_count']

        fig, ax = plt.subplots(figsize=(25,10))
        plt.xticks(rotation=90)
        plt.xlabel('Average word')
        ax.plot(x, y)
        

