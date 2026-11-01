import asyncio, json, random
from aiocoap import resource, Context, Message
from aiocoap.numbers.codes import Code
class Sensor(resource.Resource):
    async def render_get(self, request):
        data={"temperature":round(random.uniform(27,32),2),"humidity":round(random.uniform(60,75),2)}
        return Message(code=Code.CONTENT,payload=json.dumps(data).encode())
async def main():
    site=resource.Site();site.add_resource(["sensor"],Sensor())
    await Context.create_server_context(site,bind=("127.0.0.1",5683))
    print("Serving coap://127.0.0.1:5683/sensor")
    await asyncio.Future()
asyncio.run(main())
