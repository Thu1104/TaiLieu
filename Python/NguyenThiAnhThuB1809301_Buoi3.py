import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#Câu 1
wineWhite = pd.read_csv("winequality-white.csv", sep=';')
print(wineWhite) 
print(wineWhite.quality)
print("Giá trị các nhãn gồm: ", np.unique(wineWhite.quality))
#Có 12 thuộc tính
#Cột quality là cột nhãn
#Có 7 nhãn gồm [3,4,5,6,7,8,9]

#Câu 2
kf = KFold(n_splits=40,shuffle=True, random_state=3000)
X = wineWhite.iloc[:,0:11]
y = wineWhite.iloc[:,11]

for train_index, test_index in kf.split(X):
    X_train, X_test = X.iloc[train_index,],X.iloc[test_index,]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
print("Số lượng phần tử trong tập test: ",len(X_test))
print("Số lượng phần tử trong tập huấn luyện: ",len(X_train))

#Câu 3
model = GaussianNB()
model.fit(X_train, y_train)
thucte = y_test
dubao = model.predict(X_test)
print("Thực tế: \n",thucte)
print("Dự báo: \n",dubao)

#Câu 4
total_acc = 0
for train_index, test_index in kf.split(X):
    X_train, X_test = X.iloc[train_index,],X.iloc[test_index,]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    model = GaussianNB()
    model.fit(X_train, y_train)
    thucte = y_test
    dubao = model.predict(X_test)
    print("Dự báo: ", dubao)
    lb = np.unique(dubao)
    print(lb)
    cnf_matrix_gnb = confusion_matrix(thucte, dubao, labels=lb)
    print(cnf_matrix_gnb) 
    '''Độ chính xác cho từng phân lớp của lần lặp cuối: [[ 1   0  0  0]
                                                     [ 0  14  8  6]
                                                     [ 0  11 23 21]
                                                     [ 0   9  5 20]'''

#Câu 5
total_acc = 0
for train_index, test_index in kf.split(X):
    X_train, X_test = X.iloc[train_index,],X.iloc[test_index,]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    model = GaussianNB()
    model.fit(X_train, y_train)
    thucte = y_test
    dubao = model.predict(X_test)
    total_acc = total_acc + accuracy_score(y_test, dubao)
    print("Độ chính xác tổng thể: ",total_acc) 

print("Độ chính xác tổng thể trung bình: ", total_acc/40)

#Câu 6
clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=8, min_samples_leaf=7)
model = GaussianNB()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3.0,random_state=100)
clf_gini.fit(X_train,y_train)
y_pred_tree = clf_gini.predict(X_test)
print("Accuracy DT is: ",accuracy_score(y_test,y_pred_tree)*100)
model.fit(X_train,y_train)
dubao = model.predict(X_test)
print("Accuracy bayes is: ",accuracy_score(y_test,dubao)*100)

for i in range(1,5):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3.0,random_state=100)
    #clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=8, min_samples_leaf=7)
    clf_gini.fit(X_train,y_train)
    y_pred_tree = clf_gini.predict(X_test)
    print("Accuracy DT is: ",accuracy_score(y_test,y_pred_tree)*100)
    #model = GaussianNB()
    model.fit(X_train,y_train)
    dubao = model.predict(X_test)
    print("Accuracy bayes is: ",accuracy_score(y_test,dubao)*100)