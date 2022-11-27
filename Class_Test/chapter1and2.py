# coder:也
# 开发时间:2022/11/19 21:53

print("Hello World")
i = 4 + 5 + 6\
    + 5     # \是续行符
print(i)

'''
对象是python语言中最基本的概念，在python中处理的一切都是对象。
python中有许多内置对象可供编程者使用，内置对象可直接使用，如数字、字符串、列表、del等。
非内置对象需要导入模块才能使用，如正弦函数sin(x)，随机数产生函数random( )等。
'''

i = 3 + 4j
print(i)

s = '''bcisbci'''
s1 = '\t sdcs \0111'
print(s1)
print(s)
print(r'\t sdcs \0111')
print(R'\t sdcs \0111')
b = b'Hello World'
print(b)

# Python中变量是存放数据值的容器，是对存放在内存中的数据的引用。
# Python中的变量并不直接存储值，而是存储了值的内存地址或者引用，这也是变量类型随时可以改变的原因
# Python采用的是基于值的内存管理方式，如果为不同变量赋值为相同值（仅适用于-5至256的整数和短字符串），这个值在内存中只有一份，多个变量指向同一块内存地址。

y = isinstance(3, int)             #测试对象是否是某个类型的实例
print(y)
x = 'Hello world.'
print(type(x))                 #查看变量类型

# 变量名必须以汉字、英文字母或下划线开头，但以下划线开头的变量在Python中有特殊含义
acavav鱼鱼鱼  = 11
print(acavav鱼鱼鱼)

'''
Python 3.6.x支持在数字中间位置使用单个下划线作为分隔来提高数字的可读性，类似于数学上使用逗号作为千位分隔符。
在Python数字中单个下划线可以出现在中间任意位置，但不能出现开头和结尾位置，也不能使用多个连续的下划线。
'''
'''
0.4-0.1
0.30000000000000004
0.1-0.2 ==-0.1
True
0.4-0.1==0.3
False
0.3-0.1==0.2
False
import math
math.isclose(0.4-0.1,0.3)
True
x = 3 + 5j
x.imag  虚部
5.0
x.real  实部
3.0
x.conjugate()   共轭复数
(3-5j)
'''

# Python标准库fractions中的Fraction对象支持分数及其运算。
from fractions import Fraction
x = Fraction(3,5)
y = Fraction(3,7)
print(x)    # 3/5
print(x**2)     # 9/25
print(x.numerator)  # 3 查看分子
print(x.denominator)  # 5 查看分母
print(x+y)      # 36/35

# 标准库fractions和decimal中提供的Decimal类实现了更高精度实数的运算。

# from fractions import Decimal Pyhton3.10找不到

x = 'ghgh''ghghg'   # 该方式适用于字符串常量
print(x)
# x = x'dcsc'   报错 该方式不适用于字符串变量
print(type('Hello world'))    # <class 'str'>  默认字符串类型为str
print(type(b'cbwcuyuecbubc'))   # <class 'bytes'> 在定界符前加上字母b表示字节串

print(x.encode('utf-8'))    # b'ghghghghg'
y = b'dfv'
print(y.decode('utf-8'))    # dfv

x_list = [1,2,3]    # 列表
x_tuple = (1,2,3)   # 元组
x_dict = {'a':97, 'b':98, 'c':99}   # 字典
x_set = {1,2,3}     # 集合
print(x_list[1])
print(x_tuple[1])
print(x_dict['a'])
print(3 in x_set)       # 成员测试

print(xx := x)      # 海象运算符
x = 5
print((lambda x : x**2)(2))

'''
运算符	功能说明
:=	赋值运算，Python 3.8新增，俗称海象运算符
Lambda [parameter]: expression	用来定义lambda表达式，功能相当于函数，parameter相当于函数参数，可以没有；expression表达式的值相当于函数返回值
value1 if condition else value2	用来表示一个二选一的表达式，其中value1、condition、value2都为表达式，如果condition的值等价于True则整个表达式的值为value1的值，否则整个表达式的值为value2的值
or	逻辑或运算符，以exp1 or exp2为例，如果exp1的值等价于True则返回exp1的值，否则返回exp2的值
and	逻辑与运算符，以exp1 and exp2为例，如果exp1的值等价于False则返回exp1的值，否则返回exp2的值
'''
# value1 if condition else value2
# 用来表示一个二选一的表达式，其中value1、condition、value2都为表达式，如果condition的值等价于True则整个表达式的值为value1的值，否则整个表达式的值为value2的值
print(1 if 1 < 2 else 2)
# print(x@x)

