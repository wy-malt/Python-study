# coder:也
# 开发时间:2022/10/5 15:22

# Python内置的一种数据类型是列表：list。list是一种有序的集合，
# 可以随时添加和删除其中的元素
classmates = ['wang1', 'li2', 'zhang3']
# 用len()函数可以获得list元素的个数
print(len(classmates))
# 用索引来访问list中每一个位置的元素，记得索引是从0开始的
print(classmates[1])
# print(classmates[3])  IndexError: list index out of range
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(classmates[-1])
# 以此类推，可以获取倒数第2个、倒数第3个
print(classmates[-2])
print(classmates[-3])
# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('liu4')
print(classmates)   # ['wang1', 'li2', 'zhang3', 'liu4']
# 也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'jin5')
print(classmates)   # ['wang1', 'jin5', 'li2', 'zhang3', 'liu4']
# 要删除list末尾的元素，用pop()方法
classmates.pop()
print(classmates)   # ['wang1', 'jin5', 'li2', 'zhang3']
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(2)
print(classmates)   # ['wang1', 'jin5', 'zhang3']
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'shsh6'
print(classmates)   # ['wang1', 'shsh6', 'zhang3']

# list里面的元素的数据类型也可以不同
L = ['list', 65, True, 68.24]
# list元素也可以是另一个list
s = ['java', [1, 2, 3], 5, 98.6]
print(len(s))
# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0
L1 = []
print(len(L1))


# 另一种有序列表叫元组：tuple。
# tuple和list非常类似，但是tuple一旦初始化就不能修改
cm = ('wang1', '5', 6)  # 现在，cm这个tuple不能变了，它也没有append()，insert()这样的方法
# 其他获取元素的方法和list是一样的，你可以正常地使用cm[0]，cm[-1]，但不能赋值成另外的元素
'''
不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。
如果可能，能用tuple代替list就尽量用tuple
'''
# 当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1, 2)
# 如果要定义一个空的tuple，可以写成()
d = ()
# 但是，要定义一个只有1个元素的tuple，如果你这么定义
w = (1) # 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，
# 又可以表示数学公式中的小括号，这就产生了歧义

# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
r = (1,)





























































