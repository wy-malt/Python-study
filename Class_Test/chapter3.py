# coder:也
# 开发时间:2022/11/21 10:01

listname = [3,2.0,5,84,2.66]
print(listname)

print(5555555)

print(list(range(5,10)))
print(list({'a':97, 'b':98, 'c':99}))   # ['a', 'b', 'c']
print(list({'a':97, 'b':98, 'c':99}.items()))   # [('a', 97), ('b', 98), ('c', 99)]
x = list()
x.append("xasd")
print(x)
x = list()
x.append(1561651)
print(x)
x.pop()
print(x)

'''
方法	说明
append(x)	将x追加至列表尾部
extend(L)	将列表L中所有元素追加至列表尾部
insert(index, x)	在列表index位置处插入x，该位置后面的所有元素后移并且在列表中的索引加1，如果index为正数且大于列表长度则在列表尾部追加x，如果index为负数且小于列表长度的相反数则在列表头部插入元素x
remove(x)	在列表中删除第一个值为x的元素，该元素之后所有元素前移并且索引减1，如果列表中不存在x则抛出异常
pop([index])	删除并返回列表中下标为index的元素，如果不指定index则默认为-1，弹出最后一个元素；如果弹出中间位置的元素则后面的元素索引减1；如果index不是[-L, L]区间上的整数则抛出异常
clear()	清空列表，删除列表中所有元素，保留列表对象
index(x)	返回列表中第一个值为x的元素的索引，若不存在值为x的元素则抛出异常
count(x)	返回x在列表中的出现次数
reverse()	对列表所有元素进行原地逆序，首尾交换
sort(key=None, reverse=False)	对列表中的元素进行原地排序，key用来指定排序规则，reverse为False表示升序，True表示降序
copy()	返回列表的浅复制
'''
x = [1,2,5,7,4,225,5,1,5,1,5,3,5,4,5,6,5,5]
x.remove(5)
# x.clear()
print(x)
'''
列表方法count()用于返回列表中指定元素出现的次数；index()用于返回指定元素在列表中首次出现的位置
'''
print(x.index(5))
print(x.count(5))
'''
列表对象的sort()方法用于按照指定的规则对所有元素进行排序；reverse()方法用于将列表所有元素逆序或翻转
'''
x = list(range(11))
import random
random.shuffle(x)   # 把列表x中的元素随机乱序
print(x)
x.sort(key=lambda i: len(str(i)),reverse=True)
print(x)
x.sort(key=lambda i: len(str(i)),reverse=False)
print(x)
x.sort(key=str)
print(x)
x.sort()
print(x)
x.reverse()
print(x)

'''
加法运算符+也可以实现列表增加元素的目的，但不属于原地操作，而是返回新列表，涉及大量元素的复制，效率非常低。使用复合赋值运算符+=实现列表追加元素时属于原地操作，与append()方法一样高效。
>>> x = [1, 2, 3]
>>> id(x)
53868168
>>> x = x + [4]                        #连接两个列表
>>> x
[1, 2, 3, 4]
>>> id(x)                              #内存地址发生改变
53875720
>>> x += [5]                           #为列表追加元素
>>> x
[1, 2, 3, 4, 5]
>>> id(x)                              #内存地址不变
53875720

乘法运算符*可以用于列表和整数相乘，表示序列重复，返回新列表。运算符*=也可以用于列表元素重复，属于原地操作。
>>> x = [1, 2, 3, 4]
>>> id(x)
54497224
>>> x = x * 2                           #元素重复，返回新列表
>>> x
[1, 2, 3, 4, 1, 2, 3, 4]
>>> id(x)                               #地址发生改变
54603912
>>> x *= 2                              #元素重复，原地进行
>>> x
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> id(x)                               #地址不变
54603912

成员测试运算符in可用于测试列表中是否包含某个元素，查询时间随着列表长度的增加而线性增加，而同样的操作对于集合而言则是常数级的。
>>> 3 in [1, 2, 3]
True
>>> 3 in [1, 2, '3']
False


'''
x = [2,4,5]
y = [5,7,8]
z = zip(x,y)
print(list(z))  # [(2, 5), (4, 7), (5, 8)]
'''
max()、min()函数用于返回列表中所有元素的最大值和最小值，
sum()函数用于返回列表中所有元素之和；
len()函数用于返回列表中元素个数，zip()函数用于将多个列表中元素重新组合为元组并返回包含这些元组的zip对象；
enumerate()函数返回包含若干下标和值的迭代对象；
map()函数把函数映射到列表上的每个元素，filter()函数根据指定函数的返回值对列表元素进行过滤；
all()函数用来测试列表中是否所有元素都等价于True，any()用来测试列表中是否有等价于True的元素。
标准库functools中的reduce()函数以及标准库itertools中的compress()、groupby()、dropwhile()等大量函数也可以对列表进行操作
'''

