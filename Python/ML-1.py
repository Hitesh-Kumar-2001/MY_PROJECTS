import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from mpl_toolkits.mplot3d import Axes3D

# loading data in to python program
data = pd.read_csv("Problem1.txt",sep="\t")
print(data.head())


#splitting data in to train and test category
data_train , data_test = train_test_split(data,random_state=15,train_size=0.8)


#intialising data in to target and feature
X_train = np.array(data_train[data_train.columns[-4:]])
X_test = np.array(data_test[data_train.columns[-4:]])
Y_train = np.array(data_train['fruit_label'])
Y_test = np.array(data_test['fruit_label'])

#scaling data to get better accuracy
scaler = StandardScaler()
X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)


#applying knn algorithm by inbuilt functions
knn_object = neighbors.KNeighborsClassifier(n_neighbors=2)
knn_object.fit(X_train_scale,Y_train)
predictions_knn=knn_object.predict(X_test_scale)
accuracy_knn= metrics.accuracy_score(Y_test, predictions_knn) * 100


#applying LogisticRegression algorithm by inbuilt functions
logisticRegr = LogisticRegression(solver='liblinear')
logisticRegr.fit(X_train_scale, Y_train)
predictions_lr = logisticRegr.predict(X_test_scale)
accuracy_lr = (logisticRegr.score(X_test_scale, Y_test))*100


###################################### Visualisation ###############################################3

#creating subplots
fig, ax = plt.subplots(2,2)
fig.set_size_inches(15, 8)

# first plot train data visualisation according to frequency
ax[0,0].hist(Y_train, 4, width=0.5)
label = ['Apple', 'Mandarin', 'Orange', 'Lemon']
rects = ax[0,0].patches
for rect, l in zip(rects, label):
    h = rect.get_height()
    ax[0,0].text((rect.get_x() + rect.get_width()/2), h+0.02, l, ha='center', va='bottom')
ax[0,0].set_title('Fruit Distribution in Training Dataset')
ax[0,0].set_xlabel('Fruits')
ax[0,0].set_ylabel('Frequency')

#second plot train data visualisation according to their attributes
groups = data_train.groupby("fruit_name")
for name, group in groups:
    ax[0,1].plot(group["width"], group["height"], marker="o", linestyle="", label=name)
ax[0,1].set_title('Fruit Distribution according to Widht and Height')
ax[0,1].set_xlabel('Width')
ax[0,1].set_ylabel('Height')
ax[0,1].legend()

#Predictions knn
knn_correct_pred = np.where(Y_test == predictions_knn)
knn_wrong_pred = np.where(Y_test != predictions_knn)
ax[1,0].scatter(X_test[knn_correct_pred, 1], X_test[knn_correct_pred, 2], c='r', label='Correct Prediction')
ax[1,0].scatter(X_test[knn_wrong_pred, 1], X_test[knn_wrong_pred, 2], c='k', label='Wrong Prediction')
ax[1,0].set_title('Predictions by K-Nearest Neighbour Algorithm')
ax[1,0].set_xlabel('Width')
ax[1,0].set_ylabel('Height')
ax[1,0].legend()

#predictions LR
lr_correct_pred = np.where(Y_test == predictions_lr)
lr_wrong_pred = np.where(Y_test != predictions_lr)
ax[1,1].scatter(X_test[lr_correct_pred, 1], X_test[lr_correct_pred, 2], c='r', label='Correct Prediction')
ax[1,1].scatter(X_test[lr_wrong_pred, 1], X_test[lr_wrong_pred, 2], c='k', label='Wrong Prediction')
ax[1,1].set_title('Predictions by Logistic Regression Algorithm')
ax[1,1].set_xlabel('Width')
ax[1,1].set_ylabel('Height')
ax[1,1].legend()
plt.show()


print("Accuracy of KNN implementation",accuracy_knn)
print("Accuracy of Logistic Regression implementation",accuracy_lr)
if accuracy_lr > accuracy_knn:
    print("Logistic Regression gave better result")
else:
    print("KNN gave better result")