# +运算符除了用于算术加法以外，还可以用于列表、元组、字符串的连接，但不支持不同类型的对象之间相加或连接。
print([1,2] + [3,4])
print((1,2,3) + (4,))
print('1,2,3' + ',4')
print(True + 3)     # 4 Python内部把True当作1处理
print(False + 1)    # 1 把False当0处理

'''
*运算符除了表示算术乘法，还可用于列表、元组、字符串这几个序列类型与整数的乘法，表示序列元素的重复，生成新的序列对象。字典和集合不支持与整数的相乘，因为其中的元素是不允许重复的。
>>> True * 3
3
>>> False * 3
0
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> (1, 2, 3) * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> 'abc' * 3
'abcabcabc'
'''
'''
运算符/和//在Python中分别表示算术除法和算术求整商（floor division）。
>>> 3 / 2                    #数学意义上的除法
1.5
>>> 15 // 4                  #如果两个操作数都是整数，结果为整数
3
>>> 15.0 // 4                #如果操作数中有实数，结果为实数形式的整数值
3.0
>>> -15//4                   #向下取整
-4
'''
'''
%运算符可以用于整数或实数的求余数运算，还可以用于字符串格式化，但是这种用法并不推荐。
>>> 789 % 23                   #余数
7
>>> 123.45 % 3.2               #可以对实数进行余数运算，注意精度问题
1.849999999999996
>>> '%c, %d' % (65, 65)        #把65分别格式化为字符和整数
'A, 65'
>>> '%f,%s' % (65, 65)         #把65分别格式化为实数和字符串
'65.000000,65'
'''
'''
**运算符表示幂乘：
>>> 3 ** 2                    #3的2次方，等价于pow(3, 2)
9
>>> pow(3, 2, 8)              #等价于(3**2) % 8
1
>>> 9 ** 0.5                  #9的0.5次方，平方根
3.0
>>> (-9) ** 0.5               #可以计算负数的平方根
(1.8369701987210297e-16+3j)
'''
'''
Python关系运算符最大的特点是可以连用，其含义与我们日常的理解完全一致。使用关系运算符的一个最重要的前提是，操作数之间必须可比较大小。例如把一个字符串和一个数字进行大小比较是毫无意义的，所以Python也不支持这样的运算。
>>> 1 < 3 < 5                    #等价于1 < 3 and 3 < 5
True
>>> 3 < 5 > 2
True
>>> 1 > 6 < 8
False
>>> 1 > 6 < math.sqrt(9)         #具有惰性求值或者逻辑短路的特点
False
>>> 1 < 6 < math.sqrt(9)         #还没有导入math模块，抛出异常
NameError: name 'math' is not defined
>>> import math
>>> 1 < 6 < math.sqrt(9)
False
'''

print('dscws' > 'd')    # True
'''
>>> 'Hello' > 'world'              #比较字符串大小
False
>>> [1, 2, 3] < [1, 2, 4]          #比较列表大小
True
>>> 'Hello' > 3                    #字符串和数字不能比较
TypeError: unorderable types: str() > int()
>>> {1, 2, 3} < {1, 2, 3, 4}       #测试是否子集
True
>>> {1, 2, 3} == {3, 2, 1}         #测试两个集合是否相等
True
>>> {1, 2, 4} > {1, 2, 3}          #集合之间的包含测试
False
>>> {1, 2, 4} < {1, 2, 3}
False
>>> {1, 2, 4} == {1, 2, 3}
False
'''
'''
成员测试运算符in用于成员测试，即测试一个对象是否为另一个对象的元素。

>>> 3 in [1, 2, 3]                #测试3是否存在于列表[1, 2, 3]中
True
>>> 5 in range(1, 10, 1)          #range()是用来生成指定范围数字的内置函数
True
>>> 'abc' in 'abcdefg'            #子字符串测试
True
>>> for i in (3, 5, 7):           #循环，成员遍历
    print(i, end='\t')
3	5	7
'''

