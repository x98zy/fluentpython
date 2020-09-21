"""本篇代码旨在演示多重装饰器的效果"""

def a(func):
    def inner():
        print("a")
    return inner

def b(func):
    def inner():
        print("b")
    return inner

def c(func):
    def inner():
        print("c")
    return inner
@a
@b
@c
def test():
    print("function")

test()#a
print(test)#<function a.<locals>.inner at 0x036973D8>