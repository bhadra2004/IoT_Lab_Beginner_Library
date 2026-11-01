import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score
# Download Beijing Multi-Site Air Quality dataset; place one station CSV here.
df=pd.read_csv("station.csv")
features=["PM2.5","PM10","PRES","DEWP","WSPM"]
df=df[features+["TEMP"]].dropna()
X_train,X_test,y_train,y_test=train_test_split(df[features],df["TEMP"],test_size=0.2,random_state=42)
model=LinearRegression().fit(X_train,y_train)
pred=model.predict(X_test)
print("MAE:",mean_absolute_error(y_test,pred),"R2:",r2_score(y_test,pred))
example=pd.DataFrame([[30,50,1010,12,2]],columns=features)
print("Predicted temperature:",model.predict(example)[0])
