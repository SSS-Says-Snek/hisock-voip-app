from hisock import HiSockServer

IP = "192.168.1.131"
PORT = 9999

server = HiSockServer((IP, PORT))

@server.on("join")
def on_join(client_data):
    print(f"User {client_data.name} ({client_data.ip_as_str}) joined!")

@server.on("leave")
def on_leave(client_data):
    print(f"User {client_data.name} ({client_data.ip_as_str}) left :(")

@server.on("send_everyone_message")
def on_message(client_data, msg: str):
    print("wow")
    server.send_all_clients("recv_everyone_message", {"username": client_data.name, "message": msg})

print(f"Starting server at {IP}:{PORT}!")
server.start()