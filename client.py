import asyncio
import websockets

async def teste(msg):
    async with websockets.connect('ws://localhost:8000') as websocket:
        await websocket.send(msg)
        response = await websocket.recv()
        print(response)
    
async def receive_msg():
    msg = input("Entre com a mensagem:\n")
    await teste(msg)
    # asyncio.get_event_loop().run_until_complete(teste(msg))
    
async def main():
    while True:
        await receive_msg()

asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_forever()