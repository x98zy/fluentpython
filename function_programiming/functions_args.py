#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File   ：functions_args
# @IDE    ：pycharm
# @Author ：xz98y
# @Date   ：2022/2/7 22:33
from typing import List,Optional


def tag(name, *content, cls=None, **attrs):
    attr_str = ""
    if cls:
        attrs["class"] = cls
    if attrs:
        attr_str = "".join([' %s="%s"' % (key, value) for key, value in sorted(attrs.items())])
    if content:
        return "\n".join(["<%s%s>%s</%s>" % (name, attr_str, con, name) for con in content])
    else:
        return "<%s%s />" % (name, attr_str)

if __name__ == "__main__":
    print(tag("b", id="test"))
    print(tag("b", "hello", "world", cls="silder"))
    # 传入可变关键字参数，同名的键会被绑定到对应的定位参数，其余的会被attrs捕获
    my_tag = {"name": "img", "id": "sid", "src": "test.jpg"}
    print(tag(**my_tag))
