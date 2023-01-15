from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

wineWhite = pd.read_csv("winequality-white.csv",delimiter=";")
print(wineWhite)
print(len(wineWhite))
print(np.unique(wineWhite.quality))
#Co 12 thuoc tinh 7 nhan gom [3,4,5,6,7,8,9]

X = wineWhite.iloc[:,0:11]
y = wineWhite.quality

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=100)
kf= KFold(n_splits=100,shuffle=True)


#Cau 2
for train_index, test_index in kf.split(X):
    X_train, X_test = X.iloc[train_index,],X.iloc[test_index,]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
print(len(X_test))
print(len(X_train))

#Cau 3
model = GaussianNB()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print(y_pred)

#Cau 4
for train_index, test_index in kf.split(X):
    X_train, X_test = X.iloc[train_index,],X.iloc[test_index,]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    #print(X_test)
    model = GaussianNB()
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    cnf = confusion_matrix(y_test,y_pred)
print(cnf)

#Cau 5
ac = 0
for train_index, test_index in kf.split(X):
    X_train, X_test = X.iloc[train_index,],X.iloc[test_index,]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    #print(X_test)
    model = GaussianNB()
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    print("Do chinh xác cua mo hinh voi nghi thuc kiem tra kFold: %.3f" %accuracy_score(y_test, y_pred))
    ac = ac + accuracy_score(y_test, y_pred)
print(ac/80)

#Cau 6
from sklearn.tree import DecisionTreeClassifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=100)
clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=8, min_samples_leaf=7)
clf_gini.fit(X_train,y_train)
y_pred_tree = clf_gini.predict(X_test)
print(accuracy_score(y_test,y_pred_tree)*100)
model = GaussianNB()
model.fit(X_train,y_train)
y_pred_bayes= model.predict(X_test)
print(accuracy_score(y_test,y_pred_bayes)*100)
for i in range(1,5):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=100)
    clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=8, min_samples_leaf=7)
    clf_gini.fit(X_train,y_train)
    y_pred_tree = clf_gini.predict(X_test)
    print(accuracy_score(y_test,y_pred_tree)*100)
    model = GaussianNB()
    model.fit(X_train,y_train)
    y_pred_bayes= model.predict(X_test)
    print(accuracy_score(y_test,y_pred_bayes)*100)






















