import csv,time,requests
import pandas as pd
import matplotlib.pyplot as plt
rows=[]
for i in range(10):  # Change to 100 for the full lab task
    data=requests.get("http://api.open-notify.org/iss-now.json",timeout=15).json()["iss_position"]
    rows.append([pd.Timestamp.now().isoformat(),float(data["latitude"]),float(data["longitude"])])
    print("Reading",i+1,rows[-1]);time.sleep(5)
with open("iss_location.csv","w",newline="") as f:
    w=csv.writer(f);w.writerow(["Time","Latitude","Longitude"]);w.writerows(rows)
df=pd.read_csv("iss_location.csv")
print(df[["Latitude","Longitude"]].describe())
df[["Latitude","Longitude"]].plot(title="ISS location samples")
plt.show()
