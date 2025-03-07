# Scratch Grove Extension

This repository provides a **Scratch extension** for controlling Grove modules on a Raspberry Pi using a WebSocket server.

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

---

## 🚀 **Installation on Raspberry Pi**
To set up the project, clone the repository and run the setup script:
```sh
cd ~
git clone https://github.com/brwhaley/scratch-grove-extension.git
cd scratch-grove-extension
bash scripts/setup.sh
```
This will:
✅ Install necessary system packages.  
✅ Set up a **Python virtual environment (`venv`)**.  
✅ Install the required Python dependencies inside `venv`.  

---

## 🏃 **Running the WebSocket Server**
Before running the WebSocket server, you must **activate the virtual environment**:
```sh
source ~/scratch-grove-extension/venv/bin/activate
python3 src/websocket-server/server.py
```
✅ The server will start and listen for WebSocket connections on **port `8765`**.

To **stop the server**, press `CTRL+C`.

To **exit the virtual environment**, run:
```sh
deactivate
```

---

## 🎮 **Using the Scratch Extension**
1. Open **Scratch**.
2. Go to **Extensions → Load from URL**.
3. Enter the URL where `extension.js` is hosted **or** add it manually.

Once connected, you can use the blocks to control your Grove modules!

---

## 🔄 **Updating the Repository**
To get the latest updates:
```sh
cd ~/scratch-grove-extension
git pull origin main
```
If new dependencies are added, re-run:
```sh
bash scripts/setup.sh
```

---

## 🛠 **Troubleshooting**
### ❌ **ModuleNotFoundError: No module named 'websockets'**
If you see this error, ensure you have activated `venv` before running the server:
```sh
source ~/scratch-grove-extension/venv/bin/activate
python3 src/websocket-server/server.py
```

### ❌ **ModuleNotFoundError: No module named 'grove'**
Ensure `grove.py` is correctly installed inside `venv`:
```sh
source ~/scratch-grove-extension/venv/bin/activate
cd ~/grove.py
pip install .
```

---

## ⚖️ **License**
This project is licensed under the **MIT License**.

---

## 🎯 **Next Steps**
- **Add more Grove modules** to the WebSocket server and Scratch extension.
- **Improve the Scratch UI** with more interactive blocks.
- **Publish the Scratch extension** for easier integration.
