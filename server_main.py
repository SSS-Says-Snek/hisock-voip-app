import time
import random

from hisock import HiSockServer

IP = "192.168.1.131"
PORT = 9999

server = HiSockServer((IP, PORT))

online_users = []
used_discriminators = {}
ip_to_discriminator = {}

@server.on("join")
def on_join(client_data):
    username = client_data.name

    if used_discriminators.get(username) is None:
        used_discriminators[username] = []
    while (discriminator := random.randint(0, 9999)) in used_discriminators[username]:
        pass
    
    online_users.append(f"{username}#{discriminator}")
    used_discriminators[username].append(discriminator)
    ip_to_discriminator[client_data.ip] = discriminator

    server.send_client(client_data, "discriminator", discriminator)

    for client in server.get_all_clients():
        if client["ip"] != client_data.ip:
            server.send_client(client["ip"], "client_joined", f"{client['name']}#{discriminator}")

    print(f"User {username}#{discriminator} ({client_data.ip_as_str}) joined!")

@server.on("leave")
def on_leave(client_data):
    discriminator = ip_to_discriminator[client_data.ip]

    online_users.remove(f"{client_data.name}#{discriminator}")
    used_discriminators[client_data.name].remove(discriminator)

    print(f"User {client_data.name}#{discriminator} ({client_data.ip_as_str}) left :(")

@server.on("send_everyone_message")
def on_message(client_data, msg: str):
    print("wow")

    # Can't use datetime.now() because hisock can't send arbitrary objects (L pickle)
    now = time.time()
    username = f"{client_data.name}#{ip_to_discriminator[client_data.ip]}"
    server.send_all_clients("recv_everyone_message", {"username": username, "message": msg, "time_sent": now})

print(f"Starting server at {IP}:{PORT}!")
server.start()