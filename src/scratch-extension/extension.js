(function (Scratch) {
    'use strict';

    class Grove4DigitDisplay {
        constructor() {
            this.socket = null;
            this.isConnected = false;
            this.connectWebSocket();
        }

        connectWebSocket() {
            const raspberryPiIP = "ws://localhost:8765";
            this.socket = new WebSocket(raspberryPiIP);

            this.socket.onopen = () => {
                console.log("Connected to Raspberry Pi");
                this.isConnected = true;
            };
        }

        sendCommand(command) {
            if (this.isConnected) {
                this.socket.send(JSON.stringify(command));
            }
        }

        setDisplay(args) {
            let value = args.VALUE.toString().slice(0, 4);
            this.sendCommand({ action: "set_display", value: value });
        }

        getInfo() {
            return {
                id: "grove4DigitDisplay",
                name: "4-Digit Display",
                blocks: [
                    {
                        opcode: "setDisplay",
                        blockType: Scratch.BlockType.COMMAND,
                        text: "set display to [VALUE]",
                        arguments: { VALUE: { type: Scratch.ArgumentType.STRING, defaultValue: "1234" } }
                    }
                ]
            };
        }
    }

    Scratch.extensions.register(new Grove4DigitDisplay());
})(Scratch);
