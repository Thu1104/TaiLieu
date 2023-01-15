#Ví dụ 1
import numpy as np
import matplotlib.pyplot as plt

#Câu a: Biểu diễn dữ liệu trên Oxy
X = np.array([1,2,4])
Y = np.array([2,3,6])

plt.axis([0,5,0,8]) #Độ lớn trục tung, trục hoành
plt.plot(X,Y,"ro",color="blue")
plt.xlabel("Giá trị thuộc tính X")
plt.ylabel("Giá trị thuộc tính Y")
plt.show()

#Câu b: Tìm hàm hồi quy
def LR1(X,Y,eta,lanlap,theta0,theta1):
    m = len(X) #Số lượng phần tử
    for k in range(0,lanlap):
        print("Lần lặp: ", k)
        for i in range(0,m):
            h_i = theta0 + theta1*X[i]
            #Tính theta0
            theta0 = theta0 + eta*(Y[i]-h_i)*1
            print("Phần tử thứ ",i, "y=",Y[i], "h=",h_i, "Giá trị theta0 = ",round(theta0,3))
            #Tính theta1
            theta1 = theta1 + eta*(Y[i]-h_i)*X[i]
            print("Phần tử thứ ",i, "Giá trị theta1 = ",round(theta1,3))
    return [round(theta0,3), round(theta1,3)]
theta = LR1(X,Y,0.2,1,0,1)
theta

#Câu c: Vẽ đường hồi quy
theta = LR1(X,Y,0.2,1,0,1) #theta 1 bước
X1= np.array([1,6])
Y1= theta[0] + theta[1]*X1

theta2 = LR1(X,Y,0.2,2,0,1) #theta 2 bước
X2= np.array([1,6])
Y2= theta2[0] + theta2[1]*X2

plt.axis([0,7,0,10])
plt.plot(X,Y,"ro",color="blue")

plt.plot(X1,Y1,color="violet") #Đường hồi quy lần lặp 1
plt.plot(X2,Y2,color="green") #Đường hồi quy lần lặp 2

plt.xlabel("Giá trị thuộc tính X")
plt.ylabel("Giá trị dự đoán Y")
plt.show()

#Câu d: Nếu thay đổi tốc độ học =0.1
theta = LR1(X,Y,0.1,1,0,1) #theta 1 bước
X1= np.array([1,6])
Y1= theta[0] + theta[1]*X1

theta2 = LR1(X,Y,0.1,2,0,1) #theta 2 bước
X2= np.array([1,6])
Y2= theta2[0] + theta2[1]*X2

plt.axis([0,7,0,10])
plt.plot(X,Y,"ro",color="blue")

plt.plot(X1,Y1,color="violet") #Đường hồi quy lần lặp 1
plt.plot(X2,Y2,color="green") #Đường hồi quy lần lặp 2

plt.xlabel("Giá trị thuộc tính X")
plt.ylabel("Giá trị dự đoán Y")
plt.show()

#Câu e: Dự báo phần tử mới tới
#Dự báo cho 3 phần tử x=0, x=3, x=5
XX = [0,3,5]
for i in range(0,3):
    YY = theta[0] + theta[1]*XX[i]
    print(round(YY,3))

#Ví dụ 2
import pandas as pd
dt = pd.read_csv("Housing_2019.csv", index_col=0)
dt.iloc[2:4,]
X = dt.iloc[:,[1,2,3,4,10]]
X.iloc[1:5,]
y=dt.price

plt.scatter(dt.lotsize, dt.price)
plt.show()

#huấn luyện mô hình
import sklearn
from sklearn import linear_model
lm = linear_model.LinearRegression()
lm.fit(X[0:520],y[0:520])

print lm.intercept
print lm.coef

#dự báo giá nhà cho 20 phần tử cuối cùng trong tập dữ liệu
y=dt.price
y_test = y[-20:]
X_test = X[-20:]
y_pred = lm.predict(X_test)

#So sánh giá trị thực tế và giá trị dự báo
y_pred
y_test

from sklearn.metrics import mean_squared_error
err = mean_squared_error(y_test, y_pred)
err
rmse_err = np.sqrt(err)
round(rmse_err,3)

#Có 5 thuộc tính
#Thuộc tính dự đoán giá nhà: lotsize, bedrooms, bathrms, stories, garagepl

