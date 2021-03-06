# -*- coding: utf-8 -*-
"""loan approval prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RCr4RL7xEkYxugZbuZtKwfDSFVOqWYXP

Importing the Dependencies
"""

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

"""Loading Data and Processing of data

"""

# loading the dataset to pandas DataFrame
df = pd.read_csv('train.csv')# number of rows and columns

type(df)

# printing the first 5 rows of the dataframe
df.head()

#printing the entire dataset
print(df)

df.columns

# number of rows and columns
df.shape

# statistical measures
df.describe()

# number of missing values in each column
df.isnull().sum()

#visualize the missing null values using heat map
sns.heatmap(df.isnull(),cbar=False)

#count the missing values for each feature
df.isnull().sum()

#To drop the missing values
df=df.dropna()

#count the missing values for each feature
df.isnull().sum()

sns.heatmap(df.isnull(),cbar=False)

# label encoding
df.replace({"Loan_Status":{'N':0,'Y':1}},inplace=True)

# Dependent column values
df['Dependents'].value_counts()

# replacing the value of 3+ to 4
df = df.replace(to_replace='3+', value=4)

# Dependent column values
df['Dependents'].value_counts()

# convert categorical columns to numerical values
df.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},
                      'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)

"""**Data Visualization**"""

fig,ax=plt.subplots(2,4,figsize=(16,10))
sns.countplot(x='Loan_Status',data=df,ax=ax[0][0])
sns.countplot(x='Gender',data=df,ax=ax[0][1])
sns.countplot(x='Married',data=df,ax=ax[0][2])
sns.countplot(x='Education',data=df,ax=ax[0][3])
sns.countplot(x='Self_Employed',data=df,ax=ax[1][0])
sns.countplot(x='Property_Area',data=df,ax=ax[1][1])
sns.countplot(x='Credit_History',data=df,ax=ax[1][2])
sns.countplot(x='Dependents',data=df,ax=ax[1][3])

df["LoanAmount"].hist(color='red',bins=50)

sns.boxplot(x="Loan_Status",y="ApplicantIncome",data=df)

sns.boxplot(x="Loan_Status",y="CoapplicantIncome",data=df)

sns.boxplot(x="Gender",y="LoanAmount",data=df)

sns.catplot(x="Gender",y="LoanAmount",data=df,hue="Loan_Status",col="Married")

sns.catplot(x="Gender",y="CoapplicantIncome",data=df,hue="Loan_Status",col="Property_Area")

#Correlation matrix
plt.figure(figsize=(10,10))
correlation_matrix=df.corr()
sns.heatmap(correlation_matrix,annot=True)
plt.show

# separating the data and label
X =df.drop(columns=['Loan_ID','Loan_Status'],axis=1)
Y = df['Loan_Status']

print(X)
print(Y)

"""**Train Test Split**"""

X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.1,random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""**Logistic Regression**"""

from sklearn.linear_model import LogisticRegression  
classifier= LogisticRegression()  
classifier.fit(X_train, Y_train)

#Predicting the test set result  
y_pred= classifier.predict(X_test)

accuracy=accuracy_score(y_pred,Y_test)*100
print("The accuracy of the model is:",accuracy)