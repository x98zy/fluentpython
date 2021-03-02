"""socket服务端的编程流程，创建socket对象，socket的初始化过程中需要指明网络类型，协议类型
AF_INET表示的是IPV4，SOCK_STREAM表示是TCP协议，然后调用bind方法进行地址和端口绑定，然后调用listen方法
进行监听请求，调用accept方法接收请求，accept方法返回两个对象，一个是新生成的socket对象，还有一个就是
客户端的请求地址,然后调用新生成的socket对象的recv方法接受数据或者send方法发送数据"""

import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0",8000))
server.listen()
sock,addr=server.accept()

print(addr)
data=sock.recv(1024)
print(data.decode("utf8"))