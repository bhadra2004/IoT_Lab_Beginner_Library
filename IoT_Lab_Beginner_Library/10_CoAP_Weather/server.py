import asyncio,json,requests
from aiocoap import resource,Context,Message
from aiocoap.numbers.codes import Code
class Weather(resource.Resource):
    async def render_get(self,request):
        weather=requests.get("https://api.open-meteo.com/v1/forecast",params={"latitude":9.93,"longitude":76.27,"current":"temperature_2m,relative_humidity_2m"},timeout=15).json()["current"]
        air=requests.get("https://air-quality-api.open-meteo.com/v1/air-quality",params={"latitude":9.93,"longitude":76.27,"current":"pm2_5,pm10,us_aqi"},timeout=15).json()["current"]
        data={"temperature":weather["temperature_2m"],"humidity":weather["relative_humidity_2m"],"pm2_5":air.get("pm2_5"),"pm10":air.get("pm10"),"aqi":air.get("us_aqi")}
        return Message(code=Code.CONTENT,payload=json.dumps(data).encode())
async def main():
    site=resource.Site();site.add_resource(["environment"],Weather())
    await Context.create_server_context(site,bind=("127.0.0.1",5683))
    print("CoAP weather server running");await asyncio.Future()
asyncio.run(main())
