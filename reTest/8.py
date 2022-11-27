# coder:也
# 开发时间:2022/10/8 7:20

# 函数式编程
"""
函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。

而函数式编程（请注意多了一个“式”字）——Functional Programming，虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算。

我们首先要搞明白计算机（Computer）和计算（Compute）的概念。

在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令，所以，汇编语言是最贴近计算机的语言。

而计算则指数学意义上的计算，越是抽象的计算，离计算机硬件越远。

对应到编程语言，就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，比如C语言；越高级的语言，越贴近计算，抽象程度高，执行效率低，比如Lisp语言。

函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
"""

# 高阶函数

# 变量可以指向函数
# 以Python内置的求绝对值的函数abs()为例，调用该函数用以下代码：
print(abs(-10))  # 10
# 但是，如果只写abs呢？
print(abs)  # <built-in function abs>
# 可见，abs(-10)是函数调用，而abs是函数本身。
# 要获得函数调用结果，我们可以把结果赋值给变量：
x = abs(-10)
print(x)
# 但是，如果把函数本身赋值给变量呢？
f = abs
print(f)    # <built-in function abs>
# 结论：函数本身也可以赋值给变量，即：变量可以指向函数。
# 如果一个变量指向了一个函数，那么，可否通过该变量来调用这个函数？用代码验证一下：
print(f(-12))   # 12
# 成功！说明变量f现在已经指向了abs函数本身。直接调用abs()函数和调用变量f()完全相同。

# 函数名也是变量
# 那么函数名是什么呢？函数名其实就是指向函数的变量！对于abs()这个函数，
# 完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！
# 如果把abs指向其他对象，会有什么情况发生？
# abs = 10
# print(abs(-10))
'''
print(abs(-10))
TypeError: 'int' object is not callable
'''
# 把abs指向10后，就无法通过abs(-10)调用该函数了！
# 因为abs这个变量已经不指向求绝对值函数而是指向一个整数10！
'''
注：由于abs函数实际上是定义在import builtins模块中的，
所以要让修改abs变量的指向在其它模块也生效，要用
import builtins;builtins.abs=10
'''

# 传入函数
# 既然变量可以指向函数，函数的参数能接收变量，
# 那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
# 一个最简单的高阶函数：
def add(x, y, f):
    return f(x) + f(y)
# 当我们调用add(-5, 6, abs)时，参数x，y和f分别接收-5，6和abs，根据函数定义，我们可以推导计算过程为：
'''
x = -5
y = 6
f = abs
f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
return 11
'''
print(add(5,-10,abs))   # 15

#  map/reduce
# 我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f11(x):
    return x*x
r = map(f11,[1,2,3,4,5,6,7,8,9])
print(list(r))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
'''
map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，
Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
'''
'''
你可能会想，不需要map()函数，写一个循环，也可以计算出结果：

L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)
的确可以，但是，从上面的循环代码，
能一眼看明白“把f(x)作用在list的每一个元素并把结果生成一个新的list”吗？
'''
r = '1cshuchu'
print(str(r))
print(list(map(str,[1,2,3,4,5,6,7,8,9])))
'''
再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f,[x1,x2,x3,x4,x5]) = f(f(f(f(x1,x2),x3),x4),x5)
'''
# 比方说对一个序列求和，就可以用reduce实现：
from functools import reduce
def add1(x, y):
    return x+y
print(reduce(add1,[1,3,5,7,9]))     # 25

def fn(x, y):
    return x * 10 + y
print(reduce(fn,[1,3,5,7,9]))   # 13579
'''
这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，
对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
'''
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(reduce(fn,map(char2num,'13579')))     # 13579

# 整理成一个str2int的函数就是：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num1(s):
        return DIGITS[s]
    return reduce(fn, map(char2num1,s))
# 还可以用lambda函数进一步简化成：
def char2num2(s):
    return DIGITS[s]
def str2int1(s):
    return reduce(lambda x, y:x * 10 + y,map(char2num2,s))
print(str2int1('102455'))   # 102455

# 练习
'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
'''
def normalize(name):
    return name.upper()[0:1] + name.lower()[1:]
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize,L1))
print(L2)   # ['Adam', 'Lisa', 'Bart']
'''
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
'''
def prod(a):
    def m(x,y):
        return x*y
    return reduce(m,a)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
'''
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
'''
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}
def str2float(s):
    nums = map(lambda ch : CHAR_TO_FLOAT[ch],s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f*10+n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float,nums,0.0)
print(str2float('1234.56789'))      # 1234.56789

# filter
'''
Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。

