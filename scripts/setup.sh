#!/bin/bash
echo "🔧 Installing dependencies..."

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python & dependencies
sudo apt install -y python3 python3-pip git

# Install WebSockets and Grove library
pip3 install websockets
git clone https://github.com/Seeed-Studio/grove.py.git
cd grove.py && sudo pip3 install .

echo "✅ Installation complete! Now run: python3 src/websocket-server/server.py"
