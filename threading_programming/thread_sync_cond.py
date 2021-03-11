import threading

class TiaoMao(threading.Thread):
    def __init__(self,cond):
        super().__init__(name="天猫")
        self.cond=cond
    def run(self):
        with self.cond:
            print("{}:小爱".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{}:我们来对古诗吧".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{}:我住长江尾".format(self.name))
            self.cond.notify()


class XiaoAi(threading.Thread):
    def __init__(self,cond):
        super().__init__(name="小爱")
        self.cond=cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}:在".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{}:我住长江头".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{}:君心似我心".format(self.name))

if __name__=="__main__":
    cond=threading.Condition()
    tiaomao=TiaoMao(cond)
    xiaoai=XiaoAi(cond)
    xiaoai.start()
    tiaomao.start()