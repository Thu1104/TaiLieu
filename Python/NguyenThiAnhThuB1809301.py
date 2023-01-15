import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

#Cau1: doc file tu du lieu
data = pd.read_csv("baitap1.csv",delimiter=',' )

#Cau2: Hien thi du lieu vua doc
print("Dữ liệu có trong file là: ")
print(data)

#Cau3: Hien thi tat ca du lieu cot so 2
print("Tất cả các dữ liệu cột số 2: ")
print(data.iloc[:,1:2])

#Cau4: Hien thi du lieu tu dong 15 den dong 30
print("Dữ liệu từ dòng 15 đến dòng 30 trong file là: ")
print(data.loc[13:28])

#Cau5: Hien thi du lieu cot 2,3 cua dong 5
print("Dữ liệu cột 2,3 của dòng 5: ")
print(data.iloc[3,1:3])

#Cau6: Bieu dien du lieu tren mat phang toa do
x = data.iloc[:,1]
y = data.iloc[:,2]
plt.scatter(x, y)
plt.title("Biểu diễn dữ liệu cột 2 và cột 3 lên hệ trục Oxy")
plt.xlabel("Tuoi")
plt.ylabel("Can Nang")
plt.autoscale(tight=True)
plt.grid()
plt.show()

#Cau7: Dung vong lap for de in ra cac so chan tu 2 den 50
print ("Các số chẵn từ 2 đến 50 là: ")
for i in range(2,51):
    if i%2 ==0:
        print (i )