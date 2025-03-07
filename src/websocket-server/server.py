import asyncio
import json
import websockets
from modules import display

async def handle_client(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        action = data.get("action")

        if action in ["set_display"]:
            await display.handle_4_digit_display(data, websocket)

async def main():
    server = await websockets.serve(handle_client, "0.0.0.0", 8765)
    print("WebSocket Server Running on ws://<RaspberryPi_IP>:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
