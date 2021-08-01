# -*- coding: utf-8 -*-
# @Project: fluentpython
# @Author: xuzhiyi
# @File name: example
# @Create time: 2021/8/1 20:21
"""有一个记录学生分数的类，要求分数不能负数"""


class Score(object):
    def __init__(self, math):
        if math < 0:
            raise ValueError("分数不能为负数")
        self.math = math


"""此处在初始化后重新给math属性赋值为-10后并没有抛出ValueError,
 这违反了我们设计的初衷，所以仍需改进，改进可以使用@property"""


if __name__ == "__main__":
    score_instance = Score(50)
    score_instance.math = -10
    print(score_instance.math)