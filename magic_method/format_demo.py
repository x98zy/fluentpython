#format格式学习

#不指定位置，按照默认顺序
print("{} {}".format("hello","world"))
#结果： helll world

#指定位置
print("{0} {1}".format("hello","world"))
print("{0} {1} {0}".format("hello","world"))
#结果 hello world
#hello world hello

#指定名字
print("name:{name},url:{url}".format(name="python",url="www.python.com"))
#或者
site={"name":"python","url":"www.python.com"}
print("name:{name},url:{url}".format(**site))

#格式化数字的多种形式
#保留小数点后两位
print("{:.2f}".format(2.33434))
#结果：2.33

#不带小数
#此种格式化的特点是在:前指定元素的位置，在:后指定格式化的形式
print("{:.0f}".format(3.43435,4.3343))
#结果:3
print("{1:.0f}".format(3.43435,4.3343))
#结果4

#{:0>2d}往数字右边填充0，字符宽度为2位
print("{:0>3d}".format(3))
#结果003

