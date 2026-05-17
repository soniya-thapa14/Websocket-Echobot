import asyncio
import websockets


async def simulate():
    uri = "ws://localhost:8000/ws"
    print(f"connecting to {uri}")
    audio_file = 'file_example_WAV_5MG.wav'
    chunk_size = 100000

    async with websockets.connect(uri) as websocket:
        print("connected to server")

        with open(audio_file, "rb") as f:
            chunk_number =1

            while True:
                chunk = f.read(chunk_size)

                if not chunk:
                    break

                print(f"\nSending chunk {chunk_number}: {len(chunk)} bytes")
                await websocket.send(chunk)
                response = await websocket.recv()
                print(f"Received back chunk {chunk_number}: {len(response)} bytes")
                chunk_number +=1

                await asyncio.sleep(1)
        print(f"All chunks sent")

if __name__ == "__main__":
    asyncio.run(simulate())