#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File   ：callable_object
# @IDE    ：pycharm
# @Author ：xz98y
# @Date   ：2022/2/7 21:55

# 实现可调用的对象，当在一个类中定义了__call__方法，那么
# 由这个类创建的对象也是可以调用的

import random


class Bingocage():
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError as e:
            raise LookupError("pop item from empty list")

    def __call__(self, *args, **kwargs):
        return self.pick()


if __name__ == "__main__":
    bingo = Bingocage([3, 1, 6, 9, 11, 45, 23])
    print(bingo.pick())
    # 虽然bingo是对象，但是因为其所属类实现了__call__方法，所以bingo也是可以调用的
    print(bingo())