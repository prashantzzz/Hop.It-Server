# server.py
import socket
import threading
import json

rooms = {}
lock = threading.Lock()
MAX_PLAYERS_PER_ROOM = 2

def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")
    
    try:
        room_code = conn.recv(1024).decode().strip()
        if not room_code:
            conn.sendall(b"Invalid room code.")
            conn.close()
            return

        with lock:
            if room_code not in rooms:
                rooms[room_code] = []
            if len(rooms[room_code]) >= MAX_PLAYERS_PER_ROOM:
                conn.sendall(b"Room full.")
                conn.close()
                return
            rooms[room_code].append(conn)
            conn.sendall(b"OK")

        print(f"[ROOM {room_code}] Players: {len(rooms[room_code])}/2")

        while True:
            data = conn.recv(1024)
            if not data:
                break

            with lock:
                for client in rooms[room_code]:
                    if client != conn:
                        try:
                            client.sendall(data)
                        except:
                            pass

    except Exception as e:
        print(f"[ERROR] {e}")

    finally:
        conn.close()
        with lock:
            if room_code in rooms and conn in rooms[room_code]:
                rooms[room_code].remove(conn)
                if not rooms[room_code]:
                    del rooms[room_code]
        print(f"[DISCONNECTED] {addr} from {room_code}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))  # Or 127.0.0.1 for local testing
    server.listen()
    print("[SERVER STARTED] Listening on port 5555...")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    start_server()
