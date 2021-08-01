# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SX0GfmsQkZbOvcveZ7mjdT0GX7guWiv9
"""

#Description: Movie recommnendation model

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

from google.colab import files
uploaded = files.upload()

df = pd.read_excel('Amazon - Movies and TV Ratings.xlsx')
df.head()

df.shape

columns = ['user_id','Movie1','Movie2','Movie3','Movie4','Movie5']

df[columns].head()

df[columns].isnull().values.any()

def get_rating(data):
  rating = []
  for i in range(0, data.shape[0]):
    rating.append(data['Movie1'][i]+' '+data['Movie2'][i]+' '+data['Movie3'][i]+' '+data['Movie4'][i]+' '+data['Movie5'][i])
    return rating

cm = CountVectorizer().fit_transform(df['rating'])

cs = cosine_similarity(cm)
print(cs)