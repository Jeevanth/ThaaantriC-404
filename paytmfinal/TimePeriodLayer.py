import pandas as pd
import numpy as np

      #Importing DataSet
dataset = pd.read_csv("DataSetnanda.csv")
X=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values
      #LabelEncoder and OneHotEncoder
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.externals import joblib
labelencoder=LabelEncoder()
X[:,1]=labelencoder.fit_transform(X[:,1])
joblib.dump(labelencoder,'LabelEncoderCategories')
      
onehotencoder=OneHotEncoder(categorical_features=[-2])
X=onehotencoder.fit_transform(X).toarray()
joblib.dump(onehotencoder,'OneHotEncoderCategories')

      #Spliting:
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.25,random_state=1348882)
            
      #MLModel Training:
from sklearn.neighbors import KNeighborsClassifier 
knn = KNeighborsClassifier(n_neighbors = 3).fit(X_train, Y_train) 
joblib.dump(knn,'MLModelKNN')
x=np.asarray([0,0,0,0,1,25]).reshape(1,-1)
print(knn.predict_proba(x))
"""Score is .78,.72,.74,.75,.8,.71,.81,.78"""
