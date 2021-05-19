import threading
import time

def get_html_detail():
    print("get html detail started")
    time.sleep(2)
    print("get html detail end")

def get_url_list():
    print("get url list started")
    time.sleep(4)
    print("get url list end")


if __name__=="__main__":
    thread1=threading.Thread(target=get_html_detail)
    thread2=threading.Thread(target=get_url_list)
    #设置为守护线程
    """此处会打印出get html detail end和get url list end，因为thread2没有设置为守护线程
    而thread2的运行时间大约是4秒，对于一般的线程主线程会等待其执行完再退出"""
    #主线程会等到没有非守护线程存活才会退出
    thread1.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()
    # 主线程在此处代码出阻塞，等待子线程的执行完成
    #thread1.join()
    #thread2.join()
    print("last time is {}".format(time.time()-start_time))