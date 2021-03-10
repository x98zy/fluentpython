"""python线程间通信-共享变量,
但是这样的共享变量的操作并不是线程安全的，因为
对变量的操作大多时候都不是一个原子操作"""
import time
import threading

url_list=[]

def get_url_list():
    global url_list
    print("get url list started")
    for i in range(20):
        url_list.append(i)
    time.sleep(2)
    print("get url list end")

def get_detail_html():
    global url_list
    while True:
        if len(url_list):
            url_list.pop()
            print("get detail html started")
            time.sleep(2)
            print("get detail html end")

if __name__=="__main__":
    thread1=threading.Thread(target=get_url_list)
    thread1.start()
    for i in range(5):
        thread2 = threading.Thread(target=get_detail_html)
        thread2.start()
