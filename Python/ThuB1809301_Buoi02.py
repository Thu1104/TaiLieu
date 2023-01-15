# Cau 3
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#3a. Đọc dữ liệu rượu vang đỏ
data = pd.read_csv("winequality-red.csv", delimiter=';')

#3b. Tính số phần tử và nhãn trong tập dữ liệu
print("Tập dữ liệu có " + str(len(data)) + " phần tử") #Có 1599 phần tử
print("Số nhãn: ",len(np.unique(data.quality))) #có 6 nhãn

#3c. Số lượng nhãn và phần tử trong tập test
X_train,X_test,y_train,y_test = train_test_split(data.iloc[:,0:11],data.iloc[:,11:12],test_size=4/10,random_state=100)
print("Số lượng phần tử trong tập test là: " + str(len(X_test))) # 640 phần tử
print("Số nhãn của các phần tử thuộc tập test: ", len(np.unique(y_test))) #6 nhãn

#3d. Xây dựng mô hình cây quyết định
clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth = 12, min_samples_leaf = 10)
clf_gini.fit(X_train, y_train)

#3e. Độ chính xác tổng thể và từng lớp cho dữ liệu tập test
y_pred = clf_gini.predict(X_test)
print("Độ chính xác tổng thể của tập test: ", accuracy_score(y_test, y_pred)*100)

#3f. Độ chính xác tổng thể và từng lớp cho 8 phần tử đầu tiên
y_pred_8 = clf_gini.predict(X_test[0:8])
print("Độ chính xác tổng thể của 8 phần tử tập test: ", accuracy_score(y_test[0:8], y_pred_8)*100)

#Cau 4
#Xây dựng mô hình dựa vào chỉ số độ lợi thông tin
X = [[180,15,0],
     [167,42,1],
     [136,35,1],
     [174,15,0],
     [141,28,1]]
Y = ['Nam','Nữ','Nữ','Nam','Nữ']
clf_gini_4 = DecisionTreeClassifier(criterion = "gini", random_state = 5, max_depth = 3, min_samples_leaf = 2)
clf_gini_4.fit(X,Y)

#Dự báo phần tử tới có thông tin chiều cao=185, độ dài mái tóc=13, giọng nói=0
y_pred_4 = clf_gini_4.predict([[185,13,0]])[0]
print("Chiều cao = 185, độ dài mái tóc = 13, giọng nói = 0. Dự báo người này là: ",y_pred_4)

