#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File   ：function_example
# @IDE    ：pycharm
# @Author ：xz98y
# @Date   ：2022/2/7 21:40

# 高阶函数，使用其他函数作为参数或者将函数作为结果返回的函数就是高阶函数
# 例如sorted, map, filter

fruit_list = ["apple", "banana", "orange", "strabictch"]
print(sorted(fruit_list, key=len))


def fact(n: int) -> int:
    return 1 if n < 2 else n * fact(n-1)

print(list(map(fact, range(6))))