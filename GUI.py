import tkinter as tk
import redis
import json

def search_patient():
    r = redis.Redis(host='localhost', port=6379, db=0)
    patient_id = entry.get()
    vital_signs = json.loads(r.get(patient_id))
    # Display the vital signs in your GUI

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Search", command=search_patient)
button.pack()
root.mainloop()