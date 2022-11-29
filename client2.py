import socket
if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 6666
    addr=(ip,port)
    client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        data=input("enter a word:")
        data=data.encode("utf-8")
        client.sendto(data,addr)
        data,addr=client.recvfrom(1024)
        data=data.decode("utf-8")
        print(data)
