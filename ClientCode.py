import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()

host = 'localhost'
port = 143
server_addr = (host, port)
BUFFER_SIZE = 2000
c1msg = input("tcpClientA: Enter message/ Enter exit:")

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.setblocking(1)
tcpClientA.connect_ex(server_addr)
events = selectors.EVENT_READ | selectors.EVENT_WRITE

data = types.SimpleNamespace(
            recv_total=0,
            outb=b"",
        )
sel.register(tcpClientA, events, data=data)

while c1msg != 'exit':
    tcpClientA.send(c1msg.encode())
    data = tcpClientA.recv(BUFFER_SIZE)
    if not data:
        print("Server closed the connection")
    print("Server > ",  repr(data))
    data = ''
    c1msg = input("Me > ")

tcpClientA.close()
