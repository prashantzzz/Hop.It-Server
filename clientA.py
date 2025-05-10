# client_ws.py
import asyncio
import websockets
import json

async def play(room_code):
    uri = f"wss://hop-it-server.onrender.com/ws/{room_code}"  # Use wss:// for secure connection
    async with websockets.connect(uri) as websocket:
        response = await websocket.recv()
        if response == "ROOM_FULL":
            print("Room is full.")
            return

        print("Connected to room!")

        async def receive():
            while True:
                msg = await websocket.recv()
                print("[Opponent]", msg)

        asyncio.create_task(receive())

        player_status = {"score": 0, "alive": True}
        while player_status["alive"]:
            await asyncio.sleep(1)
            player_status["score"] += 10
            await websocket.send(json.dumps(player_status))

room=input("Enter room code: ")
asyncio.run(play(room))  # Replace with actual room code
