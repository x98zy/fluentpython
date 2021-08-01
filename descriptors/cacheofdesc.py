# -*- coding: utf-8 -*-
# @Project: fluentpython
# @Author: xuzhiyi
# @File name: cacheofdesc
# @Create time: 2021/8/1 21:44

"""用描述符实现一个Cache"""

from time import sleep


class Cache():
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        instance.__dict__[self.name] = self.func(instance)
        return instance.__dict__[self.name]

class Foo():
    @Cache
    def bar(self):
        sleep(5)
        return "just sleep 5 seconds"

if __name__ == "__main__":
    foo = Foo()
    # 第一次需要执行5秒
    print(foo.bar)
    # 第二次立即执行
    print(foo.bar)
