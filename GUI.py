import tkinter as tk
import redis
import json

def search_patient():
    r = redis.Redis(host='redis-12507.c246.us-east-1-4.ec2.redns.redis-cloud.com', port=12507, password='A0e5sROUo9eHtfcUeEA1NyFxPMyWSfp3')
    patient_id = entry.get()
    vital_signs = json.loads(r.get(patient_id))
    # Display the vital signs in your GUI

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Search", command=search_patient)
button.pack()
root.mainloop()
