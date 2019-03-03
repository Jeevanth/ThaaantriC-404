# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 02:33:18 2019

@author: ankita1999
"""

  # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


#importing libraries
import pandas as pd
import numpy as np
import random
import datetime

#importing dataset
dataset=pd.read_csv('Book1.csv')

#datafreme
df=pd.DataFrame(dataset[0:10])

dates=[]

#taking today's date
d=datetime.date.today()

#random generation of purchase date and warranty
for i in range(0,10):
    dates.insert(i,(d-datetime.timedelta(days=random.randrange(0,2*365))))
df['Purchased date']=dates
df['Warranty']=[12,24,12,12,1,24,12,1,12,12]

df.to_csv('Book3.csv')

#function to check whether to send notification or not based on warranty
def  expirycheck(noti):
     noti=2
     data1=pd.read_csv('Book3.csv')
     index=data1.index[data1['Notificationid']==noti]
     purchase=data1.loc[index,'Purchased date'].values
     warranty=data1.loc[index,'Warranty']
     expiry=(purchase+datetime.timedelta(days=int(warranty)*30))
     tday=(datetime.date.today())
     print(expiry)
     print(index)
     if(expiry <= tday):
        print('1')
     else:
        print('0')
    
#function call
expirycheck(2)

"""













     noti=2
     data1=pd.read_csv('Book3.csv')
     index=data1.index[data1['Notificationid']==noti]
     purchase=(data1.loc[index,'Purchased date'].values).tolist()[0]
     #p='2018-09-13'
     #p=np.array([(datetime.date(datetime.strptime(p,'%Y-%m-%d')))])
     from datetime import datetime
     from dateutil.parser import parse
     purchase=np.array([(datetime.date(datetime.strptime(purchase,'%Y-%m-%d')))])
     warranty=data1.loc[index,'Warranty']
     import datetime
     expiry=(purchase+datetime.timedelta(days=int(warranty)*30))
     tday=(datetime.date.today())
     print(expiry)
     print(index)
     if(expiry <= tday):
        print('1')
     else:
        print('0')
    
    
    
    
    
    
    
    
   """  noti=2
     index=df.index[df['Notificationid']==noti]
     purchase=df.loc[index,'Purchased date'].values
     warranty=df.loc[index,'Warranty']
     expiry=(purchase+datetime.timedelta(days=int(warranty)*30))
     tday=(datetime.date.today())
     print(expiry)
     print(index)
     if(expiry <= tday):
        print('1')
     else:
        print('0')
        """
    