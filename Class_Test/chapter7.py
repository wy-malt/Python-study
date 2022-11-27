# coder:也
# 开发时间:2022/11/25 19:20

""""""
'''
在Python中，字符串属于不可变有序序列，使用单引号、双引号、三单引号或三双引号作为定界符，并且不同的定界符之间可以互相嵌套。
'abc'、'123'、'中国'
"Python"

除了支持序列通用方法（包括双向索引、比较大小、计算长度、元素访问、切片、成员测试等操作）以外，字符串类型还支持一些特有的操作方法，例如字符串格式化、查找、替换、排版等等。
字符串属于不可变序列，不能直接对字符串对象进行元素增加、修改与删除等操作，切片操作也只能访问其中的元素而无法使用切片来修改字符串中的字符。

除了支持Unicode编码的str类型之外，Python还支持字节串类型bytes，str类型字符串可以通过encode()方法使用指定的字符串编码格式编码成为bytes对象，而bytes对象则可以通过decode()方法使用指定编码格式解码成为str字符串。

Python 3.x完全支持中文字符，默认使用UTF8编码格式，无论是一个数字、英文字母，还是一个汉字，在统计字符串长度时都按一个字符对待和处理。

>>> s = '中国山东烟台'
>>> len(s)                   #字符串长度，或者包含的字符个数
6
>>> s = '中国山东烟台ABCDE'   #中文与英文字符同样对待，都算一个字符
>>> len(s)
11
>>> 姓名 = '张三'             #使用中文作为变量名
>>> print(姓名)               #输出变量的值
张三

为了避免对字符串中的转义字符进行转义，可以使用原始字符串，在字符串前面加上字母r或R表示原始字符串，其中的所有字符都表示原始的含义而不会进行任何转义。

>>> path = 'C:\Windows\notepad.exe'
>>> print(path)                       #字符\n被转义为换行符
C:\Windows
otepad.exe
>>> path = r'C:\Windows\notepad.exe'  #原始字符串，任何字符都不转义
>>> print(path)
C:\Windows\notepad.exe

语法格式：  ‘%  [-] [+]  [0] [m] [.n]  格式字符type’ %  exp
-：可选参数，用于指定左对齐，正数前方无符号，负数前面加负号。
+：可选参数，用于指定右对齐，正数前方加正号，负数前面加负号。
0：可选参数，表示右对齐，正数前方无符号，负数前方加负号，用0填充空白处。
m：可选参数，表示占有宽度。
n：可选参数，表示小数点后保留的位数。
格式字符：用于指定类型（见下页）。
exp：要转换的项。如有多项，需要用元组表示，不能使用列表。

格式字符	说明
%s	字符串 (采用str()的显示)
%r	字符串 (采用repr()的显示)
%c	单个字符
%d	十进制整数
%i	十进制整数
%o	八进制整数
%x	十六进制整数
%e	指数 (基底写为e)
%E	指数 (基底写为E)
%f、%F	浮点数
%g	指数(e)或浮点数 (根据显示长度)
%G	指数(E)或浮点数 (根据显示长度)
%%	一个字符"%"
'''
'''
字符串对象提供了format方法用于进行字符串格式化
语法格式：  str.format(args)
str：用于指定字符串的显示样式（即模板template）。
args：用于指定要转换的项，如果有多项，用逗号进行分割。
模板str需要用“{}”和“:”指定占位符
语法格式：  { [index] [: [ [fill]align] [sign] [#] [width] [.precision] [type] ] }
index：可选参数，用于指定要设置格式的对象在参数列表中的索引位置，从0开始。
fill：可选参数，用于指定空白处填充的字符。
align：可选参数，用于指定对齐方式（“<”左对齐；“>”右对齐；“=”右对齐，只对数值有效，“^”居中），需配合width使用。
sign：可选参数，指定有无符号数（“+”正数加正号，负数加负号；“-”正数不变，负数加负号；“ ”正数加空格，负数加负号）

'Today is {0:*>6d} year {1:$>4d}month {2:@>4d} day'.format(2022,5,29)
'Today is **2022 year $$$5month @@29 day'

#：可选参数，对于二进制、八进制、十六进制数，如果加上“#”，表示会显示0b/0o/0x前缀，否则不像是前缀。
width：可选参数，用于指定所占宽度。
.precision：可选参数，用于指定保留的小数位数。
type：可选参数，格式字符，用于指定类型。

>>> 1/3
0.3333333333333333
>>> print('{0:.3f}'.format(1/3))         #保留3位小数
0.333
>>> '{0:%}'.format(3.5)                  #格式化为百分数
'350.000000%'
>>> '{0:_},{0:_x}'.format(1000000)       #Python 3.6.0及更高版本支持
'1_000_000,f_4240'
>>> '{0:_},{0:_x}'.format(10000000)      #Python 3.6.0及更高版本支持
'10_000_000,98_9680'

>>> print("The number {0:} in hex is: {0:#x}, the number {1} in oct is {1:#o}".format(5555,55))
The number 5555 in hex is: 0x15b3, the number 55 in oct is 0o67
>>> print("The number {1:} in hex is: {1:#x}, the number {0} in oct is {0:o}".format(5555,55))
The number 55 in hex is: 0x37, the number 5555 in oct is 12663
>>> print(“my name is {name}, my age is {age}, and my QQ is {qq}”.format(name = “Dong Fuguo”,age = 40,qq = “30646****”))  #（关键字参数格式化）
my name is Dong Fuguo, my age is 40, and my QQ is 30646****
>>> position = (5, 8, 13)
>>> print("X:{0[0]};Y:{0[1]};Z:{0[2]}".format(position))
X:5;Y:8;Z:13

从Python 3.6.x开始支持一种新的字符串格式化方式，官方叫做Formatted String Literals，在字符串前加字母f，含义与字符串对象format()方法类似。
>>> name = 'Dong'
>>> age = 39
>>> f'My name is {name}, and I am {age} years old.'
'My name is Dong, and I am 39 years old.'
>>> width = 10
>>> precision = 4
>>> value = 11/3
>>> f'result:{value:{width}.{precision}}'      # 保留最多4位有效数字
'result:     3.667'
>>> f'result:{value:{width}.{precision}f}'     # 恰好保留4位小数
'result:    3.6667'

Python字符串对象提供了大量方法用于字符串的切分、连接、替换和排版等操作，另外还有大量内置函数和运算符也支持对字符串的操作。
字符串对象是不可变的，所以字符串对象提供的涉及到字符串“修改”的方法都是返回修改后的新字符串，并不对原始字符串做任何修改，无一例外

检索字符串： find()、rfind()、index()、rindex()、count()
find()、rfind()、index()、rindex()、count()
语法：str.find(sub [, start [, end]])
find()和rfind方法分别用来查找一个字符串在另一个字符串指定范围（默认是整个字符串）中首次和最后一次出现的位置，如果不存在则返回-1；
index()和rindex()方法用来返回一个字符串在另一个字符串指定范围中首次和最后一次出现的位置，如果不存在则抛出异常；
count()方法用来返回一个字符串在当前字符串中出现的次数。
>>> s="apple,peach,banana,peach,pear"
>>> s.find("peach")
6
>>> s.find("peach",7)
19
>>> s.find("peach",7,20)
-1
>>> s.rfind('p')
25
>>> s.index('p')
1
>>> s.index('pe')
6
>>> s.index('pear')
25
>>> s.index('ppp')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.index('ppp')
ValueError: substring not found
>>> s.count('p')
5
>>> s.count('pp')
1
>>> s.count('ppp')
0

分割：split()、rsplit()、partition()、rpartition()
split()、rsplit()、partition()、rpartition()
语法：str.split( sep [, maxsplit])
split()和rsplit()方法分别用来以指定字符为分隔符，把当前字符串从左往右或从右往左分隔成多个字符串，并返回包含分隔结果的列表；
partition()和rpartition()用来以指定字符串为分隔符将原字符串分隔为3部分，即分隔符前的字符串、分隔符字符串、分隔符后的字符串，如果指定的分隔符不在原字符串中，则返回原字符串和两个空字符串。
>>> s = "apple,peach,banana,pear"
>>> s.split(",")
["apple", "peach", "banana", "pear"]
>>> s.partition(',')
('apple', ',', 'peach,banana,pear')
>>> s.rpartition(',')
('apple,peach,banana', ',', 'pear')
>>> s.rpartition('banana')
('apple,peach,', 'banana', ',pear')
>>> s = "2017-10-31"
>>> t = s.split("-")
>>> print(t)
['2017', '10', '31']
>>> print(list(map(int, t)))
[2017, 10, 31]

split()和rsplit()方法还允许指定最大分割次数。

>>> s = '\n\nhello\t\t world \n\n\n My name is Dong   '
>>> s.split(None, 1)
['hello', 'world \n\n\n My name is Dong   ']
>>> s.rsplit(None, 2)
['\n\nhello\t\t world \n\n\n My name', 'is', 'Dong']
>>> s.split(maxsplit=6)
['hello', 'world', 'My', 'name', 'is', 'Dong']
>>> s.split(maxsplit=100)     #最大分隔次数大于可分隔次数时无效
['hello', 'world', 'My', 'name', 'is', 'Dong']

然而，明确传递参数指定split()使用的分隔符时，情况是不一样的。

>>> 'a,,,bb,,ccc'.split(',')       #每个逗号都被作为独立的分隔符
['a', '', '', 'bb', '', 'ccc']
>>> 'a\t\t\tbb\t\tccc'.split('\t') #每个制表符都被作为独立的分隔符
['a', '', '', 'bb', '', 'ccc']
>>> 'a\t\t\tbb\t\tccc'.split()     #连续多个制表符被作为一个分隔符
['a', 'bb', 'ccc']

字符串连接join()
语法：strnew = string.join(iterable)

>>> li = ["apple", "peach", "banana", "pear"]
>>> ','.join(li)
'apple,peach,banana,pear'
>>> '.'.join(li)
'apple.peach.banana.pear'
>>> '::'.join(li)
'apple::peach::banana::pear'

使用split()和join()方法删除字符串中多余的空白字符，连续多个空白字符只保留一个。
>>> x = 'aaa      bb      c d e   fff    '
>>> ' '.join(x.split())             #使用空格作为连接符
'aaa bb c d e fff'
>>> def equavilent(s1, s2):         #判断两个字符串在Python意义上是否等价
	if s1 == s2:
		return True
	elif ' '.join(s1.split()) == ' '.join(s2.split()):
		return True
	elif ''.join(s1.split()) == ''.join(s2.split()):
		return True
	else:
		return False	
>>> equavilent('pip list', 'pip    list')
True

大小写转换：lower()、upper()、capitalize()、title()、swapcase()
>>> s = "What is Your Name?"
>>> s.lower()                   #返回小写字符串
'what is your name?'
>>> s.upper()                   #返回大写字符串
'WHAT IS YOUR NAME?'
>>> s.capitalize()              #字符串首字符大写
'What is your name?'
>>> s.title()                   #每个单词的首字母大写
'What Is Your Name?'
>>> s.swapcase()                #大小写互换
'wHAT IS yOUR nAME?

替换：replace()、maketrans()、translate()
查找替换replace()，类似于Word中的“全部替换”功能。

>>> s = "中国，中国"
>>> print(s)
中国，中国
>>> s2 = s.replace("中国", "中华人民共和国")  #两个参数都作为一个整理
>>> print(s2)
中华人民共和国，中华人民共和国

问题解决：测试用户输入中是否有敏感词，如果有的话就把敏感词替换为3个星号***。
>>> words = ('测试', '非法', '暴力', '话')
>>> text = '这句话里含有非法内容'
>>> for word in words:
    if word in text:
        text = text.replace(word, '***')		
>>> text
'这句***里含有***内容'

字符串对象的maketrans()方法用来生成字符映射表，而translate()方法用来根据映射表中定义的对应关系转换字符串并替换其中的字符，使用这两个方法的组合可以同时处理多个字符。


#创建映射表，将字符"abcdef123"一一对应地转换为"uvwxyz@#$"
>>> table = str.maketrans('abcdef123', 'uvwxyz@#$')
>>> s = "Python is a greate programming language. I like it!"
#按映射表进行替换
>>> s.translate(table)
'Python is u gryuty progrumming lunguugy. I liky it!'

问题解决：凯撒加密，每个字母替换为后面第k个。
>>> import string
>>> def kaisa(s, k):
    lower = string.ascii_lowercase          #小写字母
    upper = string.ascii_uppercase          #大写字母
    before = string.ascii_letters
    after = lower[k:] + lower[:k] + upper[k:] + upper[:k]
    table = str.maketrans(before, after)     #创建映射表
    return s.translate(table)

>>> s = "Python is a greate programming language. I like it!"
>>> kaisa(s, 3)
'Sbwkrq lv d juhdwh surjudpplqj odqjxdjh. L olnh lw!'

去除：strip()、rstrip()、lstrip()
strip()、rstrip()、lstrip()

语法：string.strip([chars])

>>> s = " abc  "
>>> s.strip()                             #删除空白字符
'abc'
>>> '\n\nhello world   \n\n'.strip()      #删除空白字符
'hello world'
>>> "aaaassddf".strip("a")                #删除指定字符
'ssddf'
>>> "aaaassddf".strip("af")
'ssdd'
>>> "aaaassddfaaa".rstrip("a")            #删除字符串右端指定字符
'aaaassddf'
>>> "aaaassddfaaa".lstrip("a")            #删除字符串左端指定字符
'ssddfaaa'

这三个函数的参数指定的字符串并不作为一个整体对待，而是在原字符串的两侧、右侧、左侧删除参数字符串中包含的所有字符，一层一层地从外往里扒。

>>> 'aabbccddeeeffg'.strip('af')  #字母f不在字符串两侧，所以不删除
'bbccddeeeffg'
>>> 'aabbccddeeeffg'.strip('gaf')
'bbccddeee'
>>> 'aabbccddeeeffg'.strip('gaef')
'bbccdd'
>>> 'aabbccddeeeffg'.strip('gbaef')
'ccdd'
>>> 'aabbccddeeeffg'.strip('gbaefcd')
''

起始判断：startswith()、endswith()
s.startswith(t)、s.endswith(t)，判断字符串是否以指定字符串开始或结束

>>> s = 'Beautiful is better than ugly.'
>>> s.startswith('Be')             #检测整个字符串
True
>>> s.startswith('Be', 5)         #指定检测范围起始位置
False
>>> s.startswith('Be', 0, 5)     #指定检测范围起始和结束位置
True
>>> import os
>>> [filename for filename in os.listdir(r'c:\\') if filename.endswith(('.bmp','.jpg','.gif'))]

isalnum()、isalpha()、isdigit()、isdecimal()、isnumeric()、isspace()、isupper()、islower()，用来测试字符串是否为数字或字母、是否为字母、是否为数字字符、是否为空白字符、是否为大写字母以及是否为小写字母。

>>> '1234abcd'.isalnum()
True
>>> '1234abcd'.isalpha()         #全部为英文字母时返回True
False
>>> '1234abcd'.isdigit()         #全部为数字时返回True
False
>>> 'abcd'.isalpha()
True
>>> '1234.0'.isdigit()
False
>>> '1234'.isdigit()
True
>>> '九'.isnumeric()              #isnumeric()方法支持汉字数字
True
>>> '九'.isdigit()
False
>>> '九'.isdecimal()
False
>>> 'ⅣⅢⅩ'.isdecimal()
False
>>> 'ⅣⅢⅩ'.isdigit()
False
>>> 'ⅣⅢⅩ'.isnumeric()          #支持罗马数字
True

center()、ljust()、rjust()，返回指定宽度的新字符串，原字符串居中、左对齐或右对齐出现在新字符串中，如果指定宽度大于字符串长度，则使用指定的字符（默认为空格）进行填充。zfill()返回指定宽度的字符串，在左侧以字符0进行填充。

>>> 'Hello world!'.center(20)        #居中对齐，以空格进行填充
'    Hello world!    '
>>> 'Hello world!'.center(20, '=')   #居中对齐，以字符=进行填充
'====Hello world!===='
>>> 'Hello world!'.ljust(20, '=')    #左对齐
'Hello world!========'
>>> 'Hello world!'.rjust(20, '=')    #右对齐
'========Hello world!'


'''
'''
Python字符串支持与整数的乘法运算，表示序列重复，也就是字符串内容的重复，得到新字符串。

>>> 'abcd' * 3
'abcdabcdabcd'

>>> x = 'Hello world.'
>>> len(x)                       #字符串长度
12
>>> max(x)                       #最大字符
'w'
>>> min(x)
' '
>>> list(zip(x,x))               #zip()也可以作用于字符串
[('H', 'H'), ('e', 'e'), ('l', 'l'), ('l', 'l'), ('o', 'o'), (' ', ' '), ('w', 'w'), ('o', 'o'), ('r', 'r'), ('l', 'l'), ('d', 'd'), ('.', '.')]
>>> sorted(x)
[' ', '.', 'H', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
>>> list(reversed(x))
['.', 'd', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'H']
>>> list(enumerate(x))
[(0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'), (5, ' '), (6, 'w'), (7, 'o'), (8, 'r'), (9, 'l'), (10, 'd'), (11, '.')]
>>> list(map(lambda i,j: i+j, x, x))
['HH', 'ee', 'll', 'll', 'oo', '  ', 'ww', 'oo', 'rr', 'll', 'dd', '..']

内置函数eval()用来把任意字符串转化为Python表达式并进行求值。

>>> eval("3+4")                         #计算表达式的值
7
>>> a = 3
>>> b = 5
>>> eval('a+b')                         #这时候要求变量a和b已存在
8
>>> import math
>>> eval('math.sqrt(3)')
1.7320508075688772

切片也适用于字符串，但仅限于读取其中的元素，不支持字符串修改。

>>> 'Explicit is better than implicit.'[:8]
'Explicit'
>>> 'Explicit is better than implicit.'[9:23]
'is better than'
>>> path = 'C:\\Python35\\test.bmp'
>>> path[:-4] + '_new' + path[-4:]
'C:\\Python35\\test_new.bmp'

Python标准库string中定义数字字符、标点符号、英文字母、大写字母、小写字母等常量。

>>> import string
>>> string.digits
'0123456789'
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

问题解决：生成指定长度的随机密码。
>>> import string
>>> characters = string.digits + string.ascii_letters
>>> import random
>>> ''.join([random.choice(characters) for i in range(8)])
'J5Cuofhy'
>>> ''.join([random.choice(characters) for i in range(10)])
'RkHA3K3tNl'
>>> ''.join([random.choice(characters) for i in range(16)])
'zSabpGltJ0X4CCjh'

中英文分词
>>> import jieba                    #导入jieba模块
>>> x = '分词的准确度直接影响了后续文本处理和挖掘算法的最终效果。'
>>> jieba.cut(x)                    #使用默认词库进行分词
<generator object Tokenizer.cut at 0x000000000342C990>
>>> list(_)
['分词', '的', '准确度', '直接', '影响', '了', '后续', '文本处理', '和', '挖掘', '算法', '的', '最终', '效果', '。']
>>> list(jieba.cut('纸杯'))
['纸杯']
>>> list(jieba.cut('花纸杯'))
['花', '纸杯']
>>> jieba.add_word('花纸杯')         #增加词条
>>> list(jieba.cut('花纸杯'))        #使用新词库进行分词
['花纸杯']
>>> import snownlp                  #导入snownlp模块
>>> snownlp.SnowNLP('学而时习之，不亦说乎').words
['学而', '时习', '之', '，', '不亦', '说乎']
>>> snownlp.SnowNLP(x).words
['分词', '的', '准确度', '直接', '影响', '了', '后续', '文本', '处理', '和', '挖掘', '算法', '的', '最终', '效果', '。']

汉字到拼音的转换
>>> from pypinyin import lazy_pinyin, pinyin
>>> lazy_pinyin('董付国')            #返回拼音
['dong', 'fu', 'guo']
>>> lazy_pinyin('董付国', 1)         #带声调的拼音
['dǒng', 'fù', 'guó']
>>> lazy_pinyin('董付国', 2)         #另一种拼音形式，数字表示前面字母的声调
['do3ng', 'fu4', 'guo2']
>>> lazy_pinyin('董付国', 3)         #只返回拼音首字母
['d', 'f', 'g']
>>> lazy_pinyin('重要', 1)           #能够根据词组智能识别多音字
['zhòng', 'yào']
>>> lazy_pinyin('重阳', 1)
['chóng', 'yáng']
>>> pinyin('重阳')                   #返回拼音
[['chóng'], ['yáng']]
>>> pinyin('重阳节', heteronym=True) #返回多音字的所有读音
[['chóng'], ['yáng'], ['jié', 'jiē']]
>>> import jieba                     #其实不需要导入jieba，这里只是说明已安装
>>> x = '中英文混合test123'
>>> lazy_pinyin(x)                   #自动调用已安装的jieba扩展库分词功能
['zhong', 'ying', 'wen', 'hun', 'he', 'test123']
>>> lazy_pinyin(jieba.cut(x))
['zhong', 'ying', 'wen', 'hun', 'he', 'test123']
>>> x = '山东烟台的大樱桃真好吃啊'
>>> sorted(x, key=lambda ch: lazy_pinyin(ch))
                                     #按拼音对汉字进行排序
['啊', '吃', '大', '的', '东', '好', '山', '台', '桃', '烟', '樱', '真']

'''





































































































