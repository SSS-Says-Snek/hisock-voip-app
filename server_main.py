"""
This file is a part of the source code for hisock-voip-app
This project has been licensed under the MIT license.
Copyright (c) 2022-present SSS-Says-Snek
"""

from __future__ import annotations

import random
import time

from hisock import HiSockServer

IP = "192.168.1.131"
PORT = 9999

server = HiSockServer((IP, PORT))

online_users = []
used_discriminators = {}
ip_to_discriminator = {}


@server.on("join")
def on_join(client_data):
    name = client_data.name

    if used_discriminators.get(name) is None:
        used_discriminators[name] = []
    while (discriminator := random.randint(0, 9999)) in used_discriminators[name]:
        pass
    
    server.send_client(client_data, "discriminator", discriminator)
    server.send_client(client_data, "online_users", online_users)

    username = f"{name}#{discriminator}"

    online_users.append(username)
    used_discriminators[name].append(discriminator)
    ip_to_discriminator[client_data.ip] = discriminator

    for client in server.get_all_clients():
        if client["ip"] != client_data.ip:
            server.send_client(client["ip"], "client_join", username)

    print(f"User {username} ({client_data.ip_as_str}) joined!")


@server.on("leave")
def on_leave(client_data):
    name = client_data.name
    discriminator = ip_to_discriminator[client_data.ip]
    username = f"{name}#{discriminator}"

    online_users.remove(username)
    used_discriminators[name].remove(discriminator)

    for client in server.get_all_clients():
        if client["ip"] != client_data.ip:
            server.send_client(client["ip"], "client_leave", username)

    print(f"User {username} ({client_data.ip_as_str}) left :(")


@server.on("send_everyone_message")
def on_message(client_data, msg: str):
    print("wow")

    # Can't use datetime.now() because hisock can't send arbitrary objects (L pickle)
    now = time.time()
    username = f"{client_data.name}#{ip_to_discriminator[client_data.ip]}"
    server.send_all_clients("recv_everyone_message", {"username": username, "message": msg, "time_sent": now})


print(f"Starting server at {IP}:{PORT}!")
server.start()