'''
列表推导式在逻辑上等价于一个循环语句，只是形式上更加简洁。例如：
[expression for expr1 in sequence1]

>>> aList = [x*x for x in range(10)]
相当于
>>> aList = []
>>> for x in range(10):
        aList.append(x*x)
'''

x = [i**2 for i in range(0,10)]
print(x)    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
freshfruit = [' banana', ' loganberry ', 'passion fruit ']
aList = [w.strip() for w in freshfruit]
print(aList)    # 返回删除前导和尾随空格的字符串副本 ['banana', 'loganberry', 'passion fruit']

s = sum([2**i for i in range(64)])
print(s)    # 18446744073709551615

'''
实现嵌套列表的平铺
>>> vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9] 

在这个列表推导式中有2个循环，其中第一个循环可以看作是外循环，执行的慢；而第二个循环可以看作是内循环，执行的快。上面代码的执行过程等价于下面的写法：
>>> vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> result = []
>>> for elem in vec:
        for num in elem:
            result.append(num)
>>> result
[1, 2, 3, 4, 5, 6, 7, 8, 9]

过滤不符合条件的元素
在列表推导式中可以使用if子句对列表中的元素进行筛选，只在结果列表中保留符合条件的元素。

下面的代码用于从列表中选择符合条件的元素组成新的列表：
>>> aList = [-1, -4, 6, 7.5, -2.3, 9, -11]
>>> [i for i in aList if i>0]                          #所有大于0的数字
[6, 7.5, 9]

>>> bList = [item%3 for item in aList]                 #aList对3取余
[2, 2, 0, 1.5, 0.7000000000000002, 0, 1]


'''
'''
问题解决：已知有一个包含一些同学成绩的字典，
现在需要计算所有成绩的最高分、最低分、平均分，并查找所有最高分同学
'''
scores = {"Zhang San": 45, "Li Si": 78, "Wang Wu": 40, "Zhou Liu": 96,
              "Zhao Qi": 65, "Sun Ba": 90, "Zheng Jiu": 78, "Wu Shi": 99,
              "Dong Shiyi": 60}
hightest = max(scores.values())
lowest = min(scores.values())
average = sum(scores.values())/len(scores)
names = [name for name,s in scores.items() if s==hightest]
print(hightest,lowest,average)
print(names)