例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
'''
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd,[1,5,7,4,6,8,9,3,4,5,7])))     # [1, 5, 7, 9, 3, 5, 7]
# 把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()  # str.strip([chars])    chars -- 移除字符串头尾指定的字符序列。
print(list(filter(not_empty,['A','xcwsc',None,'B','c',' '])))   # ['A', 'xcwsc', 'B', 'c']
# 可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，
# 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
'''
用filter求素数
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：

首先，列出从2开始的所有自然数，构造一个序列：

2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：

3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：

5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数5，然后用5把序列的5的倍数筛掉：

7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

不断筛下去，就可以得到所有的素数。

用Python来实现这个算法，可以先构造一个从3开始的奇数序列：
'''
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x : x%n > 0
def primes():
    yield 2
    it = _odd_iter()    # 初始序列
    while True:
        n = next(it)    # 返回序列第一个数
        yield n
        it = filter(_not_divisible(n),it)   # 构造新序列
# 这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。
# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
# 打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
# 注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。

# sorted
'''
排序算法
排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，
排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，
但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，
因此，比较的过程必须通过函数抽象出来。

Python内置的sorted()函数就可以对list进行排序：
'''
print(sorted([1,2,32,6,7,4,1,2]))   # [1, 1, 2, 2, 4, 6, 7, 32]
# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([36,-5,-95,54,2,175],key=abs))     # [2, -5, 36, 54, -95, 175]
# 再看一个字符串排序的例子：
print(sorted(['bob', 'about', 'Zoo', 'Credit']))    # ['Credit', 'Zoo', 'about', 'bob']
'''
默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，
结果，大写字母Z会排在小写字母a的前面。

现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，
不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。
忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。

这样，我们给sorted传入key函数，即可实现忽略大小写的排序：
'''
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key = str.lower))    # ['about', 'bob', 'Credit', 'Zoo']
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key = str.lower,reverse = True))     # ['Zoo', 'Credit', 'bob', 'about']
# 从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。

# 返回函数
'''
函数作为返回值
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
'''
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
# 可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum1():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum1
# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
print(lazy_sum(1,2,3,4,5))  # <function lazy_sum.<locals>.sum1 at 0x00000209A6E7B2E0>
f = lazy_sum(1,2,3,4,5)
print(f())  # 15
'''
在这个例子中，我们在函数lazy_sum中又定义了函数sum，
并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
这种称为“闭包（Closure）”的程序结构拥有极大的威力。

请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，
即使传入相同的参数：
'''
f1 = lazy_sum(1,2,3)
f2 = lazy_sum(1,2,3)
print(f1==f2)   # False
# f1()和f2()的调用结果互不影响。
'''
闭包
注意到返回的函数在其定义内部引用了局部变量args，
所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
所以，闭包用起来简单，实现起来可不容易。

另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：
'''
def count():
    fs = []
    for i in range(1,4):
        def f4():
            return i * i
        fs.append(f4)
    return fs
f5,f6,f7=  count()
# 在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
#
# 你可能认为调用f5()，f6()和f7()结果应该是1，4，9，但实际结果是：
print(f5(),f6(),f7())   # 9 9 9
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count1():
    def f10(j):
        def g():
            return j*j
        return g
    fs1 = []
    for i in range(1,4):
        fs1.append(f10(i))    # # f(i)立刻被执行，因此i的当前值被传入f()
    return fs1
f11,f12,f13 = count1()
print(f11(),f12(),f13())    # 1 4 9
# 缺点是代码较长，可利用lambda函数缩短代码。
'''
nonlocal
使用闭包，就是内层函数引用了外层函数的局部变量。
如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常
'''
def inc():
    x = 0
    def fn1():
        # 仅读取x的值:
        return x+1
    return fn1
f = inc()
print(f())  # 1
print(f())  # 1
# 但是，如果对外层变量赋值，由于Python解释器会把x当作函数fn()的局部变量，它会报错：
def inc1():
    x = 0
    def fn2():
        nonlocal x  # 不加报错
        # 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。
        x = x+1
        return x
    return fn2
f = inc1()
print(f())  # 1
print(f())  # 2
'''
Traceback (most recent call last):
  File "E:\pythonProject\Test\reTest\8.py", line 386, in <module>
    print(f())
  File "E:\pythonProject\Test\reTest\8.py", line 382, in fn2
    x = x+1
UnboundLocalError: local variable 'x' referenced before assignment
'''
'''
原因是x作为局部变量并没有初始化，直接计算x+1是不行的。
但我们其实是想引用inc()函数内部的x，
所以需要在fn()函数内部加一个nonlocal x的声明。
加上这个声明后，解释器把fn()的x看作外层函数的局部变量，
它已经被初始化了，可以正确计算x+1。
'''
# 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。
'''
小结
一个函数可以返回一个计算结果，也可以返回一个函数。

