import numpy as np
import pandas as pd

#1 Nguyen ly hoat dong cua Bayes
#Buoc1

#dt = pd.read_csv("play_tennis_F.csv")
dt = pd.read_csv("play_tennis.csv")
dt
dt.shape
dtP = dt.Outlook
PlayYes = dt[dt.Play=="Yes"]
PlayYes.Outlook
#..
dtOy = dt.Outlook[dt.Play=="Yes"]
dtOy.value_counts()
dtOy.count()

dtOy = dt.Outlook[dt.Play=="Yes"]
P1_1 = dtOy.value_counts()/dtOy.count()
dtOn = dt.Outlook[dt.Play=="No"]
P1_2 = dtOn.value_counts()/dtOn.count()
P1_1
P1_2

dtTy = dt.Temp[dt.Play=="Yes"]
P2_1 = dtTy.value_counts()/dtTy.count()
dtTn = dt.Temp[dt.Play=="No"]
P2_2 = dtTn.value_counts()/dtTn.count()
P2_1
P2_2

dtHy = dt.Humidity[dt.Play=="Yes"]
P3_1 = dtHy.value_counts()/dtHy.count()
dtHn = dt.Humidity[dt.Play=="No"]
P3_2 = dtHn.value_counts()/dtHn.count()
P3_1
P3_2

dtWy = dt.Windy[dt.Play=="Yes"]
P4_1 = dtWy.value_counts()/dtWy.count()
dtWn = dt.Windy[dt.Play=="No"]
P4_2 = dtWn.value_counts()/dtWn.count()
P4_1
P4_2

Play = dt.Play.value_counts()/dt.Play.count()
Play

#Buoc 2
P_yes = P1_1[1]*P2_1[1]*P3_1[1]*P4_1[0]*Play[0]
P_no = P1_2[1]*P2_2[1]*P3_2[1]*P4_2[0]*Play[1]

#Hoac

P_yes = P1_1["Rainy"]*P2_1["Cool"]*P3_1["High"]*P4_1[False]*Play["Yes"]
P_no = P1_2["Rainy"]*P2_2["Cool"]*P3_2["High"]*P4_2[False]*Play["No"]

P_yes
P_no
PY = P_yes/(P_no+P_yes)
PN = P_no/(P_no+P_yes)
PY
PN

#2 Su dung thu vien scikit-learn