'''
访问列表元素的另外一种方法，访问一定范围内的元素；（对元组和字符串同样适应）
在形式上，切片使用2个冒号分隔的3个数字来完成。
listName[start:end:step]
第一个数字start表示切片开始位置，默认为0；
第二个数字end表示切片截止（但不包含）位置（默认为列表长度）；
第三个数字step表示切片的步长（默认为1）。
当start为0时可以省略，当end为列表长度时可以省略，当step为1时可以省略，省略步长时还可以同时省略最后一个冒号。
当step为负整数时，表示反向切片
'''
'''
使用切片为列表增加元素
可以使用切片操作在列表任意位置插入新元素，不影响列表对象的内存地址，属于原地操作。
>>> aList = [3, 5, 7]
>>> aList[len(aList):]
[]
>>> aList[len(aList):] = [9]       #在列表尾部增加元素
>>> aList[:0] = [1, 2]             #在列表头部插入多个元素
>>> aList[3:3] = [4]               #在列表中间位置插入元素
>>> aList
[1, 2, 3, 4, 5, 7, 9]

使用切片替换和修改列表中的元素
>>> aList = [3, 5, 7, 9]
>>> aList[:3] = [1, 2, 3]           #替换列表元素，等号两边的列表长度相等
>>> aList
[1, 2, 3, 9]
>>> aList[3:] = [4, 5, 6]           #切片连续，等号两边的列表长度可以不相等
>>> aList
[1, 2, 3, 4, 5, 6]
>>> aList[::2] = [0]*3              #隔一个修改一个
>>> aList
[0, 2, 0, 4, 0, 6]
>>> aList[::2] = ['a', 'b', 'c']    #隔一个修改一个
>>> aList
['a', 2, 'b', 4, 'c', 6]

>>> aList[1::2] = range(3)             #序列解包的用法
>>> aList
['a', 0, 'b', 1, 'c', 2]
>>> aList[1::2] = map(lambda x: x!=5, range(3))
>>> aList
['a', True, 'b', True, 'c', True]
>>> aList[1::2] = zip('abc', range(3)) #map、filter、zip对象都支持这样的用法
>>> aList
['a', ('a', 0), 'b', ('b', 1), 'c', ('c', 2)]
>>> aList[::2] = [1]                   #切片不连续时等号两边列表长度必须相等
ValueError: attempt to assign sequence of size 1 to extended slice of size 3


'''

g = ((i+2)**2 for i in range(10))
for item in g:
    print(item,end=' ')

'''
字典（dictionary）是包含若干“键:值”元素的无序可变序列，字典中的每个元素包含用冒号分隔开的“键”和“值”两部分，表示一种映射或对应关系，也称关联数组。定义字典时，每个元素的“键”和“值”之间用冒号分隔，不同元素之间用逗号分隔，所有的元素放在一对大括号“｛｝”中。
字典中元素的“键”可以是Python中任意不可变数据，例如整数、实数、复数、字符串、元组等类型等可哈希数据，但不能使用列表、集合、字典或其他可变类型作为字典的“键”。另外，字典中的“键”不允许重复，而“值”是可以重复的
'''
'''
使用赋值运算符“=”将一个字典赋值给一个变量即可创建一个字典变量。
dictName = {key1:value1, key2:value2, …, Keyn: valuen}
>>> aDict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}

也可以使用内置类dict以不同形式创建字典。
>>> x = dict()                               #空字典
>>> type(x)                                  #查看对象类型
<class 'dict'>
>>> x = {}                                   #空字典
>>> keys = ['a', 'b', 'c', 'd']
>>> values = [1, 2, 3, 4]
>>> dictionary = dict(zip(keys, values))     #根据已有数据创建字典
>>> d = dict(name='Dong', age=39)            #以关键参数的形式创建字典
>>> aDict = dict.fromkeys(['name', 'age', 'sex'])
                             #以给定内容为“键”，创建“值”为空的字典
>>> aDict
{'name': None, 'age': None, 'sex': None}
'''

