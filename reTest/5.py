# coder:也
# 开发时间:2022/10/5 21:57

# Python内置了很多有用的函数，我们可以直接调用。
"""
要调用一个函数，需要知道函数的名称和参数，
比如求绝对值的函数abs，只有一个参数。
也可以在交互式命令行通过help(abs)查看abs函数的帮助信息
"""
'''
调用函数的时候，如果传入的参数数量不对，会报TypeError的错误
如果传入的参数数量是对的，但参数类型不能被函数所接受，
也会报TypeError的错误，并且给出错误信息
'''
'''
函数名其实就是指向一个函数对象的引用，
完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
'''
a = abs
print(a(-1154))  # 1154

'''
在Python中，定义一个函数要使用def语句，
依次写出函数名、括号、括号中的参数和冒号:，
然后，在缩进块中编写函数体，函数的返回值用return语句返回。
'''


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-66))
'''
请注意，函数体内部的语句在执行时，一旦执行到return时，
函数就执行完毕，并将结果返回。
因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
如果没有return语句，函数执行完毕后也会返回结果，
只是结果为None。return None可以简写为return。
'''
'''
如果你已经把my_abs()的函数定义保存为abstest.py文件了，
那么，可以在该文件的当前目录下启动Python解释器，
用from abstest import my_abs来导入my_abs()函数,
注意abstest是文件名（不含.py扩展名）
'''
'''
如果想定义一个什么事也不做的空函数，可以用pass语句
pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，
比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
'''
def mm():
    pass
# pass还可以用在其他语句里
age = 1
if age >= 18:
    pass    # 缺少了pass，代码运行就会有语法错误。

'''
调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
但是如果参数类型不对，Python解释器就无法帮我们检查。
试试my_abs和内置函数abs的差别：

>>> my_abs('A')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in my_abs
TypeError: unorderable types: str() >= int()
>>> abs('A')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bad operand type for abs(): 'str'
当传入了不恰当的参数时，内置函数abs会检查出参数错误，
而我们定义的my_abs没有参数检查，会导致if语句出错，
出错信息和abs不一样。所以，这个函数定义不够完善。
'''
'''
让我们修改一下my_abs的定义，对参数类型做检查，
只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现
'''
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# 添加了参数检查后，如果传入错误的参数类型，函数就可以抛出一个错误
# my_abs('a')
'''
Traceback (most recent call last):
  File "E:\pythonProject\Test\reTest\5.py", line 92, in <module>
    my_abs('a')
  File "E:\pythonProject\Test\reTest\5.py", line 86, in my_abs
    raise TypeError('bad operand type')
TypeError: bad operand type
'''

# 函数可以返回多个值吗？答案是肯定的。
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
# 然后就可以同时获得返回值
x, y = move(100, 100, 60, math.pi / 6)
# 但其实这只是一种假象，Python函数返回的仍然是单一值
r = move(100, 100, 60, math.pi / 6)
print(r)    # (151.96152422706632, 70.0)    返回值是一个tuple
'''
但是，在语法上，返回一个tuple可以省略括号，
而多个变量可以同时接收一个tuple，按位置赋给对应的值，
所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
'''
'''
小结

定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。
'''


































