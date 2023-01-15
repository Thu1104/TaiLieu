import pandas as pd
dt = pd.read_csv("play_tennis.csv",delimiter=',' )
dt.head()
dt.tail(7)

dt.loc[3:8]
dt.iloc[:,3:6]
dt.iloc[5:10,3:4]
dt.Outlook

print(dt.head())
