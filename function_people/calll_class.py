"""本章主要讲解python函数作为一等对象"""


#实现一个实力可以调用的类
import random


class BingoPage():
    def __init__(self,items):
        self._items=items
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError as e:
            raise LookupError("内置列表已空")

    def __call__(self, *args, **kwargs):
        return self.pick()

if __name__=="__main__":
    bingo=BingoPage([2,41,2,1])
    print(bingo())
    print(bingo())
    print(bingo())
    print(bingo())
    #此时不用直接调用bingo.pick()方法