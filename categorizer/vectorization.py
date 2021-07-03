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
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

        


class Vectorizer():

    def __init__(self, dataframe=pd.DataFrame(), lang='english'):
        self.data = dataframe
        nltk.download


    def TfidVectorizer():
        print("test")