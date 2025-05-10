# Hop.It Multiplayer WebSocket Server

This is the real-time multiplayer server for **Hop.It**, a vertical jumping game built with Pygame. It allows two players to compete live by syncing scores and survival status over WebSockets.

Hosted for free using **FastAPI + WebSocket** on [Glitch](https://glitch.com), no credit card required.

---

## 🌐 Live Server URL

Replace `<room_code>` with any 6-letter code (e.g. `abc123`):

wss://hopit-ws-server.glitch.me/ws/<room_code>

---

## 📁 File Structure

├── server.py # FastAPI WebSocket server
├── requirements.txt # Python dependencies
├── start.sh # Glitch launch script (must be executable)
├── .glitch.json # (Optional) Glitch project config
└── README.md # You're here!


---

## 🚀 How It Works

- Players join using a **room code**
- Each room allows **2 players max**
- Scores and alive status are synced in real-time
- When one player falls, the other wins
- Rooms auto-clean when players disconnect

---

## 🔧 How to Deploy (on Glitch.com)

1. Go to [https://glitch.com](https://glitch.com)
2. Create a new project → choose "Hello Webpage" or "Blank"
3. Click `Tools` → `Terminal`
4. Run:
   ```bash
   rm -rf * .*

Create the following files with these contents:

server.py

✅ Hosting Check

After setup, visit:

https://hopit-ws-server.glitch.me
If the server is working, you’ll see:
{"detail":"Not Found"}
This means the server is running (FastAPI root endpoint is undefined).

🧪 Test WebSocket
Try connecting to the server using a WebSocket client or the game client:
wss://hopit-ws-server.glitch.me/ws/test01
You can use client_ws.py in your game to connect and exchange real-time score/status.

💬 About
Built to enable 1v1 multiplayer in Hop.It, a vertical arcade jumper game made with Pygame.

Enjoy climbing and competing!