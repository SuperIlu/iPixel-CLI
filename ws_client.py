from websockets.sync.client import connect
import sys
import json

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <server> <command>")
    exit(1)
else:
    server = sys.argv[1]
    command = sys.argv[2]

    req = {
        "command": command,
        "params": sys.argv[3:]
    }
    js = json.dumps(req)

    if not server.startswith('ws://'):
        server = 'ws://'+server

    with connect(server) as websocket:
        websocket.send(js)
        print(f">>> {js}")

        resp = websocket.recv()
        print(f"<<< {resp}")
