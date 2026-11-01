import requests,pandas as pd,matplotlib.pyplot as plt
url="https://api.open-meteo.com/v1/forecast"
data=requests.get(url,params={"latitude":9.93,"longitude":76.27,"hourly":"temperature_2m,relative_humidity_2m","forecast_days":2},timeout=20).json()["hourly"]
df=pd.DataFrame(data);df.to_csv("weather.csv",index=False)
print(df[["temperature_2m","relative_humidity_2m"]].describe())
df.head(24).plot(x="time",y=["temperature_2m","relative_humidity_2m"],kind="bar",title="Weather readings")
plt.tight_layout();plt.show()
