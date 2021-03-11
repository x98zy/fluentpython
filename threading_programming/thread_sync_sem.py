"""线程间同步-信号量（用于控制进入的线程数量）,acquire会将数量减一
release会将数量加1"""

import threading
import time

class HtmlSplider(threading.Thread):
    def __init__(self,sem):
        super().__init__()
        self.sem=sem
    def run(self):
        time.sleep(2)
        print("get html end")
        self.sem.release()

class UrlProducer(threading.Thread):
    def __init__(self,sem):
        super().__init__()
        self.sem=sem
    def run(self):
        for i in range(20):
            self.sem.acquire()
            thread=HtmlSplider(self.sem)
            thread.start()

if __name__=="__main__":
    sem=threading.Semaphore(3)
    urlthread=UrlProducer(sem)
    urlthread.start()
