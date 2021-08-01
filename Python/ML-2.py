import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from mpl_toolkits.mplot3d import Axes3D

# loading data in to python program
data = pd.read_csv("Problem2.csv",sep=",")
print(data.head())


#splitting data in to train and test category
data_train , data_test = train_test_split(data,random_state=25,train_size=0.7)


#intialising data in to target and feature
X_train = np.array(data_train[data_train.columns[:7]])
X_test = np.array(data_test[data_train.columns[:7]])
Y_train = np.array(data_train['Outcome'])
Y_test = np.array(data_test['Outcome'])

#scaling data to get better accuracy
scaler = StandardScaler()
X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)




#applying LogisticRegression algorithm by inbuilt functions
logisticRegr = LogisticRegression(solver='liblinear')
logisticRegr.fit(X_train_scale, Y_train)
predictions_lr = logisticRegr.predict(X_test_scale)
accuracy_lr = (logisticRegr.score(X_test_scale, Y_test))*100


print(accuracy_lr)


###################################### Visualisation ###############################################3

# plotting and visualizing the data

fig, ax = plt.subplots(2,2)

pos = np.squeeze(np.where(Y_train == 1))
neg = np.squeeze(np.where(Y_train == 0))

x = np.array(data_train['Age'])
y = np.array(data_train['DiabetesPedigreeFunction'])
z = np.array(data_train['Glucose'])


# histogram of diabetic and non-diabetic people distributed
# on the basis of age, from training dataset

ax[0,0].hist([x[pos], x[neg]], bins=10, label=['Diabetic', 'Not Diabetic'])
ax[0,0].set_title('Distribution by Age')
ax[0,0].set_xlabel('Age')
ax[0,0].set_ylabel('Frequency')
ax[0,0].legend()


# histogram of diabetic and non-diabetic people distributed
# on the basis of DPF, from training dataset

ax[0,1].hist([y[pos], y[neg]], bins=10, label=['Diabetic', 'Not Diabetic'])
ax[0,1].set_title('Distribution by DPF')
ax[0,1].set_xlabel('Diabetes Pedigree Function (DPF)')
ax[0,1].set_ylabel('Frequency')
ax[0,1].legend()


# histogram of diabetic and non-diabetic people distributed
# on the basis of Glucose, from training dataset

ax[1,0].hist([z[pos], z[neg]], bins=10, label=['Diabetic', 'Not Diabetic'])
ax[1,0].set_title('Distribution by Glucose')
ax[1,0].set_xlabel('Glucose')
ax[1,0].set_ylabel('Frequency')
ax[1,0].legend()


# scatter plot of predictions

#predictions LR
lr_correct_pred = np.where(Y_test == predictions_lr)
lr_wrong_pred = np.where(Y_test != predictions_lr)
ax[1,1].scatter(X_test[lr_correct_pred, 1], X_test[lr_correct_pred, 2], c='r', label='Correct Prediction')
ax[1,1].scatter(X_test[lr_wrong_pred, 1], X_test[lr_wrong_pred, 2], c='k', label='Wrong Prediction')
ax[1,1].set_title('Predictions by Logistic Regression Algorithm')
ax[1,1].set_xlabel('DPF')
ax[1,1].set_ylabel('AGE')
ax[1,1].legend()
plt.show()


plt.show()