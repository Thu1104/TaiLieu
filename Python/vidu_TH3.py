#Sử dụng pandas
import pandas as pd
dt = pd.read_csv("play_tennis.csv")
dt

#Outlook
dtOy = dt.Outlook[dt.Play=="Yes"]
P1_1 = dtOy.value_counts()/dtOy.count()
dtOn = dt.Outlook[dt.Play=="No"]
P1_2 = dtOn.value_counts()/dtOn.count()
P1_1
P1_2

#Temperature
dtTy = dt.Temp[dt.Play=="Yes"]
P2_1 = dtTy.value_counts()/dtTy.count()
dtTn = dt.Temp[dt.Play=="No"]
P2_2 = dtTn.value_counts()/dtTn.count()
P2_1
P2_2

#Humidity
dtHy = dt.Humidity[dt.Play=="Yes"]
P3_1 = dtHy.value_counts()/dtHy.count()
dtHn = dt.Humidity[dt.Play=="No"]
P3_2 = dtHn.value_counts()/dtHn.count()
P3_1
P3_2

#Windy
dtWy = dt.Windy[dt.Play=="Yes"]
P4_1 = dtWy.value_counts()/dtWy.count()
dtWn = dt.Windy[dt.Play=="No"]
P4_2 = dtWn.value_counts()/dtWn.count()
P4_1
P4_2

#Play
Play = dt.Play.value_counts()/dt.Play.count()
Play

#Dự báo nhãn
P_yes = P1_1[1]*P2_1[1]*P3_1[1]*P4_1[0]*Play[0]
P_no = P1_2[1]*P2_2[1]*P3_2[1]*P4_2[0]*Play[1]
P_yes
P_no
PY = P_yes/(P_no + P_yes)
PN = P_no/(P_no + P_yes)
PY
PN

#Sử dụng scikit-learn
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
iris = datasets.load_iris()
X = iris.data
y = iris.target

#Phân chia dữ liệu
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
#Xây dựng mô hình dựa trên phân phối xác suất theo Gaussian
model = GaussianNB()
model.fit(X_train, y_train)
print(model)

#Dự đoán
thucte = y_test
dubao = model.predict(X_test)
thucte
dubao

cnf_matrix_gnb = confusion_matrix(thucte, dubao)
print(cnf_matrix_gnb)