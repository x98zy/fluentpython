# -*- coding: utf-8 -*-
# @Project: fluentpython
# @Author: xuzhiyi
# @File name: descriptor
# @Create time: 2021/8/1 20:51

"""属性描述符就是实现了__get__,__set__,__delete__三个魔法函数的类
当然三个函数不一定都要实现，而可以只实现其中一个，这样都可以称作属性
描述符，属性描述符是可重用的属性，它把对函数的调用伪装成对属性的访问"""


class NonNegative():
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        # 这里的instance表示的就是Score这个类的实例
        # __dict__这个字典存放了一个类的所有属性
        if value < 0:
            raise ValueError("value must be > 0")
        instance.__dict__[self.name] = value

class Score():
    math = NonNegative('math')
    english = NonNegative('english')

    def __init__(self, math, englisth):
        self.math = math
        self.english = englisth

if __name__ == "__main__":
    score = Score(100,50)
    print(score.math)