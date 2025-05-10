import asyncio
import websockets
import json

SERVER_URL = "wss://hopit-ws-server.glitch.me/ws"

async def play(room_code):
    uri = f"{SERVER_URL}/{room_code}"
    try:
        async with websockets.connect(uri) as websocket:
            print(f"Connected to room '{room_code}'")

            # Check for full room message
            initial_response = await websocket.recv()
            if initial_response == "ROOM_FULL":
                print("Room is full. Please try another code.")
                return

            # Store local player state
            player_status = {"score": 0, "alive": True}

            # Function to receive opponent updates
            async def receive_opponent():
                while True:
                    try:
                        msg = await websocket.recv()
                        opponent_status = json.loads(msg)
                        print("[Opponent]", opponent_status)  # Replace with UI update in game
                    except:
                        print("Lost connection to opponent.")
                        break

            # Start listening to opponent in background
            asyncio.create_task(receive_opponent())

            # Main loop (replace with your Pygame loop logic)
            while player_status["alive"]:
                await asyncio.sleep(1)  # simulate time passing
                player_status["score"] += 10  # example: score increases
                await websocket.send(json.dumps(player_status))

    except Exception as e:
        print("Connection failed:", e)

# To test from terminal:
if __name__ == "__main__":
    room = input("Enter room code: ")
    asyncio.run(play(room))