for i in (2,4,6):
    print(i, end='\n')
'''
同一性测试运算符is用来测试两个对象是否是同一个，如果是则返回True，否则返回False。如果两个对象是同一个，二者具有相同的内存地址。

>>> 3 is 3
True
>>> x = [300, 300, 300]
>>> x[0] is x[1]                #基于值的内存管理，同一个值在内存中只有一份
True
>>> x = [1, 2, 3]
>>> y = [1, 2, 3]
>>> x is y                      #上面形式创建的x和y不是同一个列表对象
False
>>> x[0] is y[0]
True
'''

'''
位运算符只能用于整数，其内部执行过程为：首先将整数转换为二进制数，然后右对齐，必要的时候左侧补0，按位进行运算，最后再把计算结果转换为十进制数字返回。
位运算符有位与（&）、位或（|）、位异或（^）、取反（~）、左移（<<）、右移（>>）。
位与运算规则为1&1=1、1&0=0&1=0&0=0，位或运算规则为1|1=1|0=0|1=1、0|0=0，位异或运算规则为1^1=0^0=0、1^0=0^1=1。
左移位时右侧补0，每左移一位相当于乘以2；右移位时左侧补0，每右移一位相当于整除以2
'''

print({1,2,3}-{4,5,6})
print({1,2,3}^{4,5,6})
'''
集合的交集（&）、并集（|）、对称差集（^）运算借助于位运算符来实现，而差集则使用减号运算符实现（注意，并集运算符不是加号）。

>>> {1, 2, 3} | {3, 4, 5}          #并集，自动去除重复元素
{1, 2, 3, 4, 5}
>>> {1, 2, 3} & {3, 4, 5}          #交集
{3}
>>> {1, 2, 3} ^ {3, 4, 5}          #对称差集
{1, 2, 4, 5}
>>> {1, 2, 3} - {3, 4, 5}          #差集
{1, 2}
'''

'''
>>> 3>5 and a>3              #注意，此时并没有定义变量a
False
>>> 3>5 or a>3               #3>5的值为False，所以需要计算后面表达式
NameError: name 'a' is not defined
>>> 3<5 or a>3               #3<5的值为True，不需要计算后面表达式
True
>>> 3 and 5                  #最后一个计算的表达式的值作为整个表达式的值
5
>>> 3 and 5>2
True
>>> 3 not in [1, 2, 3]       #逻辑非运算not
False
>>> 3 is not 5               #not的计算结果只能是True或False之一
True
>>> not 3
False
>>> not 0
True
'''

'''
从Python 3.5开始增加了一个新的矩阵相乘运算符@，不过由于Python没有内置的矩阵类型，所以该运算符常与扩展库numpy一起使用。另外，@符号还可以用来表示修饰器的用法。

>>> import numpy             #numpy是用于科学计算的Python扩展库
>>> x = numpy.ones(3)        #ones()函数用于生成全1矩阵，参数表示矩阵大小
>>> m = numpy.eye(3)*3       #eye()函数用于生成单位矩阵
>>> m[0,2] = 5               #设置矩阵指定位置上元素的值
>>> m[2, 0] =3
>>> x @ m                    #矩阵相乘
array([ 6.,  3.,  8.])
'''


