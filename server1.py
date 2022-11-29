import socket
if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 6666
    
    server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server.bind((ip,port))
    
    while True:
        data, addr=server.recvfrom(1024)
        data=data.decode("utf-8")
        print(data)
        data=data.upper()
        data=data.encode("utf-8")
        server.sendto(data,addr)
