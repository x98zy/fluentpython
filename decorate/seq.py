"""序列的相关操作"""

#1:切片赋值

seq_list=[1,2,3,4,5,6]
seq_list[0:2]=4,6
#或者
seq_list[0:2]=[4,6]
print(seq_list)

#序列的*，+操作

seq_list=[1,2,3]
copy_list=seq_list*3
print(copy_list)
print(id(seq_list))
seq_list*=3
#对于可变序列，*=，+=等增量操作是在原序列的基础上进行的操作，并没有创建新的对象
print(id(seq_list))

#对于不可变序列，*=，+=等操作是创建了一个新对象并将新对象关联到原有变量上
seq_tuple=(1,2,3)
print(id(seq_tuple))
seq_tuple*=3
print(id(seq_tuple))

#序列*，+等操作的一些误区

#对于一个可变序列中本身含有可变序列，那么使用*操作，其实最后的可变序列中含有的都是同一个可变序列的引用
seq_list=[["_","_","_"]]*3
seq_list[1][2]="+"
print(seq_list)
#结果：[['_', '_', '+'], ['_', '_', '+'], ['_', '_', '+']]

#如果要实现上述效果可使用列表推导

seq_list=[["_"]*3 for i in range(3)]
seq_list[1][2]="+"
print(seq_list)
#结果：[['_', '_', '_'], ['_', '_', '+'], ['_', '_', '_']]

