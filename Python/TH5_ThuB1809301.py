#Bài 1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

def my_perceptron(X, y, eta, lanlap):
    n = len(X[0, ])
    m = len(X[:, 0])
    #print("m= ",m," n= ",n)
    w0 = np.random.randn()
    w = tuple(np.random.randn(1, n)[0])
    #print(" w0= ", w0)
    #print(" w= ", w)
    for t in range(0,lanlap):
        #print("lanlap _____", t+1)
        for i in range(0,m):
            gx = w0 + sum(X[i,]*w)
            #print("gx= ",gx)
            if(gx>0):
                output = 1
            else:
                output = 0
            w0 = w0 + eta*(y[i]-output)
            w = w + eta*(y[i]-output)*X[i,]
            #print(" w0= ",w0)
            #print(" w= ",w)
    return(np.round(w0,3), np.round(w,3))
    
dt = pd.read_csv("data_per.csv")
X = dt.iloc[:, 0:-1].values
Y = dt.iloc[:, -1].values

print(my_perceptron(X, Y, 0.15, 50))
#(-13.903, array([-2.099719e+03, -8.362364e+03, -1.594000e+01, -4.600000e+00, -1.150600e+01]))


#Bài 2


iris_dt = load_iris()
X = iris_dt.data
Y = iris_dt.target
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, shuffle=True)

max_iter_arr = (5, 50, 100, 1000)
eta0_arr = (0.002, 0.02, 0.2)

for i in range(len(max_iter_arr)):
    for j in range(len(eta0_arr)):

        iter_i = max_iter_arr[i]
        eta_j = eta0_arr[j]

        net = Perceptron(max_iter=iter_i, eta0=eta_j)

        net.fit(x_train, y_train)

        y_pred = net.predict(x_test)
        print("Max_iter: ", iter_i)
        print("Eta: ", eta_j)
        print("Accuracy Score: ", accuracy_score(y_test, y_pred))
        