'''
关键字	含义
False	常量，逻辑假
None	常量，空值
True	常量，逻辑真
and	逻辑与运算
as	在import或except语句中给对象起别名
assert	断言，用来确认某个条件必须满足，可用来帮助调试程序
break	用在循环中，提前结束break所在层次的循环
class	用来定义类
continue	用在循环中，提前结束本次循环
def	用来定义函数
del	用来删除对象或对象成员
elif	用在选择结构中，表示else if的意思
else	可以用在选择结构、循环结构和异常处理结构中
except	用在异常处理结构中，用来捕获特定类型的异常
finally	用在异常处理结构中，用来表示不论是否发生异常都会执行的代码
for	构造for循环，用来迭代序列或可迭代对象中的所有元素
from	明确指定从哪个模块中导入什么对象，例如from math import sin；
还可以与yield一起构成yield表达式
global	定义或声明全局变量
if	用在选择结构中
import	用来导入模块或模块中的对象
in	成员测试
is	同一性测试
lambda	用来定义lambda表达式，类似于函数
nonlocal	用来声明nonlocal变量
not	逻辑非运算
or	逻辑或运算
pass	空语句，执行该语句时什么都不做，常用作占位符
raise	用来显式抛出异常
return	在函数中用来返回值，如果没有指定返回值，表示返回空值None
try	在异常处理结构中用来限定可能会引发异常的代码块
while	用来构造while循环结构，只要条件表达式等价于True就重复执行限定的代码块
with	上下文管理，具有自动管理资源的功能
yield	在生成器函数中用来返回值
'''

print(dir(__builtins__))

print(bin(116))     # 0b1110100 二进制串
print(oct(116))     # 0o164     八进制串
print(hex(116))     # 0x74      十六进制串

'''
ord()和chr()是一对功能相反的函数，ord()用来返回单个字符的Unicode码，而chr()则用来返回Unicode编码对应的字符，str()则直接将其任意类型参数转换为字符串。
>>> ord('a')           #查看指定字符的Unicode编码
97
>>> chr(65)            #返回数字65对应的字符
'A'
>>> chr(ord('A')+1)    #Python不允许字符串和数字之间的加法操作
'B'
>>> chr(ord('国')+1)   #支持中文
'图'
>>> ord('董')          #这个用法仅适用于Python 3.x
33891
>>> ord('付')
20184
>>> ord('国')
22269

>>> ''.join(map(chr, (33891, 20184, 22269)))
'董付国'
>>> str(1234)                      #直接变成字符串
'1234'
>>> str([1,2,3])
'[1, 2, 3]'
>>> str((1,2,3))
'(1, 2, 3)'
>>> str({1,2,3})
'{1, 2, 3}'
'''
'''
内置类ascii可以把对象转换为ASCII码表示形式，必要的时候使用转义字符来表示特定的字符。

>>> ascii('a')
"'a'"
>>> ascii('董付国')
"'\\u8463\\u4ed8\\u56fd'"
>>> eval(_)                        #对字符串进行求值
'董付国'
'''
'''
list()、tuple()、dict()、set()、frozenset()用来把其他类型的数据转换成为列表、元组、字典、可变集合和不可变集合，或者创建空列表、空元组、空字典和空集合。
>>> list(range(5))               #把range对象转换为列表
[0, 1, 2, 3, 4]
>>> tuple(_)                     #一个下划线表示上一次正确的输出结果
(0, 1, 2, 3, 4)
>>> dict(zip('1234', 'abcde'))   #创建字典
{'1': 'a', '2': 'b', '3': 'c', '4': 'd’} 
>>> set('1112234')               #创建可变集合，自动去除重复
{'4', '2', '3', '1'}
>>> _.add('5')
>>> _
{'2', '1', '3', '4', '5'}
>>> frozenset('1112234')         #创建不可变集合，自动去除重复
frozenset({'2', '1', '3', '4'})
>>> _.add('5')                   #不可变集合frozenset不支持元素添加与删除
AttributeError: 'frozenset' object has no attribute 'add'
'''

print(list(range(5)))
'''
内置函数type()和isinstance()可以用来判断数据类型，常用来对函数参数进行检查，可以避免错误的参数类型导致函数崩溃或返回意料之外的结果。
>>> type(3)                                 #查看3的类型
<class 'int'>
>>> type([3])                               #查看[3]的类型
<class 'list'>
>>> type({3}) in (list, tuple, dict)        #判断{3}是否为list,tuple或dict类型的实例
False
>>> type({3}) in (list, tuple, dict, set)   #判断{3}是否为list,tuple,dict或set的实例
True
>>> isinstance(3, int)                      #判断3是否为int类型的实例
True
>>> isinstance(3j, int)
False
>>> isinstance(3j, (int, float, complex))   #判断3是否为int,float或complex类型
True
'''
'''
max()、min()、sum()这三个内置函数分别用于计算列表、元组或其他包含有限个元素的可迭代对象中所有元素最大值、最小值以及所有元素之和。
sum()默认（可以通过start参数来改变）支持包含数值型元素的序列或可迭代对象，max()和min()则要求序列或可迭代对象中的元素之间可比较大小。

>>> from random import randint
>>> a = [randint(1,100) for i in range(10)]  #包含10个[1,100]之间随机数的列表
>>> print(max(a), min(a), sum(a))            #最大值、最小值、所有元素之和
>>> sum(a) / len(a)                          #平均值
'''
from random import randint
a = [randint(1,100) for i in range(10)]
print(max(a), min(a), sum(a))
print(sum(a) / len(a))

