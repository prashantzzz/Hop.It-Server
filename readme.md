# Hop.It Multiplayer WebSocket Server

This is the real-time multiplayer server for **[Hop.It](https://github.com/prashantzzz/hop.it)**, a vertical jumping game built with Pygame. It allows two players to compete live by syncing scores and survival status over WebSockets.

Hosted for free using **FastAPI + WebSocket** on [Render](https://hop-it-server.onrender.com/).

---

## 🌐 Live Server URL

Replace `<room_code>` with any 6-letter code (e.g. `abc123`):

wss://hop-it-server.onrender.com/ws/<room_code>

---

## 📁 File Structure

├── server.py # FastAPI WebSocket server
├── requirements.txt # Python dependencies
├── render.yaml # render config file
└── README.md # You're here!


---

## 🚀 How It Works

- Players join using a **room code**
- Each room allows **2 players max**
- Scores and alive status are synced in real-time
- When one player falls, the other wins
- Rooms auto-clean when players disconnect

---

[Render Hosted Server](https://hop-it-server.onrender.com/)
If the server is working, you’ll see:
{"detail":"Not Found"}
This means the server is running (FastAPI root endpoint is undefined).

🧪 Test WebSocket
You can use clientA.py/clientB.py in your game to connect and exchange real-time score/status.

💬 About
Built to enable 1v1 multiplayer in [Hop.It](https://github.com/prashantzzz/hop.it), a vertical arcade jumper game made with Pygame.

Enjoy climbing and competing!