返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
'''

# 匿名函数
'''
当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

在Python中，对匿名函数提供了有限支持。还是以map()函数为例，
计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
'''
print(list(map(lambda x : x * x,[1,2,3,4,5,6,7,8,9])))      # [1, 4, 9, 16, 25, 36, 49, 64, 81]
# 通过对比可以看出，匿名函数lambda x: x * x实际上就是：
# def f(x):
#     return x*x
'''
关键字lambda表示匿名函数，冒号前面的x表示函数参数。

匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
此外，匿名函数也是一个函数对象，
也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
'''
f22 = lambda x: x*x
print(f22)  # <function <lambda> at 0x00000134269DB760>
print(f22(5))   # 25
# 同样，也可以把匿名函数作为返回值返回，比如：
def buile(x, y):
    return lambda : x*x+y*y

# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print('2022-10-8')
f = now
f()     # 2022-10-8
# 函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__)     # now
print(f.__name__)   # now
'''
现在，假设我们要增强now()函数的功能，
比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

本质上，decorator就是一个返回函数的高阶函数。
所以，我们要定义一个能打印日志的decorator，可以定义如下：
'''
print('*************************')
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper
# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，
# 并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now1():
    print('2022-10-8')
now1()
'''
调用now1()函数，不仅会运行now1()函数本身，还会在运行now1()函数前打印一行日志：
call now1():
2022-10-8
'''
'''
把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)
'''
'''
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，
即在log()函数中返回的wrapper()函数。

wrapper()函数的参数定义是(*args, **kw)，
因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，
首先打印日志，再紧接着调用原始函数。

如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
写出来会更复杂。比如，要自定义log的文本：
'''
print('*****************************')
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
# 这个3层嵌套的decorator用法如下：
@log('execute')
def now2():
    print('2022-10-8')
now2()
'''
execute now2():
2022-10-8
'''
# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：
# now = log('execute')(now2)
'''
我们来剖析上面的语句，首先执行log('execute')，
返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

以上两种decorator的定义都没有问题，但还差最后一步。
因为我们讲了函数也是对象，它有__name__等属性，
但你去看经过decorator装饰之后的函数，
它们的__name__已经从原来的'now'变成了'wrapper'：
'''
print(now2.__name__)    # wrapper
'''
因为返回的那个wrapper()函数名字就是'wrapper'，
所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，
Python内置的functools.wraps就是干这个事的，
所以，一个完整的decorator的写法如下：
'''
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper
# 或者针对带参数的decorator：
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

# 偏函数
'''
Python的functools模块提供了很多有用的功能，
其中一个就是偏函数（Partial function）。
要注意，这里的偏函数和数学意义上的偏函数不一样。

在介绍函数参数的时候，我们讲到，通过设定参数的默认值，
可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：

int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
'''
print(int('45656')) # 45656
# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：

# print(int('12345',base=2))
'''
Traceback (most recent call last):
  File "E:\pythonProject\Test\reTest\8.py", line 558, in <module>
    print(int('12345',base=2))
ValueError: invalid literal for int() with base 2: '12345'
'''
print(int('12345',base=6))  # 1865
print(int('1010110001',base=2))     # 689
# print(int(12345,base=2))
'''
Traceback (most recent call last):
  File "E:\pythonProject\Test\reTest\8.py", line 567, in <module>
    print(int(12345,base=2))
TypeError: int() can't convert non-string with explicit base
'''
# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
def int2(x, base=2):
    return int(x, base)
print(int2('10000000'))     # 128
'''
functools.partial就是帮助我们创建一个偏函数的，
不需要我们自己定义int3()，可以直接使用下面的代码创建一个新的函数int3：
'''
import functools
int3 = functools.partial(int, base=2)
print(int3('1111011'))      # 123
'''
所以，简单总结functools.partial的作用就是，
把一个函数的某些参数给固定住（也就是设置默认值），
返回一个新的函数，调用这个新函数会更简单。

注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，
但也可以在函数调用时传入其他值
'''
print(int3('515151',base=10))       # 515151
'''
最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：

int2 = functools.partial(int, base=2)
实际上固定了int()函数的关键字参数base，也就是：

int2('10010')
相当于：

kw = { 'base': 2 }
int('10010', **kw)
'''
# 当传入：
max2 = functools.partial(max,10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：
'''
相当于：
args = (10, 5, 6, 7)
max(*args)
'''
print(max2(5,6,7))  # 10
'''
小结
当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
'''



















