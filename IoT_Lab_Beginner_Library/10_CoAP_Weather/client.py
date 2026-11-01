import asyncio,json
from aiocoap import Context,Message
from aiocoap.numbers.codes import Code
async def main():
    c=await Context.create_client_context()
    response=await c.request(Message(code=Code.GET,uri="coap://127.0.0.1:5683/environment")).response
    print(json.dumps(json.loads(response.payload.decode()),indent=2))
asyncio.run(main())
