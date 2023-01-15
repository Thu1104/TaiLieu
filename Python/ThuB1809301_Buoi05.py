#1. Dữ liệu khả tách tuyến tính
import numpy as np
import matplotlib.pyplot as plt

#Dữ liệu huấn luyện
X = np.array([[0,0,1,1],[0,1,0,1]])
X
X=X.T

X1 = np.array([[0,0],[0,1],[1,0],[1,1]])
X1

Y = np.array([0,0,0,1])
Y

#Biểu diễn dữ liệu để kiểm tra dữ liệu có khả tách hay không
colormap = np.array(['red','green'])
plt.axis([0,1.5,0,2])
plt.scatter(X[:,0],X[:,1], c=colormap[Y],s=150)
plt.xlabel("Giá trị thuộc tính X1")
plt.ylabel("Giá trị thuộc tính X2")
plt.show()

#Cập nhật các trọng số w0,w1,w2
def my_perceptron(X, y, eta, lanlap):
    n = len(X[0,])
    m = len(X[:,0])
    print("m= ",m," n= ",n)
    w0 = -0.2
    w = (0.5,0.5)
    print(" w0= ", w0)
    print(" w= ", w)
    for t in range(0,lanlap):
        print("lanlap _____", t+1)
        for i in range(0,m):
            gx = w0 + sum(X[i,]*w)
            print("gx= ",gx)
            if(gx>0):
                output = 1
            else:
                output = 0
            w0 = w0 + eta*(y[i]-output)
            w = w + eta*(y[i]-output)*X[i,]
            print(" w0= ",w0)
            print(" w= ",w)
    return(np.round(w0,3), np.round(w,3))

my_perceptron(X, Y, 0.15, 2)

#2. Dữ liệu không khả tách tuyến tính
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron

dt = pd.read_csv("data_per.csv")
dt
X = dt.iloc[:,0:4]
Y = dt.Y
X
Y
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=1/3.0,random_state=100)

net = Perceptron()
net.fit(X_train, y_train)
print(net)
net.coef_ #Trọng số thuộc tính
net.intercept_ # Trọng số w0
net.n_iter_ # số lần lặp