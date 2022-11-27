# coder:也
# 开发时间:2022/11/25 9:28

"""
关系运算符
Python中的关系运算符可以连续使用，这样不仅可以减少代码量，也比较符合人类的思维方式
"""
print(1<2<3)  # 等价于1<2 and 2<3

# 在条件表达式中使用赋值运算符“=”将抛出异常，提示语法错误
'''
Python还提供了一个三元运算符，并且在三元运算符构成的表达式中还可以嵌套三元运算符，可以实现与选择结构相似的效果。语法为
value1 if condition else value2
'''
'''
两种循环结构的完整语法形式分别为：

while 条件表达式:
    循环体
[else:
    else子句代码块]

和
for 迭代变量 in 序列或迭代对象:
    循环体
[else:
    else子句代码块]

'''
# 9*9乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('{0}*{1}={2}'.format(i,j,i*j),end=' ')
    print()
'''
1*1=1 
2*1=2 2*2=4 
3*1=3 3*2=6 3*3=9 
4*1=4 4*2=8 4*3=12 4*4=16 
5*1=5 5*2=10 5*3=15 5*4=20 5*5=25 
6*1=6 6*2=12 6*3=18 6*4=24 6*5=30 6*6=36 
7*1=7 7*2=14 7*3=21 7*4=28 7*5=35 7*6=42 7*7=49 
8*1=8 8*2=16 8*3=24 8*4=32 8*5=40 8*6=48 8*7=56 8*8=64 
9*1=9 9*2=18 9*3=27 9*4=36 9*5=45 9*6=54 9*7=63 9*8=72 9*9=81 
'''

numbers = []
while True:
    x = input("请输入成绩")
    try:
        numbers.append(float(x))
    except:
        print("输入错误！")
    while True:
        flag = input("继续吗（yes）or(no)")
        if flag.lower() not in ('yes','no'):
            print("只能输入yes或no")
        else:
            break
    if flag.lower() == 'no':
        break
print(numbers)

import time
date = time.localtime()
year, month, day = date[0:3]
day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    day_month[1] = 29
if month == 1:
    print(day)
else:
    print(sum(day_month[:month-1])+day)




















































































