import tkinter as tk
import redis
import json
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def search_patient():
    r = redis.Redis(host='redis-15549.c328.europe-west3-1.gce.redns.redis-cloud.com', port=15549, password='b3jfO2WviKF4kcD1PwgTTc4HpMEFYOsW')
    patient_id = entry.get()
    vital_signs = json.loads(r.get(patient_id))

    # Create a new figure and add a subplot
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Set the title
    ax.set_title(f'Vital Signs for {patient_id}')

    # Plot the heart rate and blood pressure point by point
    for i in range(len(vital_signs['heart_rate'])):
        ax.plot(vital_signs['heart_rate'][:i+1], label='Heart Rate' if i == 0 else "")
        ax.plot(vital_signs['blood_pressure'][:i+1], label='Blood Pressure' if i == 0 else "")
        plt.pause(0.1)

    # Add labels and a legend
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend()

    # Create a canvas and add it to the GUI
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
        
root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Search", command=search_patient)
button.pack()
root.mainloop()
