import requests,pandas as pd,matplotlib.pyplot as plt
from datetime import datetime,timedelta,timezone
end=datetime.now(timezone.utc).date();start=end-timedelta(weeks=7)
url="https://earthquake.usgs.gov/fdsnws/event/1/query"
data=requests.get(url,params={"format":"geojson","starttime":start.isoformat(),"endtime":end.isoformat(),"minmagnitude":4},timeout=45).json()
rows=[]
for item in data["features"]:
    p=item["properties"];lon,lat,depth=item["geometry"]["coordinates"]
    rows.append({"Magnitude":p["mag"],"Place":p["place"],"Time":pd.to_datetime(p["time"],unit="ms",utc=True),"Longitude":lon,"Latitude":lat,"Depth":depth,"Tsunami":p["tsunami"]})
df=pd.DataFrame(rows);df.to_csv("earthquakes.csv",index=False)
if not df.empty:
    print(df.describe(numeric_only=True));df.set_index("Time").resample("D").size().plot(title="Earthquakes per day");plt.show()
else: print("No results")
