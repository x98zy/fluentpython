# -*- coding: utf-8 -*-
# @Project: fluentpython
# @Author: xuzhiyi
# @File name: propertyofscore
# @Create time: 2021/8/1 20:30

"""property实现的已经足够完美，但是唯一的缺点就是不能重用，如果有还有english,
和chinese两个属性，那么还要分别实现@englist @english.setter，@chinese,@chinese.setter装饰器实现的函数"""

class Score(object):
    def __init__(self, math):
        """
        此处math这个属性是对应的@property设置的math属性，
        通过执行self.math=math会转到@math.setter所装饰的
        这个函数中
        :param math:
        """
        self.math = math

    @property
    def math(self):
        return self._math

    @math.setter
    def math(self, value):
        if value < 0:
            raise ValueError("分数不能为负数")
        self._math = value


if __name__ == "__main__":
    score_instance = Score(10)
    score_instance.math = -10
    print(score_instance.math)