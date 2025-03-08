import asyncio
import json
import websockets
import logging
from modules import display

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

async def handle_client(websocket):
    logging.info(f"New WebSocket connection from: {websocket.remote_address}")

    try:
        async for message in websocket:
            logging.debug(f"Received message: {message}")
            data = json.loads(message)
            action = data.get("action")

            if action == "set_display":
                value = data.get("value", "0000")
                logging.info(f"Setting display to: {value}")
                await display.handle_4_digit_display(data, websocket)
            else:
                logging.warning(f"Unknown action received: {action}")

    except websockets.exceptions.ConnectionClosed as e:
        logging.warning(f"Connection closed: {e}")
    except Exception as e:
        logging.error(f"Error in WebSocket handler: {e}")

async def main():
    server = await websockets.serve(handle_client, "0.0.0.0", 8765)
    logging.info("WebSocket Server Running on ws://<RaspberryPi_IP>:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
