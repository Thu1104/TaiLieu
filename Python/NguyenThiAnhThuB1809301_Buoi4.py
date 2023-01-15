#Bài tập 1
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

dt = pd.read_csv("Housing_2019.csv", index_col=0)
X = dt.iloc[:,[1,2,4,10]]
Y=dt.price

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=1/3.0,random_state=100)
len(X_train) #364

lm = linear_model.LinearRegression()
lm.fit(X_train,y_train)

print(lm.intercept_)
print(lm.coef_)

Y_pred = lm.predict(X_test)

err = mean_squared_error(y_test, Y_pred)
err
np.sqrt(err)

#Bài tập 2
import numpy as np
import matplotlib.pyplot as plt

X = np.array([1,2,4])
Y = np.array([2,3,6])

#Tìm hàm hồi quy
def LR2(X,Y,eta,lanlap,theta0,theta1):
    m = len(X) #Số lượng phần tử
    for k in range(0,lanlap):
        print("Lần lặp: ", k)
        h_x1 = 0
        h_x2 = 0
        for i in range(0,m):
            h_i = theta0 + theta1*X[i]
            h_x1 = h_x1 + (Y[i] - h_i)*1
            h_x2 = h_x2 + (Y[i] - h_i)*X[i]
        #Tính theta0
        theta0 = theta0 + eta*h_x1
        print("Giá trị theta0 = ",round(theta0,3))
        #Tính theta1
        theta1 = theta1 + eta*h_x2
        print("Giá trị theta1 = ",round(theta1,3))
    return [round(theta0,3), round(theta1,3)]
theta = LR2(X,Y,0.2,2,0,1)
theta

#Dự báo giá trị
XX = [0,3,5]
for i in range(0,3):
    YY = theta[0] + theta[1]*XX[i]
    print(round(YY,3))
    
#So sánh: giải thuật LR1 tốt hơn LR2 vì LR1 cho kết quả là số dương