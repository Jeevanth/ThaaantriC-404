# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:45:31 2019

@author: Nanda Krishna K S
"""
import numpy as np
import pandas as pd

dataset=pd.read_csv('DataSet.csv')
sample=dataset.iloc[0:1,4:-1].values
#x1=dataset.iloc[0:1,4:-1].values

#LabelEncoding:
from sklearn.externals import joblib
LabelEncoderGender=joblib.load('LabelEncoderGender')
sample[:,1]=LabelEncoderGender.transform(sample[:,1])
LabelEncoderPlace=joblib.load('LabelEncoderPlace')
sample[:,2]=LabelEncoderPlace.transform(sample[:,2])

#mj1=joblib.load('TrailModel1')
#x1[:,1]=labelencoderX.transform(x1[:,1])

#OneHotEncoding:
OnehotEncoderPlace=joblib.load('OneHotEncoderPlace')
sample=OnehotEncoderPlace.transform(sample).toarray()

#Predicting:
classifier=joblib.load("MLModelLogisticRegression")
prob=classifier.predict_proba(sample)
print(prob)

LabelEncoderY=joblib.load('LabelEncoderY')
result=0
prob2=prob[0].tolist()
dict1=dict(zip(prob2,range(0,4)))
QueryCategory=np.array(['Fashion'])
if LabelEncoderY.transform(QueryCategory) in list(dict1.values())[1:4]:
    result=1
print(result)