import json
import logging
from grove.grove_4_digit_display import Grove4DigitDisplay

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

CLK_PIN = 5
DIO_PIN = 6
display = Grove4DigitDisplay(CLK_PIN, DIO_PIN)

async def handle_4_digit_display(message, websocket):
    try:
        value = message.get("value", "0000")
        logging.info(f"Displaying value: {value}")
        display.show(value)

        response = {"status": f"Display set to {value}"}
        await websocket.send(json.dumps(response))
        logging.info(f"Sent response: {response}")

    except Exception as e:
        logging.error(f"Error setting display: {e}")
