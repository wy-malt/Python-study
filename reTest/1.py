# coder:也
# 开发时间:2022/10/5 14:29

print(r"xab\t\\\'")
print("xab\t\\\'")

a = 52  # 动态语言
# int b = 62;  这是静态语言

b = 'ABC'
'''
Python解释器干了两件事情：
在内存中创建了一个'ABC'的字符串；
在内存中创建了一个名为a的变量，并把它指向'ABC'。
'''
'''
/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
还有一种除法是//，称为地板除，两个整数的除法仍然是整数
无论整数做//除法还是取余数，结果永远是整数，所以，整数运算结果永远是精确的。
'''

'''
对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，
chr()函数把编码转换为对应的字符
'''
print(ord('A'))
print(ord('中'))
print(chr(65))
print(chr(65156))

'''
Pyhton的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
如果要在网络上传输，或者在磁盘上保存，就需要把str变为以字节为单位的bytes
Python对bytes类型的数据用带b前缀的单引号或双引号表示
'''
x = b'ABC'  # bytes的每个字符都只占用一个字节
print(x)
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
# 要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 要计算str包含多少个字符，可以用len()函数
print(len('ABGUDJDJD'))
print(len(b'ABGUDJDJD'))

'''
当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
#!/user/bin/env python3
# -*- coding : utf-8 -*-

'''
输出格式化的字符串
%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，
有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
占位符	替换内容
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
格式化整数和浮点数还可以指定是否补0和整数与小数的位数
'''
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
# %s永远起作用，它会把任何数据类型转换为字符串
print('Age %s,Gender %s' % (26,True))
# 用%%来表示一个%
print('growth rate: %d %%' % 7)
# 另一种格式化字符串的方法是使用字符串的format()方法，
# 它会用传入的参数依次替换字符串内的占位符{0}、{1}……
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
'''
最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，
它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换
'''
q = 2
w = 3.14 * q **2
print(f'the area of a circle with radius {q} is {w : .2f}')

s1 = 72
s2 = 85
r = (s2-s1) / s1
print('%.1f' % r)









































