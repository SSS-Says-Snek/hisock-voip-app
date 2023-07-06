"""
This file is a part of the source code for hisock-voip-app
This project has been licensed under the MIT license.
Copyright (c) 2022-present SSS-Says-Snek
"""

from __future__ import annotations

import random
import time

from hisock import HiSockServer

IP = input("Enter Server IP: ")
PORT = 9999

server = HiSockServer((IP, PORT))

online_users = []
used_discriminators = {}


@server.on("join")
def on_join(client_data):
    name = client_data.name

    if used_discriminators.get(name) is None:
        used_discriminators[name] = []
    while (discriminator := random.randint(0, 9999)) in used_discriminators[name]:
        pass

    username = f"{name}#{discriminator:04}"

    online_users.append(username)
    used_discriminators[name].append(discriminator)

    # INCLUDE CURRENT USER IN ONLINE_USERS
    server.send_client(client_data, "discriminator", discriminator)
    server.send_client(client_data, "online_users", online_users)

    for client in server.get_all_clients():
        if client["ip"] != client_data.ip:
            server.send_client(client["ip"], "client_join", username)

    print(f"User {username} ({client_data.ip_as_str}) joined!")


@server.on("leave")
def on_leave(client_data):
    username = client_data.name

    online_users.remove(username)
    used_discriminators[username[:-5]].remove(int(username[-4:]))

    for client in server.get_all_clients():
        if client["ip"] != client_data.ip:
            server.send_client(client["ip"], "client_leave", username)

    print(f"User {username} ({client_data.ip_as_str}) left :(")


@server.on("name_change")
def on_name_change(_, __, ___):
    pass


@server.on("send_everyone_message")
def on_message(client_data, msg: str):
    print("Everyone message")

    # Can't use datetime.now() because hisock can't send arbitrary objects (L pickle)
    now = time.time()
    server.send_all_clients("recv_everyone_message", {"username": client_data.name, "message": msg, "time_sent": now})


@server.on("send_dm_message")
def on_dm_message(client_data, data: list):
    print("DM message")
    recipient, message = data

    now = time.time()
    server.send_client(
        recipient, "recv_dm_message", {"username": client_data.name, "message": message, "time_sent": now}
    )

@server.on("request_call")
def on_request_call(client_data, recipient: str):
    print(f"Call request from {client_data.name} to {recipient}")
    server.send_client(
        recipient, "incoming_call", client_data.name
    )

@server.on("accepted_call")
def on_accepted_call(client_data, original_sender: str):
    print(f"Accepted call between {client_data.name} and {original_sender}!")
    server.send_client(
        original_sender, "accepted_call", client_data.name
    )

@server.on("video_data")
def on_video_data(_, data: list):
    recipient, frame_data = data

    if recipient in online_users:
        print(time.time(), "viddata")
        server.send_client(recipient, "video_data", frame_data)
    
@server.on("end_call")
def on_end_call(client_data, recipient: str):
    print(f"Requesting to end call between {client_data.name} and {recipient} ({client_data.name} initiated)")
    server.send_client(recipient, "end_call")

@server.on("ended_call")
def on_ended_call(client_data, recipient: str):
    print(f"Ended call between {client_data.name} and {recipient} ({recipient} finalized)")
    server.send_client(recipient, "ended_call")


print(f"Starting server at {IP}:{PORT}!")
server.start()
