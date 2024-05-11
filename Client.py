import socket
import json
import random
import time

def generate_vital_signs():
    return {
        "heart_rate": random.randint(60, 100),
        "blood_pressure": random.randint(120, 180)
    }

def send_data():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    while True:
        patient_id = "patient1"
        vital_signs = generate_vital_signs()
        data = {"patient_id": patient_id, "vital_signs": vital_signs}
        client_socket.send(json.dumps(data).encode())
        time.sleep(1)

send_data()