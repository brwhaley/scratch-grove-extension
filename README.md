# Scratch Grove Extension

This repository provides a **Scratch extension** for controlling Grove modules on a Raspberry Pi.

## 📂 Project Structure
```
scratch-grove-extension/
│── src/                  
│   ├── scratch-extension/         # JavaScript for Scratch
│   │   ├── extension.js            # Main Scratch extension
│   │   ├── modules/                 # Individual Scratch blocks
│   ├── websocket-server/           # Python WebSocket backend
│   │   ├── server.py                 # Main WebSocket server
│   │   ├── modules/                  # Hardware-specific handlers
│── examples/                         
│── docs/                             
│── tests/                            
│── scripts/                          
│── README.md                         
│── LICENSE                          
│── .github/                          
```

## 🚀 Installation on Raspberry Pi
Run the setup script:
```
cd ~
git clone https://github.com/brwhaley/scratch-grove-extension.git
cd scratch-grove-extension
bash scripts/setup.sh
```

## 🏃 Running the WebSocket Server
After installation, start the server:
```
python3 src/websocket-server/server.py
```
