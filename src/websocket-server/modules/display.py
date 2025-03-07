import json
from grove.grove_4_digit_display import Grove4DigitDisplay

CLK_PIN = 5
DIO_PIN = 4
display = Grove4DigitDisplay(CLK_PIN, DIO_PIN)

async def handle_4_digit_display(message, websocket):
    value = message.get("value", "0000")
    display.show(value)
    await websocket.send(json.dumps({"status": f"Display set to {value}"}))
