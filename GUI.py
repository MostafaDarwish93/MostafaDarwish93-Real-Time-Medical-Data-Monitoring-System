import tkinter as tk
import redis
import json
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Global index to keep track of the data point to be plotted next
index = 0
vital_signs = None

def search_patient():
    global vital_signs, index
    r = redis.Redis(host='redis-15549.c328.europe-west3-1.gce.redns.redis-cloud.com', port=15549, password='')
    patient_id = entry.get()
    vital_signs = json.loads(r.get(patient_id))

    # Update the patient ID label
    patient_id_label.config(text=f"Patient ID: {patient_id}")

    # Reset the index
    index = 0

    # Start the real-time plotting
    update()

def update():
    global index

    # Clear the axes for the new plot
    ax.clear()

    # Set the title
    ax.set_title(f'Vital Signs')

    # Plot the heart rate and blood pressure point by point
    if vital_signs and index < len(vital_signs['heart_rate']):
        ax.plot(vital_signs['heart_rate'][:index+1], label='Heart Rate' if index == 0 else "")
        ax.plot(vital_signs['blood_pressure'][:index+1], label='Blood Pressure' if index == 0 else "")
        index += 1

        # Add labels and a legend
        ax.set_xlabel('Time')
        ax.set_ylabel('Value')
        ax.legend()

        # Redraw the canvas with the new plot
        canvas.draw()

    # Schedule the next update
    root.after(1000, update)

def plot_heart_rate():
    ax.clear()
    ax.plot(vital_signs['heart_rate'], label='Heart Rate')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend()
    canvas.draw()

def plot_blood_pressure():
    ax.clear()
    ax.plot(vital_signs['blood_pressure'], label='Blood Pressure')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend()
    canvas.draw()

root = tk.Tk()
root.geometry("800x600")  # Set initial size of the window

entry = tk.Entry(root)
entry.pack(padx=20, pady=20)  # Add padding around the entry field

search_button = tk.Button(root, text="Search For Patient ID", command=search_patient)
search_button.pack(pady=10)  # Add padding above the button

heart_rate_button = tk.Button(root, text="Plot Heart Rate", command=plot_heart_rate)
heart_rate_button.pack(pady=10)

blood_pressure_button = tk.Button(root, text="Plot Blood Pressure", command=plot_blood_pressure)
blood_pressure_button.pack(pady=10)

patient_id_label = tk.Label(root, text="")
patient_id_label.pack(pady=10)

# Create a new figure and add a subplot
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

# Create a canvas and add it to the GUI
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()