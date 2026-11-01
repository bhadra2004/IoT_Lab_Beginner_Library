import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
# Download UCI Occupancy Detection dataset and put datatraining.txt in this folder.
df=pd.read_csv("datatraining.txt")
features=["Temperature","Humidity","Light","CO2"]
X=df[features];y=df["Occupancy"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
model=DecisionTreeClassifier(max_depth=4,random_state=42)
model.fit(X_train,y_train)
pred=model.predict(X_test)
print("Accuracy:",accuracy_score(y_test,pred))
print("Confusion matrix:",confusion_matrix(y_test,pred))
print("Example prediction:",model.predict([[23,30,500,600]]))
