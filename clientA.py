# client.py
import socket
import threading
import json
import time

server_ip = "your-server-ip"  # Change this to your Fly.io IP or localhost
server_port = 5555

room_code = input("Enter room code: ").strip()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))
client.sendall(room_code.encode())

response = client.recv(1024).decode()
if response == "Room full.":
    print("Room is already full. Try another code.")
    client.close()
    exit()
elif response == "Invalid room code.":
    print("Invalid room code.")
    client.close()
    exit()
elif response != "OK":
    print("Unexpected response:", response)
    client.close()
    exit()

print("Connected! Waiting for opponent...")

player_status = {"score": 0, "alive": True}

def receive():
    while True:
        try:
            data = client.recv(1024)
            if data:
                opponent_status = json.loads(data.decode())
                print("[Opponent]", opponent_status)
        except:
            break

threading.Thread(target=receive, daemon=True).start()

# Simulate status updates (replace with actual game loop in Pygame)
try:
    while player_status["alive"]:
        player_status["score"] += 10
        client.sendall(json.dumps(player_status).encode())
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    client.close()
