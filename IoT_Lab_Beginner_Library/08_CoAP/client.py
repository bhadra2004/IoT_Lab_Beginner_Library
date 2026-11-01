import asyncio, json
from aiocoap import Context, Message
from aiocoap.numbers.codes import Code
async def main():
    context=await Context.create_client_context()
    request=Message(code=Code.GET,uri="coap://127.0.0.1:5683/sensor")
    reply=await context.request(request).response
    print(json.loads(reply.payload.decode()))
asyncio.run(main())
