#!/bin/bash
echo "🔧 Installing dependencies and setting up virtual environment..."

# Update system
sudo apt update && sudo apt upgrade -y

# Install required system packages
sudo apt install -y python3 python3-pip python3-venv git

# Set up virtual environment
cd ~/scratch-grove-extension
python3 -m venv venv
source venv/bin/activate

# Install dependencies inside venv
pip install websockets
git clone https://github.com/Seeed-Studio/grove.py.git
cd grove.py && pip install .

echo "✅ Setup complete!"
echo "🔹 To run the WebSocket server, activate the virtual environment first:"
echo "    source ~/scratch-grove-extension/venv/bin/activate"
echo "    python3 src/websocket-server/server.py"
