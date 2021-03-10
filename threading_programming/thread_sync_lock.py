"""Lock,RLock用于线程间同步，RLock可以重复读取多次"""
import threading
from threading import Lock,RLock

total=0

def add(lock):
    global total
    for i in range(1000):
        lock.acquire()
        total+=1
        lock.release()

def desc(lock):
    global total
    for i in range(1000):
        lock.acquire()
        total-=1
        lock.release()

if __name__=="__main__":
    lock = Lock()
    thread1=threading.Thread(target=add,args=(lock,))
    thread2=threading.Thread(target=desc,args=(lock,))
    thread1.start()
    thread2.start()
    print(total)


