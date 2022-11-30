import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score


dataCoord = pd.read_csv("C:/Users/lucie/Downloads/digit_file.csv")
print(dataCoord)
#x corresponds to all the coordinates, our data
#.iloc[all the rows, the column starting at x0 to z20]
x = dataCoord.iloc[:,2:65]
print(x)
#y corresponds to the label : the different digits
y = dataCoord.iloc[:,1]
print(y)

#---------------Tests and Train part-----------------#
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3, random_state=0) #test size = 30%
sc = StandardScaler()
xTrain = sc.fit_transform(xTrain)
xTest = sc.fit_transform(xTest)
classifier = RandomForestClassifier(n_estimators=20, random_state=0)#20 decision trees
classifier.fit(xTrain, yTrain)
yPrediction = classifier.predict(xTest)

#------------------------Accuracy----------------------------#
print(classification_report(yTest, yPrediction))
print(accuracy_score(yTest, yPrediction))