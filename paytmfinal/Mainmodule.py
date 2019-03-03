import WishlistFiltering as wm
import UserBehaviourBasedPrediction as usbbpm
import AgeandRegionBasedPrediction as arbpm
import MarketbasketAnalysis as mbam
import UserBasedTimeSlotPrediction as ubtspm
import PredictingModel as pm

import TimeLayerPrediction as tlp
import TimeSlotOnAge as tsam
import ExpiryDate as expd
import json




#firebase = firebase.FirebaseApplication('https://final-bb89d.firebaseio.com/message', None)

config = json.loads(open('userresponce.json').read())



#Users details

notId=4
userUniqueId=int(config["userid"])
age=int(config["userage"])
regionid=int(config["userregion"])
Usergender=1 #male
g=['M','F']

#print("User ID: "+str(userUniqueId)+"\nAge: "+str(age)+"\nRegion Id: "+str(regionid)+"\nUseragender: "+str(g[Usergender-1]))

iteams=['LGTV','SamsungRefigerator','UshaIronBox','MorphyToaster','NikeShoes','Radowatch','RaybanGlasses','Garniearcream','MacBook','OnePlus6T','IphoneXs','Dell','WheelSoap','Turdal','Ketchup','GaramMasala']
pname=['ElectronicsAppliances','Fashion','ComputerAndMobile','Grossaries']
#iteamdict={'LGTV':1,'SamsungRefigerator':2,'UshaIronBox':3,'MorphyToaster':4,'NikeShoes':5,'Radowatch':6,'RaybanGlasses':7,'Garniearcream':8,'MacBook':9,'OnePlus6T':10,'IphoneXs':11,'Dell':12,'WheelSoap':13,'Turdal':14,'Ketchup':15,'GaramMasala':16}

str0=pname[pm.generalprediction(userUniqueId)]

str1=arbpm.RegionAndAgeBasedGeneralPrediction(age,720,regionid) # parameters are age , usagetime , regionid



top2UsersPrediction=usbbpm.IndivisualUserBasedProductPrediction(userUniqueId)



str3=mbam.MarketBasedPrediction(top2UsersPrediction[0])   #only users intrested products id are sent for basket analysis

str4=wm.PotentialIteamsInWishlist(3)


str5=tsam.TimeSlotBasedOnAge(age,Usergender)

str6=ubtspm.UserBasedTimeSlot(userUniqueId)
str7=tlp.parent(userUniqueId)
str8=expd.getExpiry(notId)





#print (str8)
print("Notification 1: "+"&"+top2UsersPrediction[1]+"&"+'Notification Time: '+str(int(int(str5)/60))+':'+str(int(str5)%60)+"$"+'Notification 2: '+"&"+top2UsersPrediction[2]+"&"+str3+"&"+str4[0]+"&"+str4[1]+"&"+'Notification Time: '+str(int(int(str6)/60))+':'+str(int(str6)%60))




# a Python object (dict):


datafile=open('datatest.json','w')
datafile.write("data='")
datafile.close()
x = {
  "regionbasedproduct": str1[0],
  "agebasedproduct": str1[1],
  "userbehaviourbased1": top2UsersPrediction[1],
  "userbehaviourbased1": top2UsersPrediction[2],
  "marketbaseket":str3,
  "wishlist1":str4[0],
  "wishlist2":str4[1],
  "timeonage":(int(str5)/60+int(str5)%60),
  "timeonuser":(int(str6)/60+int(str5)%60)
}

notificationdatfile=open('/Users/manthanmkulakarni/gits/Taaanthrics404/paytmfinal/notificationjsondata/notification'+str(userUniqueId)+'.json', 'w')
notificationdatfile.write("data='")
notificationdatfile.close()
# convert into JSON:
string=[x]


y = json.dumps(x)
with open('/Users/manthanmkulakarni/gits/Taaanthrics404/paytmfinal/notificationjsondata/notification'+str(userUniqueId)+'.json', 'a') as outfile:  
    json.dump(string, outfile)

datafile=open('/Users/manthanmkulakarni/gits/Taaanthrics404/paytmfinal/notificationjsondata/notification'+str(userUniqueId)+'.json','a')
datafile.write("';")
datafile.close()
datafile=open('/Users/manthanmkulakarni/gits/Taaanthrics404/paytmfinal/notificationjsondata/notification'+str(userUniqueId)+'.json','r')
filedata=datafile.read()
#print filedata
datafile.close()
