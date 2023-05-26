from hisock import HiSockServer

server = HiSockServer(("192.168.1.131", 9999))

@server.on("join")
def on_join(client_data):
    print(client_data)

@server.on("leave")
def on_leave(client_data):
    print("left", client_data)

server.start()