'''
函数max()和min()还支持default参数和key参数，其中default参数用来指定可迭代对象为空时默认返回的最大值或最小值，而key参数用来指定比较大小的依据或规则，可以是函数或lambda表达式。函数sum()还支持start参数，用来控制求和的初始值。

>>> max(['2', '111'])               #不指定排序规则
'2'
>>> max(['2', '111'], key=len)      #返回最长的字符串
'111'
>>> print(max([], default=None))    #对空列表求最大值，返回空值None
None
'''
'''
input()和print()是Python的基本输入输出函数，前者用来接收用户的键盘输入，后者用来把数据以指定的格式输出到标准控制台或指定的文件对象。不论用户输入什么内容，input()一律返回字符串对待，必要的时候可以使用内置函数int()、float()或eval()对用户输入的内容进行类型转换
'''
'''
>>> x = input('Please input: ')
Please input: 345
>>> x
'345'
>>> type(x)                     #把用户的输入作为字符串对待
<class 'str'>
>>> int(x)                      #转换为整数
345
>>> eval(x)                     #对字符串求值，或类型转换
345
>>> x = input('Please input: ')
Please input: [1, 2, 3]
>>> x
'[1, 2, 3]'
>>> type(x)
<class 'str'>
>>> eval(x)
[1, 2, 3]
'''
'''
内置函数print()用于输出信息到标准控制台或指定文件，语法格式为：
print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout)

sep参数之前为需要输出的内容（可以有多个）；
sep参数用于指定数据之间的分隔符，默认为空格；
end参数用于指定输出完数据之后再输出什么字符；
file参数用于指定输出位置，默认为标准控制台，也可以重定向输出到文件。

>>> print(1, 3, 5, 7, sep='\t')       #修改默认分隔符
1	3	5	7
>>> for i in range(10):               #修改end参数，每个输出之后不换行
    print(i, end=' ')
0 1 2 3 4 5 6 7 8 9 
>>> with open('test.txt', 'a+') as fp:
    print('Hello world!', file=fp)    #重定向，将内容输出到文件中
'''

'''
sorted()对列表、元组、字典、集合或其他可迭代对象进行排序并返回新列表，
reversed()对可迭代对象（生成器对象和具有惰性求值特性的zip、map、filter、enumerate等类似对象除外）进行翻转（首尾交换）并返回可迭代的reversed对象。
'''
x = list(range(11))
import random
random.shuffle(x)   # 打乱顺序
print(x)        # [5, 1, 0, 10, 4, 2, 8, 3, 6, 9, 7]
print(sorted(x))    # 默认从小到大 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 按转换成字符串以后的长度降序排列
print(sorted(x,key=lambda item:len(str(item))))    # [10, 8, 7, 5, 1, 6, 2, 0, 4, 3, 9]
# 按转换成字符串以后的大小升序排列
print(sorted(x, key=str))

x = ['aaa', 'bc', 'd', 'b', 'ba']
print(sorted(x, key=lambda item: (len(item), item)))    # ['b', 'd', 'ba', 'bc', 'aaa']
print(reversed(x))  # 逆序，返回reversed对象
print(list(reversed(x)))    # ['ba', 'b', 'd', 'bc', 'aaa']

# enumerate()函数用来枚举可迭代对象中的元素，返回可迭代的enumerate对象，其中每个元素都是包含索引和值的元组。
print(list(enumerate('abcd')))  # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
for index, value in enumerate(range(10,15)):
    print((index, value),end = ' ')     # (0, 10) (1, 11) (2, 12) (3, 13) (4, 14)
