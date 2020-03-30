#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 13:43:51 2020

@author: katerinaroza
"""
#^nclude
import pandas as pd
import nltk 
from bs4 import BeautifulSoup
import string
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer 
from nltk.stem.porter import PorterStemmer


df=pd.read_csv("twitter_pleasant.csv")



def remove_html(text): #removal of the html link 
    soup=BeautifulSoup(text,'lxml')
    html_free=soup.get.text()
    return html_free

def remove_punct(text): #remove of punctuations
    no_punct="".join([c for c in text if c not in string.punctuation])
    return no_punct

df['Text']=df['Text'].apply(lambda x: remove_punct(x))

tokenizer=RegexpTokenizer(r'\w+')
df['Text']=df['Text'].apply(lambda x: tokenizer.tokenize(x.lower()))


def remove_stopwords(text):
    words=[w for w in text if w not in stopwords.words('english')]
    return words

df['Text']=df['Text'].apply(lambda x: remove_stopwords(x))

lemmatizer=WordNetLemmatizer()

def word_lemmatizer(text):
    lem_text=[lemmatizer.lemmatize(i) for i in text]
    return lem_text

df['Text']=df['Text'].apply(lambda x: word_lemmatizer(x))

#stemmer=PorterStemmer()
#def word_stemm(text):
   # stem_text=" ".join([stemmer.stem(i) for i in text])
   # return stem_text

#df['Text']=df['Text'].apply(lambda x: word_stemm(x))

df.to_csv('twitter_pleasant(after).csv')