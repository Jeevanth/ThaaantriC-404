def getExpiry(notid):
     import pandas as pd
     import numpy as np
 
     
     
     data1=pd.read_csv('Book3.csv')
     index=data1.index[data1['Notificationid']==notid]
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
     #print(expiry)
     #print(index)
     if(expiry <= tday):
        return(1)
     else:
        return(0)
    
    
    
    
    
    
    
  