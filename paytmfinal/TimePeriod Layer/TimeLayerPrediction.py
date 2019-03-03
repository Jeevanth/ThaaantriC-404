import os
import time

def child(t):
   time.sleep(t)
   print('\nA new child ',  os.getpid())
   os._exit(0)  

def parent():#Parameter Time Period and Discount Price
   while True:
      newpid = os.fork()
      import pandas as pd
      import numpy as np
      from sklearn.externals import joblib
      #Importing DataSet
      dataset = pd.read_csv("DataSet.csv")
      sample=dataset.iloc[1:2,1:-1].values
      labelencoder=joblib.load('LabelEncoderCategories')
      sample[:,1]=labelencoder.transform(sample[:,1])
      
      onehotencoder=joblib.load('OneHotEncoderCategories')
      sample=onehotencoder.transform(sample).toarray()

      
      #Best Period Prediction:
      knn=joblib.load('MLModelKNN')
      tp=[]
      for i in range(1,11):
          tp.append(knn.predict(np.asarray([0,0,0,0,i,25]).reshape(1,-1)).tolist())
      tp1=[x for i in tp for x in i]
      dict2=dict(zip(range(1,11),tp1))
      dict2=sorted(dict2.items(), key=lambda kv: kv[1])


      from datetime import datetime  
      from datetime import timedelta  
      today_block=int(datetime.now().day)//3
      popular_block=dict2[-1][0]
      if(popular_block<today_block):
          popular_block+=10
      Waiting_block=popular_block-today_block
      print(Waiting_block)
      print((datetime.now()+timedelta(days=Waiting_block*3)).date())
      #time=(int((datetime.now()+timedelta(days=Waiting_block*3)).day))*60*60*24
      time=10#Since we cannot wait for many days,i have taken time as 10.Actual time formula is as above. 
      if(newpid==0):
          child(time)
      break
       
parent()