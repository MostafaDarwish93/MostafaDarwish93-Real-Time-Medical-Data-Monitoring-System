import socket
import json
import redis

def receive_data():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    r = redis.Redis(host='redis-15549.c328.europe-west3-1.gce.redns.redis-cloud.com', port=15549, password='b3jfO2WviKF4kcD1PwgTTc4HpMEFYOsW')
    print("Server started. Waiting for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            data = json.loads(data.decode())
            print(f"Received data: {data}")

            r.set(data["patient_id"], json.dumps(data["vital_signs"]))

        print(f"Connection with {addr} closed")

receive_data()