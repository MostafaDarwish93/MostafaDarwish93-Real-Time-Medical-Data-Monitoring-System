# Real-Time-Medical-Data-Monitoring-System

This project is a real-time patient vital signs monitoring system. It consists of a client that generates random vital signs for a patient and sends this data to a server via a socket connection. The server then stores this data in a Redis database. There is also a GUI application that retrieves the vital signs for a specific patient from the Redis database and displays them in a plot.

## Language Used

The project is implemented in Python, using several libraries including `socket` for networking, `redis` for interacting with the Redis database, `tkinter` for the GUI, and `matplotlib` for plotting the vital signs.

## Code Explanation

The project consists of three main parts:

1. **Client Code**: Generates random vital signs for a patient and sends this data to a server via a socket connection. The patient ID is input by the user.

2. **Server Code**: Receives the data from the client, decodes it, and stores it in a Redis database.

3. **GUI Code**: A simple Tkinter application that retrieves the vital signs for a specific patient from the Redis database and displays them in a plot.

## How to Run the Code and Use Redis

1. Install the required Python libraries if you haven't already: `pip install redis matplotlib tkinter`.

2. Make sure you have a Redis server running and replace the host, port, and password in the code with your Redis server details.

3. Run the server code: `python server.py`.

4. Run the client code in a different terminal: `python client.py`. Enter a patient ID when prompted.

5. Run the GUI code in another terminal: `python gui.py`. Enter the same patient ID in the entry field and click "Search" to display the patient's vital signs.

Please note that the Redis database connection details (host, port, password) are hardcoded in the code. In a real-world application, these should be stored securely and not exposed in the code.