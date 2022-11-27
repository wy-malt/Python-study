# coder:也
# 开发时间:2022/10/5 15:41

# 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
# 也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了
age = 3
if age >= 18:       # 注意不要少写了冒号:
    print('your age is', age)
    print('adult')
else:       # 注意不要少写了冒号:
    print('your age is', age)
    print('teenager')
# 可以用elif做更细致的判断
"""
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
"""
'''
if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，
把该判断对应的语句执行后，就忽略掉剩下的elif和else
'''
'''
if判断条件还可以简写，比如写：

if x:
    print('True')
只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
'''
"""
最后看一个有问题的条件判断。很多同学会用input()读取用户的输入，这样可以自己输入，程序运行得更有意思：

birth = input('birth: ')
if birth < 2000:
    print('00前')
else:
    print('00后')
输入1982，结果报错：

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: str() > int()
这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：

s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
"""


# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names = ['wang', 'dcs', 'vedv']
for name in names:
    print(name)

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

"""
如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，
可以生成一个整数序列，再通过list()函数可以转换为list。
比如range(5)生成的序列是从0开始小于5的整数
"""
print(list(range(5)))
# range(101)就可以生成0-100的整数序列
sum1 = 0
for i in list(range(101)):
    sum1 = sum1 + i
print(sum1)


# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
# 计算100以内所有奇数之和
s1 = 0
n = 99
while n > 0:
    s1 = s1 + n
    n = n - 2
print(s1)

# 在循环中，break语句可以提前退出循环。
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)






















































