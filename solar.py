import pandas as pd
import os
import pickle
data1 = pd.read_excel("1.xlsx")
data2 = pd.read_excel("2.xlsx")
data3 = pd.read_excel("3.xlsx")
data4 = pd.read_excel("4.xlsx")
data5 = pd.read_excel("5.xlsx")
data6 = pd.read_excel("6.xlsx")
dataset = pd.concat([data1, data2 , data3, data4, data5, data6])

data = dataset.drop(columns=['(Inverters)','(Inverter)','Unnamed: 13','Date','Random','Hour','Time','Station pressure', 'Altimeter'])

data.isna().sum()
df = data.dropna(subset = ['Solar energy'])
df.isna().sum()
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
(df< (Q1 - 1.5 * IQR)) | (df> (Q3 +1.5 * IQR))
df1 = df[~((df < (Q1 - 1.5 * IQR)) | (df> (Q3 +1.5 * IQR))).any(axis=1)]
y = df1['Solar energy']
x = df1[['Cloud coverage', 'Visibility', 'Temperature', 'Dew point','Relative humidity', 'Wind speed']]
from sklearn.model_selection import train_test_split
x_train, x_test , y_train , y_test = train_test_split(x,y,test_size=0.2)
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
print(rf.fit(x_train , y_train))
pickle.dump(rf,open('iri.pkl','wb'))