def MarketBasedPredictionDataLoading(iteamId):
	import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt


	dataset=np.array(pd.read_csv('/Users/manthanmkulakarni/gits/Taaanthrics404/paytmfinal/distancegeneral.csv'))
    iteams=['LGTV','SamsungRefigerator','UshaIronBox','MorphyToaster','NikeShoes','Radowatch','RaybanGlasses','Garniearcream','MacBook','OnePlus6T','IphoneXs','Dell','WheelSoap','Turdal','Ketchup','GaramMasala']
	iteams=np.array(iteams)
	pname=['ElectronicsAppliances','Fashion','ComputerAndMobile','Grossaries']
	pname=np.array(pname)
    distancegeneral=np.array(dataset)
	

	#predicting the associated products
	for i in range(iteams.shape[0]):
		median=np.median(distancetable[i])/2
		print "If product "+str(iteams[i])+ "is choosen then other similar products which might be choosen are"

	string=""
	for l in range(iteamId.shape[0]):
		median=np.median(distancetable[l])*2
		for j in range(iteams.shape[0]):
		    if(distancetable[iteamId[l]][j]>median):
		        string=string+str(" ")+str(iteams[j])
		#print ("Based On users market basket analysis "+string+"\n")

	
		        
	#if response id negative decrease the value by .15 time else increase the value by .15 times

	return(string)"""


