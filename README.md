# WebSocket Audio Streaming

A real-time audio streaming application built with Python, FastAPI, and WebSockets. It splits an audio file into chunks and streams them to a server which echoes them back in real time.

---

## What It Does

- Client reads an audio file and splits it into small chunks
- Each chunk is sent to the server one by one over a WebSocket connection
- Server receives each chunk and sends it back
- Client confirms each chunk arrived back
- Simulates real time audio streaming between a client and server

---

## How It Works

**Client — simulate.py**
Opens a WebSocket connection to the server. Reads the audio file in chunks of 4065 bytes. Sends each chunk and waits for the server to echo it back. Waits 1 second between each chunk to simulate real time streaming.

**Server — server.py**
Built with FastAPI and runs on port 8000. Accepts incoming WebSocket connections. Listens for incoming audio chunks. Echoes each chunk back to the client immediately. Handles disconnections cleanly.

---

## Project Structure

```
WEBSOCKET_ECHOBOT/
│
├── simulate.py              
├── main.py    -Server 
├── file_example_WAV_5MG.wav  
├── requirements.txt
└── README.md
```

---

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/websocket-audio-streaming.git
cd websocket-echobot
```

**2. Install dependencies**
```bash
pip install fastapi uvicorn websockets
```

---

## Usage

**Step 1 — Start the server**
```bash
python server.py
```

You should see:
```
Uvicorn running on http://localhost:8000
```

**Step 2 — Run the client in a new terminal**
```bash
python simulate.py
```

You should see:
```
Connecting to ws://localhost:8000/ws
Connected to server
Sending chunk 1: 4065 bytes
Received back chunk 1: 4065 bytes
Sending chunk 2: 4065 bytes
Received back chunk 2: 4065 bytes
...
All chunks sent
```

---

## Requirements

```
fastapi
uvicorn
websockets
```

---

## Tech Stack

- **Python** 
- **FastAPI** 
- **WebSockets** 
- **Uvicorn** 
- **AsyncIO** 