'''
OrderedDict类
Python内置字典dict是无序的，如果需要一个可以记住元素插入顺序的字典，可以使用collections.OrderedDict
'''
print()
import collections
x = collections.OrderedDict()
x['a'] = 1
x['b'] = 2
x['c'] = 3
print(x)    # OrderedDict([('a', 1), ('b', 2), ('c', 3)])
key = 'abcd'
values = [1,2,3,4]
aDict = {k:v for k,v in zip(key,values)}
print(aDict)
'''
集合（set）属于Python无序可变序列，使用一对大括号作为定界符，元素之间使用逗号分隔，同一个集合内的每个元素都是唯一的，元素之间不允许重复。
集合中只能包含数字、字符串、元组等不可变类型（或者说可哈希）的数据，而不能包含列表、字典、集合等可变类型的数据。
'''
a = {(1,),6,'sss'}
print(a)
'''
也可以使用函数set()函数将列表、元组、字符串、range对象等其他可迭代对象转换为集合，如果原来的数据中存在重复元素，则在转换为集合的时候只保留一个；如果原序列或迭代对象中有不可哈希的值，无法转换成为集合，抛出异常
'''
a_set = set([1,5,5,4,7,7,8,4,2,1,6,9,5,4])
print(a_set)    # {1, 2, 4, 5, 6, 7, 8, 9}
a_set.discard(5)
print(a_set)    # 删除元素，不存在则忽略该操作
'''
pop()方法用于随机删除并返回集合中的一个元素，如果集合为空则抛出异常；
remove()方法用于删除集合中的元素，如果指定元素不存在则抛出异常；
discard()用于从集合中删除一个特定元素，如果元素不在集合中则忽略该操作；
clear()方法清空集合删除所有元素。
>>> s.discard(5)                     #删除元素，不存在则忽略该操作
>>> s
{1, 2, 3, 4}
>>> s.remove(5)                      #删除元素，不存在就抛出异常
KeyError: 5
>>> s.pop()                          #删除并返回一个元素
1
'''
b_set = set([8,5,7,49,6,5,4,4,5])
print(a_set | b_set)    # 并集 {1, 2, 4, 5, 6, 7, 8, 9, 49}
print(a_set.union(b_set))   # 并集 {1, 2, 4, 5, 6, 7, 8, 9, 49}
print(a_set & b_set)    # 交集 {8, 4, 6, 7}
print(a_set.intersection(b_set))    # 交集 {8, 4, 6, 7}
print(a_set - b_set)    # 差集 {1, 2, 9}
print(a_set ^ b_set)    # 对称差集 {1, 2, 5, 9, 49}
a,b,c = 'ABC'
print(a,b,c)    # 字符串也支持序列解包
'''
可以使用序列解包功能对多个变量同时进行赋值。
>>> x, y, z = 1, 2, 3                   #多个变量同时赋值
>>> v_tuple = (False, 3.5, 'exp')
>>> (x, y, z) = v_tuple
>>> x, y, z = v_tuple
>>> x, y = y, x                         #交换两个变量的值
>>> x, y, z = range(3)                  #可以对range对象进行序列解包
>>> x, y, z = iter([1, 2, 3])           #使用迭代器对象进行序列解包
>>> x, y, z = map(str, range(3))        #使用可迭代的map对象进行序列解包

>>> a = [1, 2, 3]
>>> b, c, d = a                        #列表也支持序列解包的用法
>>> x, y, z = sorted([1, 3, 2])        #sorted()函数返回排序后的列表
>>> s = {'a':1, 'b':2, 'c':3}
>>> b, c, d = s.items()                #这是Python 3.5之前的版本执行结果
                                       #Python 3.6之后的版本略有不同
>>> b
('c', 3)
>>> b, c, d = s                        #使用字典时不用太多考虑元素的顺序
>>> b
'c'
>>> b, c, d = s.values()
>>> print(b, c, d)
1 3 2
>>> a, b, c = 'ABC'                    #字符串也支持序列解包
>>> print(a, b, c)
A B C
'''
'''
使用序列解包可以很方便地同时遍历多个序列。
>>> keys = ['a', 'b', 'c', 'd']
>>> values = [1, 2, 3, 4]
>>> for k, v in zip(keys, values):
    print(k, v)
a 1
b 2
c 3
d 4

对内置函数enumerate()返回的迭代对象进行遍历：
>>> x = ['a', 'b', 'c']
>>> for i, v in enumerate(x):
    print('The value on position {0} is {1}'.format(i,v))
The value on position 0 is a
The value on position 1 is b
The value on position 2 is c

使用序列解包遍历字典元素：
>>> s = {'a':1, 'b':2, 'c':3}
>>> for k, v in s.items():        #字典中每个元素包含“键”和“值”两部分
    print(k, v)
a 1
c 3
b 2
'''





























































