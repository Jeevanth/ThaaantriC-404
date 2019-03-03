
import pandas as p
import numpy as np
import random

iteams={'ElectronicsAppliances':['LGTV','SamsungRefigerator','UshaIronBox','MorphyToaster'],'Fashion':['NikeShoes','Radowatch','RaybanGlasses','Garniearcream'],'ComputerAndMobile':['MacBook','OnePlus6T','IphoneXs','Dell'],'Grossaries':['WheelSoap','Turdal','Ketchup','GaramMasala']}
pname=['ElectronicsAppliances','Fashion','ComputerAndMobile','Grossaries']

notdata=p.read_csv('/Users/manthanmkulakarni/gits/Taaanthrics404/paytmfinal/NotificationDataset.csv')
notdata=np.array(notdata)
iteam=""
temp=''
for _ in range(10):
    i=random.randrange(1,98)
    iteam=iteams[notdata[i][1]][int(random.randrange(1,4))]
    
    temp=str(temp)+'&'+'Catagory: '+str(notdata[i][1])+'&'+'Product: '+str(iteam)+'&'+'Price: '+str(notdata[i][3])+'&'+'AfterDiscount: '+str(notdata[i][4])+'$'
    
print temp


