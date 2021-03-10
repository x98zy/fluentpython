"""线程间通信-队列"""

import threading
from queue import Queue
import time


def get_url_list(thread_queue):
    print("get url list started")
    for i in range(20):
        thread_queue.put(i)
    time.sleep(2)
    print("get url list end")

def get_detail_html(thread_queue):
    global url_list
    while True:
        thread_queue.get()
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

if __name__=="__main__":
    thread_queue=Queue()
    thread1=threading.Thread(target=get_url_list,args=(thread_queue,))
    thread1.start()
    for i in range(5):
        thread2 = threading.Thread(target=get_detail_html,args=(thread_queue,))
        thread2.start()
