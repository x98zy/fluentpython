"""socket客户端的编程过程，生成socket对象，调用connect方法连接服务端，调用send方法发送数据"""

import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8000))
client.send("hello".encode("utf8"))
client.close()