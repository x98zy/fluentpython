"""在嵌套的字典中如果要获取嵌套中的键值就要写类似于dict[key1][key2]等语句
通过将键值转为属性可用obj.attr来获取"""

from collections import abc

class FrozenJson():
    def __init__(self,mapping):
        self._data=dict(mapping)
    #通过obj.attr会调用__getattr__魔法函数
    def __getattr__(self, item):
        if hasattr(self._data,item):
            return getattr(obj,item)
        else:
            return FrozenJson.build(self._data[item])
    @classmethod
    def build(cls,obj):
        if isinstance(obj,abc.Mapping):
            return cls(obj)
        if isinstance(obj,abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


#使用__new__方法进行改进
class FrozenJsonAgain():
    def __new__(cls,arg):
        if isinstance(arg,abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg,abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg
    def __init__(self,mapping):
        self._data=dict(mapping)
    def __getattr__(self, item):
        if hasattr(self._data,item):
            return getattr(obj,item)
        else:
            return FrozenJsonAgain(self._data[item])


if __name__=="__main__":
    dict1={"grade":"primary","teacher":{"Alice":1,"Bob":2,"Jack":3},"students":["Fang","Justbin"]}
    frozen=FrozenJsonAgain(dict1)
    print(frozen.students)