from fastapi import FastAPI,WebSocket,WebSocketDisconnect
import uvicorn

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket:  WebSocket):
    await websocket.accept()
    print("client connected")

    try:
        while True:
            data = await websocket.receive_bytes()
            #print(f"Recieved: {data}")
            await websocket.send_bytes((data))
            #print(f"sent back: {data}")
    except WebSocketDisconnect:
        print("Client Disconnected")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost",port=8000)

    