print()
print(list(map(str,range(5))))  # ['0', '1', '2', '3', '4'] 把列表中元素转换为字符串


def add5(v):
    return v + 5


print(list(map(add5, range(10))))
x = random.randint(1,1e38)
print(x)    # 25372644075703750582007525541310003952
print(list(map(int, str(x))))   # [2, 5, 3, 7, 2, 6, 4, 4, 0, 7, 5, 7, 0, 3, 7, 5, 0, 5, 8, 2, 0, 0, 7, 5, 2, 5, 5, 4, 1, 3, 1, 0, 0, 0, 3, 9, 5, 2]

'''
标准库functools中的函数reduce()可以将一个接收2个参数的函数以迭代累积的方式从左到右依次作用到一个序列或迭代器对象的所有元素上，并且允许指定一个初始值。
        reduce(func, seq)
>>> from functools import reduce
>>> seq = list(range(1, 10))
>>> reduce(lambda x, y: x+y, seq)
45
'''
'''
>>> import operator                         #标准库operator提供了大量运算
>>> operator.add(3,5)                       #可以像普通函数一样直接调用
8
>>> reduce(operator.add, seq)               #使用add运算
45
>>> reduce(operator.mul, seq)               #乘法运算
362880
>>> reduce(operator.mul, range(1, 6))       #5的阶乘
120
>>> reduce(operator.add, map(str, seq))     #转换成字符串再累加
'123456789'
>>> reduce(operator.add, [[1, 2], [3]], []) #这个操作占用空间较大，慎用
[1, 2, 3]
'''
'''
内置函数filter()将一个单参数函数作用到一个序列上，返回该序列中使得该函数返回值为True的那些元素组成的filter对象，如果指定函数为None，则返回序列中等价于True的元素。
    filter(func, seq)
>>> seq = ['foo', 'x41', '?!', '***']
>>> def func(x):
        return x.isalnum()                  #测试是否为字母或数字

>>> filter(func, seq)                   #返回filter对象
<filter object at 0x000000000305D898>
>>> list(filter(func, seq))             #把filter对象转换为列表
['foo', 'x41']
'''
'''
range()是Python开发中非常常用的一个内置函数，语法格式为range([start,] stop [, step] )，有range(stop)、range(start, stop)和range(start, stop, step)三种用法。该函数返回具有惰性求值特点的range对象，其中包含左闭右开区间[start,stop)内以step为步长的整数。参数start默认为0，step默认为1。

>>> range(5)                       #start默认为0，step默认为1
range(0, 5)
>>> list(_)
[0, 1, 2, 3, 4]
>>> list(range(1, 10, 2))          #指定起始值和步长
[1, 3, 5, 7, 9]
>>> list(range(9, 0, -2))          #步长为负数时，start应比stop大
[9, 7, 5, 3, 1]
'''
'''
zip()函数用来把多个可迭代对象中的元素压缩到一起，返回一个可迭代的zip对象，其中每个元素都是包含原来的多个可迭代对象对应位置上元素的元组，如同拉拉链一样。
>>> list(zip('abcd', [1, 2, 3]))             #压缩字符串和列表
[('a', 1), ('b', 2), ('c', 3)]
>>> list(zip('123', 'abc', ',.!'))           #压缩3个序列
[('1', 'a', ','), ('2', 'b', '.'), ('3', 'c', '!')]
>>> x = zip('abcd', '1234')
>>> list(x)
[('a', '1'), ('b', '2'), ('c', '3'), ('d', '4')]
'''
'''
eval(  ) 用来计算字符串（字节串）的值，也可以用来实现类型转换功能。
>>> eval(b‘3+5')             #压缩字符串和列表
8
>>> eval(‘9')           #压缩3个序列
9
>>> eval(input('Please input a num: ')) 
Please input a num: 12+13
25
>>> a,b=eval(input('Please input two numbers:'))
Please input two numbers:12,34
>>> print(a,b)
12 34
'''
print(isinstance(eval('3+5'),int))  # True



























