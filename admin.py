#!/usr/bin/env python

import asyncio
import pathlib
import ssl
import websockets

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.load_verify_locations("./cert.pem", "./key.pem")

async def hello():
    uri = "wss://localhost/admin"
    async with websockets.connect(
        uri, ssl=ssl_context
    ) as websocket:
        greeting = await websocket.recv()
        print(f"Clients:\n\t {greeting}")
        clnt = input("Select client:")
        await websocket.send(clnt)
        while True:
            cmd = input("cmd:")
            await websocket.send(cmd)
            response = await websocket.recv()
            print(str(response))

asyncio.get_event_loop().run_until_complete(hello())

