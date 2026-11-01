import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
# Download India Air Quality Data city_day.csv from Kaggle.
df=pd.read_csv("city_day.csv")
features=["PM2.5","PM10","NO2","CO","SO2","O3"]
df=df[features+["AQI_Bucket"]].dropna()
X_train,X_test,y_train,y_test=train_test_split(df[features],df["AQI_Bucket"],test_size=0.2,random_state=42,stratify=df["AQI_Bucket"])
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)
pred=model.predict(X_test)
print("Accuracy:",accuracy_score(y_test,pred))
print(classification_report(y_test,pred))
example=pd.DataFrame([[40,70,25,1,10,30]],columns=features)
print("Predicted AQI category:",model.predict(example)[0])
