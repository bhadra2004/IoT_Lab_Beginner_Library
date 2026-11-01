import requests,pandas as pd,matplotlib.pyplot as plt
url="https://air-quality-api.open-meteo.com/v1/air-quality"
data=requests.get(url,params={"latitude":9.93,"longitude":76.27,"hourly":"pm10,pm2_5,us_aqi","timezone":"Asia/Kolkata"},timeout=20).json()["hourly"]
df=pd.DataFrame(data);df.to_csv("air_quality.csv",index=False)
print(df[["pm10","pm2_5","us_aqi"]].describe())
df.plot(x="time",y=["pm10","pm2_5","us_aqi"],title="Kochi air quality")
plt.tight_layout();plt.show()
