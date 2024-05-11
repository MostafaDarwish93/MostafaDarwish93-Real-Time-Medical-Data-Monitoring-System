import socket
import json
import redis

def receive_data():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    r = redis.Redis(host='localhost', port=6379, db=0)

    while True:
        client_socket, addr = server_socket.accept()
        data = json.loads(client_socket.recv(1024).decode())
        r.set(data["patient_id"], json.dumps(data["vital_signs"]))

receive_data()