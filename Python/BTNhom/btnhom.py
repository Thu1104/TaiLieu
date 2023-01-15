import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
#Đọc tập dữ liệu
dt = pd.read_csv("indexData.csv")
print(dt)
#Lưu các cột thuộc tính vào X, cột nhãn lưu vào Y 
#(bỏ cột Date (cột 1) trong tập dữ liệu vì không ảnh hưởng đến quá trình dực đoán) 
X = dt.iloc[:,2:8]
Y = dt.Index 

#In các nhãn có trong tập dữ liệu
print("\nNhãn: \n", np.unique(Y))
#Xác suất của từng nhãn trong tập dữ liệu
xs = Y.value_counts()/Y.count()
print("\n% từng nhãn trong tập dữ liệu: ")
print(round(xs*100,3))

#Phân chia tập dữ liệu
print("\nSử dụng nghi thức hold-out Phân chia tập dữ liệu huấn luyện") 
X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=1/3.0,random_state=3000)
#Độ dài tập dữ liệu sau khi chia
print("\nĐộ dài dữ liệu y_train = ", len(y_train))
print("Độ dài dữ liệu y_test = ", len(y_test))

#Xác suất của từng nhãn trong tập test
stage = y_test.value_counts()/y_test.count()
print("\n% từng nhãn trong tập test: ")
print(round(stage*100,3))
print("\n----------------------------------------------")

#Giải thuật Cây quyết định phân hoạch dựa trên Entropy
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 3000, max_depth=15, min_samples_leaf=10)
clf_entropy.fit(X_train, y_train)
y_pred_entropy = clf_entropy.predict(X_test)   
print("Accuracy is with Entropy = ", round(accuracy_score(y_test, y_pred_entropy)*100,3))
#Độ chính xác cho từng phân lớp của Entropy
print("Độ chính xác cho từng phân lớp của Entropy:")
cnf_matrix_gnb = confusion_matrix(y_test, y_pred_entropy)
print(cnf_matrix_gnb)
print("\n")

#Giải thuật cây quyết định phân hoạch dựa trên Gini
clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 3000, max_depth=15, min_samples_leaf=9)
clf_gini.fit(X_train, y_train)
y_pred_gini = clf_gini.predict(X_test)   
print("Accuracy is with gini = ", round(accuracy_score(y_test, y_pred_gini)*100,3))
#Độ chính xác cho từng phân lớp của Gini
print("Độ chính xác cho từng phân lớp của Gini:")
cnf_matrix_gnb = confusion_matrix(y_test, y_pred_gini)
print(cnf_matrix_gnb)
print("\n")

#Giải thuật Bayes thơ ngây
model=GaussianNB()
model.fit(X_train,y_train)
thucte= y_test
dubao=model.predict(X_test)
print ("Accuracy is with Bayes = ", round(accuracy_score(thucte,dubao)*100,3))
#Độ chính xác cho từng phân lớp của Bayes
print("Độ chính xác cho từng phân lớp của Bayes:")
cnf_matrix_gnb = confusion_matrix(thucte, dubao)
print(cnf_matrix_gnb)
print("\n")

print("\nSo sánh các giải thuật qua 10 vòng lặp:")
trungbinh1 = 0
trungbinh2 = 0
trungbinh3 = 0
for i in range (0,10):
    print("\nLần lặp thứ: " ,i+1)
    X_train, X_test, y_train, y_test = train_test_split (X, Y, test_size=1/3.0, random_state=3000)
    danhgia1 = 0
    danhgia2 = 0
    danhgia3 = 0
    for j in range (0,10):
        #Giải thuật cây quyết định phân hoạch dựa trên Entropy
        clf_entropy1 = DecisionTreeClassifier (criterion = "entropy", random_state = 3000, max_depth = 6+i, min_samples_leaf = 1+j)
        clf_entropy1.fit(X_train, y_train)        
        #Giải thuật cây quyết định phân hoạch dựa trên Gini
        clf_gini1 = DecisionTreeClassifier (criterion = "gini", random_state = 3000, max_depth = 6+i, min_samples_leaf = 1+j)
        clf_gini1.fit(X_train, y_train)  
        y_pred1 = clf_entropy1.predict(X_test)
        y_pred2 = clf_gini1.predict(X_test)
        #Giải thuật Bayes thơ ngây
        model1 = GaussianNB()
        model1.fit(X_train,y_train)
        y_pred3 = model1.predict(X_test)
        
        #Độ chính xác sau mỗi vòng lặp
        print("\nMax_depth=",6+i,";", " min_samples_leaf=",1+j)
        print ("Accuracy is Entropy: ", round(accuracy_score(y_test,y_pred1)*100,3))
        print ("Accuracy is gini: ", round(accuracy_score(y_test,y_pred2)*100,3))
        print ("Accuracy is Bayes: ", round(accuracy_score(y_test,y_pred3)*100,3))
        #Đánh giá
        danhgia1 = danhgia1 + accuracy_score(y_test,y_pred1)*100
        danhgia2 = danhgia2 + accuracy_score(y_test,y_pred2)*100
        danhgia3 = danhgia3 + accuracy_score(y_test,y_pred3)*100
        
    #In giá trị trung bình sau 10 lần lặp j
    print("\nTrung bình của Entropy ở lần lặp thứ: ",i+1,"= ",round(danhgia1/10,3))
    print("Trung bình của Gini ở lần lặp thứ: ",i+1,"= ",round(danhgia2/10,3))
    print("Trung bình của Bayes ở lần lặp thứ: ",i+1,"= ",round(danhgia3/10,3))
 
    trungbinh1 = trungbinh1 + danhgia1/10
    trungbinh2 = trungbinh2 + danhgia2/10
    trungbinh3 = trungbinh3 + danhgia3/10
    
    

#In giá trị trung bình sau 10 lần lặp i
print("\nTrung bình 10 lần lặp của Entropy: ", round(trungbinh1/10,3))
print("Trung bình 10 lần lặp của Gini: ", round(trungbinh2/10,3))
print("Trung bình 10 lần lặp của Bayes: ", round(trungbinh3/10,3))
