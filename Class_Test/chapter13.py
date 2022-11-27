# coder:也
# 开发时间:2022/11/26 22:35

"""
数据分析、科学计算、数据可视化
"""
import numpy as np

print(np.array([1,2,3,4,5]))
print(np.arange(8))     # [0 1 2 3 4 5 6 7]
print(np.zeros(3))
print(np.ones(3))

print(np.zeros((3,3)))
'''
[[0. 0. 0.]         全0二维数组，3行3列
 [0. 0. 0.]
 [0. 0. 0.]]
'''

print(np.identity(3))
'''
[[1. 0. 0.]         单位矩阵
 [0. 1. 0.]
 [0. 0. 1.]]
'''

print(np.random.randint(0,50,5))    # 随机数组，5个0到50之间的整数
# [14 45 28 46 22]
print(np.random.randint(0,50,(3,5)))    # 3行5列，15个介于0和50之间的整数
'''
[[36 19 10 29  1]
 [ 7 35  5 32 12]
 [41 19  0  1 24]]
'''

print(np.random.rand(10))       # 10个小数
# [0.09149078 0.42892904 0.96729294 0.48794706 0.70873967 0.92083597
#  0.75906818 0.6610452  0.07166106 0.04584557]

print(np.random.standard_normal(5))     # 从标准正态分布中随机采样
# [-1.26886524 -0.7073441  -0.02172475 -0.27346914  1.34429339]

x = np.random.standard_normal(size=(3,4,2))
print(x)
'''
[[[ 0.20425401  0.98707713]
  [ 0.00486726 -0.64673101]
  [-1.70485666  1.07417814]
  [-0.58050916 -1.44550418]]

 [[ 0.08499361 -0.77339675]
  [-1.17046092  0.57136563]
  [-0.15923869 -0.2082803 ]
  [-1.60458358 -0.71159868]]

 [[-1.02220276 -1.00185733]
  [-0.362034    0.40802418]
  [ 0.16860093  0.27460562]
  [-1.62205326 -0.3964414 ]]]
'''

a = np.diag([1,2,3])
print(a)    # 对角矩阵
'''
[[1 0 0]
 [0 2 0]
 [0 0 3]]
'''

# 测试两个数组是否足够接近
x = np.array([1, 2, 3, 4.001, 5])
y = np.array([1,1.999,3,4.01,5.1])
print(np.allclose(x,y))     # False
print(np.allclose(x,y,rtol=0.2))    # True  # 设置相对误差参数
print(np.allclose(x,y,atol=0.2))    # True  # 设置绝对误差参数

a = np.array((1,2,3))
b = np.array(([1,2,3],[4,5,6],[7,8,9]))
c = a * b   # a中的每个元素乘以b中的对应列元素
print(c)
'''
[[ 1  4  9]
 [ 4 10 18]
 [ 7 16 27]]
'''
print(c/b)
'''
[[1. 2. 3.]
 [1. 2. 3.]
 [1. 2. 3.]]
'''
print(c/a)
'''
[[1. 2. 3.]
 [4. 5. 6.]
 [7. 8. 9.]]
'''
print(a + a)    # 数组之间的加法运算
# [2 4 6]
print(a * a)    # 数组之间的乘法运算
# [1 4 9]
print(a / a)    # 数组之间的除法运算
# [1. 1. 1.]

d = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(d)
print(d.T)      # 转置
'''
[[1 4 7]
 [2 5 8]
 [3 6 9]]
'''

# 一维数组排序
排序 = np.array([3,1,2])
print(np.argsort(排序))   # [1 2 0]  返回排序后元素的原下标
print(排序[np.argsort(排序)])   # [1 2 3]
x = np.array([5,7,4,9,4,56])
x.sort()
print(x)    # [ 4  4  5  7  9 56]   原地排序

x = np.array([[0,3,4],[2,1,2]])
print(np.argsort(x,axis=0))     # 二维数组纵向排序，返回原下标
'''
[[0 1 1]
 [1 0 0]]
'''
print(np.argsort(x,axis=1))     # 二维数组横向排序
'''
[[0 1 2]
 [1 0 2]]
'''
x.sort(axis=1)      # 原地排序，横向
print(x)
'''
[[0 3 4]
 [1 2 2]]
'''
x.sort(axis=0)      # 原地排序，纵向
print(x)
'''
[[0 2 2]
 [1 3 4]]
'''

# 向量内积
a = np.array((5,6,7))
b = np.array((6,6,6))
print(a.dot(b))     # 108   内积
print(np.dot(a,b))  # 108   内积
c = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(c.dot(a))     # [ 38  92 146]     二维数组的每行与一维向量计算内积
print(a.dot(c))     # [ 78  96 114]     一维向量与二维向量的每列计算内积

'''
数组元素访问

>>> b = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
>>> b
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> b[0]               # 第0行
array([1, 2, 3])
>>> b[0][0]            # 第0行第0列的元素值
1
>>> b[0, 2]            # 第0行第2列的元素值
3
>>> b[[0, 1]]          # 第0行和第1行
array([[1, 2, 3],
       [4, 5, 6]])
>>> b[[0,1], [1,2]]    #第0行第1列的元素和第1行第2列的元素
array([2, 6])
>>> x = np.arange(0, 100, 10, dtype=np.float64)
>>> x
array([  0.,  10.,  20.,  30.,  40.,  50.,  60.,  70.,  80.,  90.])
>>> x[[1, 3, 5]]                 # 同时访问多个位置上的元素
array([ 10.,  30.,  50.])
>>> x[[1, 3, 5]] = 3             # 把多个位置上的元素改为相同的值
>>> x
array([  0.,   3.,  20.,   3.,  40.,   3.,  60.,  70.,  80.,  90.])
>>> x[[1, 3, 5]] = [34, 45, 56]  # 把多个位置上的元素改为不同的值
>>> x
array([  0.,  34.,  20.,  45.,  40.,  56.,  60.,  70.,  80.,  90.])

'''

# 数组元素访问与修改
x = np.arange(8)
print(x)    # [0 1 2 3 4 5 6 7]
print(np.append(x,8))   # [0 1 2 3 4 5 6 7 8]   返回新数组，增加元素
print(np.append(x,[9,10]))      # [ 0  1  2  3  4  5  6  7  9 10]
print(x)    # [0 1 2 3 4 5 6 7]   不影响原来数组
x[3] = 8    # 原地修改
print(x)    # [0 1 2 8 4 5 6 7]
print(np.insert(x,1,9))     # [0 9 1 2 8 4 5 6 7]  返回新数组，插入元素
print(x)    # [0 1 2 8 4 5 6 7]
print(x.repeat(3))  # 元素重复，返回新数组 [0 0 0 1 1 1 2 2 2 8 8 8 4 4 4 5 5 5 6 6 6 7 7 7]

x = np.arange(0,100,10,dtype=np.floating)
print(np.sin(x))    # 一维数组中所有元素求正弦值
'''
[ 0.         -0.54402111  0.91294525 -0.98803162  0.74511316 -0.26237485
 -0.30481062  0.77389068 -0.99388865  0.89399666]
'''
print(np.round(np.sin(x)))  # 四舍五入 [ 0. -1.  1. -1.  1. -0. -0.  1. -1.  1.]
x = np.random.rand(10)*10
print(x)
'''
[9.38431723 5.35784655 8.51835241 6.98117107 1.60421941 4.07383024
 3.33885448 3.04477929 9.78730745 5.35766814]
'''
print(np.floor(x))      # 所有元素向下取整
# [9. 5. 8. 6. 1. 4. 3. 3. 9. 5.]
print(np.ceil(x))       # 所有元素向上取整
# [10.  6.  9.  7.  2.  5.  4.  4. 10.  6.]

'''
>>> np.absolute(-3)                # 绝对值或模
3
>>> np.absolute(3+4j)
5.0
>>> np.ceil(np.array([1, 2, 3.1])) # 向上取整
array([ 1.,  2.,  4.])
>>> np.isnan(np.NAN)
True
>>> np.log2(8)                     # 对数
3.0
>>> np.log10([100, 1000, 10000])
array([ 2.,  3.,  4.])
>>> np.sqrt(range(10))             # 平方根
array([ 0.        ,  1.        ,  1.41421356,  1.73205081,  2.   ,
        2.23606798,  2.44948974,  2.64575131,  2.82842712,  3.    ])

'''

a = np.arange(1,11,1)
print(a)    # [ 1  2  3  4  5  6  7  8  9 10]
a.shape = 2,5   # 改为2行5列
print(a)
'''
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
'''

# 切片操作
a = np.arange(10)
print(a)
print(a[::-1])      # 反向切片
'''
[0 1 2 3 4 5 6 7 8 9]
[9 8 7 6 5 4 3 2 1 0]       
'''
print(a[::2])   # [0 2 4 6 8]
print(a[:5])    # [0 1 2 3 4]

b = np.arange(25)
b.shape = 5,5
print(b)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
'''
print(b[0,2:5])     # [2 3 4] 第0行中下标[2,5)之间的元素值
print(b[1])     # [5 6 7 8 9]
print(b[2:5,2:5])
'''
[[12 13 14]
 [17 18 19]
 [22 23 24]]
'''

# 布尔运算
x = np.random.rand(10)
print(x)
'''
[0.25616799 0.91175069 0.81279466 0.45911747 0.50661507 0.4079097
 0.68581404 0.31345054 0.78393175 0.18234152]
'''
print(x > 0.65)     # 比较数组中每个元素值是否大于0.5 [False False False  True  True False False  True False False]
print(x[x>0.5])     # 获取数组中大于0.5的元素，可用于检测和过滤异常值
'''
[0.69789291 0.61247368 0.6567679  0.87979325 0.52037319 0.55439812
 0.58207318 0.81341839 0.73026033]
'''
print(np.all(x<1))  # True 测试是否全部元素都小于1

'''
取整运算

>>> x = np.random.rand(10)*50      # 10个随机数
>>> x
array([ 43.85639765,  30.47354735,  43.68965984,  38.92963767,
         9.20056878,  21.34765863,   4.61037809,  17.99941701,
        19.70232038,  30.05059154])
>>> np.int64(x)                    # 取整
array([43, 30, 43, 38,  9, 21,  4, 17, 19, 30], dtype=int64)
>>> np.int32(x)
array([43, 30, 43, 38,  9, 21,  4, 17, 19, 30])
>>> np.int16(x)
array([43, 30, 43, 38,  9, 21,  4, 17, 19, 30], dtype=int16)
>>> np.int8(x)
array([43, 30, 43, 38,  9, 21,  4, 17, 19, 30], dtype=int8)
'''
'''
广播

>>> a = np.arange(0,60,10).reshape(-1,1)     # 列向量
>>> b = np.arange(0,6)                       # 行向量
>>> a
array([[ 0],
       [10],
       [20],
       [30],
       [40],
       [50]])
>>> b
array([0, 1, 2, 3, 4, 5])
>>> a[0] + b                                 # 数组与标量的加法
array([0, 1, 2, 3, 4, 5])
>>> a[1] + b
array([10, 11, 12, 13, 14, 15])
>>> a + b                                     # 广播
array([[ 0,  1,  2,  3,  4,  5],
       [10, 11, 12, 13, 14, 15],
       [20, 21, 22, 23, 24, 25],
       [30, 31, 32, 33, 34, 35],
       [40, 41, 42, 43, 44, 45],
       [50, 51, 52, 53, 54, 55]])
>>> a * b
array([[  0,   0,   0,   0,   0,   0],
       [  0,  10,  20,  30,  40,  50],
       [  0,  20,  40,  60,  80, 100],
       [  0,  30,  60,  90,  120, 150],
       [  0,  40,  80,  120, 160, 200],
       [  0,  50,  100, 150,  200, 250]])
'''

# 矩阵运算-matrix()函数继承自adarray对象，与线性代数中的矩阵概念几乎相同
a_list = [3,5,7]
a_mat = np.matrix(a_list)
print(a_mat)    # [[3 5 7]]  创建矩阵
print(a_mat.T)  # 转置
'''
[[3]
 [5]
 [7]]
'''
print(a_mat.shape)      # 矩阵形状 (1, 3)
print(a_mat.size)       # 矩阵元素个数 3
'''
>>> a_mat.mean()                         # 元素平均值
5.0
>>> a_mat.sum()                          # 所有元素之和
15
>>> a_mat.max()                          # 最大值
7
>>> a_mat.max(axis=1)                    # 横向最大值
matrix([[7]])
>>> a_mat.max(axis=0)                    # 纵向最大值
matrix([[3, 5, 7]])
>>> b_mat = np.matrix((1, 2, 3))         # 创建矩阵
>>> b_mat
matrix([[1, 2, 3]])
>>> a_mat * b_mat.T                      # 矩阵相乘
matrix([[34]])
'''
'''
>>> c_mat = np.matrix([[1, 5, 3], [2, 9, 6]]) # 创建二维矩阵
>>> c_mat
matrix([[1, 5, 3],
        [2, 9, 6]])
>>> c_mat.argsort(axis=0)                     # 纵向排序后的元素序号
matrix([[0, 0, 0],
        [1, 1, 1]], dtype=int64)
>>> c_mat.argsort(axis=1)                     # 横向排序后的元素序号
matrix([[0, 2, 1],
        [0, 2, 1]], dtype=int64)
>>> d_mat = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>>> d_mat.diagonal()                          # 矩阵对角线元素
matrix([[1, 5, 9]])

>>> np.cov([1, 1, 1, 1, 1])                 # 协方差
array(0.0)
>>> x = [-2.1, -1,  4.3]
>>> y = [3,  1.1,  0.12]
>>> X = np.vstack((x,y))
>>> print(np.cov(X))                        # 协方差
[[ 11.71        -4.286     ]
 [ -4.286        2.14413333]]
>>> print(np.cov(x, y))
[[ 11.71        -4.286     ]
 [ -4.286        2.14413333]]
>>> print(np.cov(x))
11.709999999999999

'''
x = np.linalg.eig([[1,1],[2,2]])    # 特征值 特征向量
print(x)
'''
(array([0., 3.]), array([[-0.70710678, -0.4472136 ],
       [ 0.70710678, -0.89442719]]))
'''
x = np.matrix([[1,2],[3,4]])
y = np.linalg.inv(x)    # 逆矩阵
print(y)
'''
[[-2.   1. ]
 [ 1.5 -0.5]]
'''
print(x*y)
'''
[[1.0000000e+00 0.0000000e+00]
 [8.8817842e-16 1.0000000e+00]]
'''
'''
矩阵QR分解

>>> a = np.matrix([[1, 2, 3], [4, 5, 6]])
>>> np.linalg.qr(a)
(matrix([[-0.24253563, -0.9701425 ],
        [-0.9701425 ,  0.24253563]]), matrix([[-4.12310563, -5.33578375, -6.54846188],
        [ 0.        , -0.72760688, -1.45521375]]))
>>> q, r = np.linalg.qr(a)
>>> np.dot(q, r)
matrix([[ 1.,  2.,  3.],
        [ 4.,  5.,  6.]])

矩阵不同维度上的计算

>>> x = np.matrix(np.arange(0,10).reshape(2,5))  # 二维矩阵
>>> x
matrix([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9]])
>>> x.sum()                                      # 所有元素之和
45
>>> x.sum(axis=0)                                # 纵向求和
matrix([[ 5,  7,  9, 11, 13]])
>>> x.sum(axis=1)                                # 横向求和
matrix([[10],
        [35]])
>>> x.mean()                                     # 平均值
4.5
>>> x.mean(axis=1)
matrix([[ 2.],
        [ 7.]])
>>> x.mean(axis=0)
matrix([[ 2.5,  3.5,  4.5,  5.5,  6.5]])

>>> x.max()                                # 所有元素最大值
9
>>> x.max(axis=0)                          # 纵向最大值
matrix([[5, 6, 7, 8, 9]])
>>> x.max(axis=1)                          # 横向最大值
matrix([[4],
        [9]])
>>> weight = [0.3, 0.7]                    # 权重
>>> np.average(x, axis=0, weights=weight)
matrix([[ 3.5,  4.5,  5.5,  6.5,  7.5]])

>>> x = np.matrix(np.random.randint(0, 10, size=(3,3)))
>>> x
matrix([[3, 7, 4],
        [5, 1, 8],
        [2, 7, 0]])
>>> x.std()                         # 标准差
2.6851213274654606
>>> x.std(axis=1)                   # 横向标准差
matrix([[ 1.69967317],
        [ 2.86744176],
        [ 2.94392029]])
>>> x.std(axis=0)                   # 纵向标准差
matrix([[ 1.24721913,  2.82842712,  3.26598632]])
>>> x.var(axis=0)                   # 纵向方差
matrix([[  1.55555556,   8.        ,  10.66666667]])


'''

# 读写文件
x = np.random.rand(4,10)
np.save('data.npy',x)
y = np.load('data.npy')
print(y)
'''
[[0.04605112 0.3042103  0.89161597 0.5732083  0.14461034 0.15276931
  0.69078951 0.20805046 0.17053952 0.9951604 ]
 [0.89332957 0.24797349 0.03270148 0.91523741 0.41680887 0.57132708
  0.47927427 0.25573205 0.20861236 0.96784573]
 [0.93784657 0.33465517 0.71366382 0.82048306 0.02241029 0.48154685
  0.97937577 0.08177457 0.55677193 0.63000558]
 [0.60328586 0.43406708 0.35006361 0.22104753 0.88189998 0.89823294
  0.69307286 0.35399624 0.6511284  0.99673536]]
'''

# scipy在numpy的基础上增加了大量用于数学计算、科学计算以及工程计算的模块，包括线性代数、常微分方程数值求解、信号处理、图像处理、稀疏矩阵等等。
'''
模块	说明
constants	常数
special	特殊函数
optimize	数值优化算法，如最小二乘拟合（leastsq）、函数最小值（fmin系列）、非线性方程组求解（fsolve）等等
interpolate	插值（interp1d、interp2d等等）
integrate	数值积分
signal	信号处理
ndimage	图像处理，包括滤波器模块filters、傅里叶变换模块fourier、图像插值模块interpolation、图像测量模块measurements、形态学图像处理模块morphology等等
stats	统计
misc	提供了读取图像文件的方法和一些测试图像
io	提供了读取Matlab和Fortran文件的方法
'''
from scipy import constants as C
print(C.pi)     # 圆周率
# 3.141592653589793
print(C.golden)  # 黄金比例
# 1.618033988749895
'''
>>> C.c                       # 真空中的光速
299792458.0
>>> C.h                       # 普朗克常数
6.62606896e-34
>>> C.mile                    # 一英里等于多少米
1609.3439999999998
>>> C.inch                    # 一英寸等于多少米
0.0254
>>> C.degree                  # 一度等于多少弧度
0.017453292519943295
>>> C.minute                  # 一分钟等于多少秒
60.0
>>> C.g                       # 标准重力加速度
9.80665
'''
'''
scipy的special模块包含了大量函数库，包括基本数学函数、特殊函数以及numpy中的所有函数。

>>> from scipy import special as S
>>> S.cbrt(8)                # 立方根
2.0
>>> S.exp10(3)               # 10**3
1000.0
>>> S.sindg(90)              # 正弦函数，参数为角度
1.0
>>> S.round(3.1)             # 四舍五入函数
3.0
>>> S.round(3.5)
4.0
>>> S.round(3.499)
3.0

>>> S.comb(5, 3)              # 从5个中任选3个的组合数
10.0
>>> S.perm(5, 3)              # 排列数
60.0
>>> S.gamma(4)                # gamma函数
6.0
>>> S.beta(10, 200)           # beta函数
2.839607777781333e-18
>>> S.sinc(0)                 # sinc函数
1.0
>>> S.sinc(1)
3.8981718325193755e-17

signal模块包含大量滤波函数、B样条插值算法等等。

>>> import numpy as np
>>> x = np.array([1, 2, 3])
>>> h = np.array([4, 5, 6])
>>> import scipy.signal
>>> scipy.signal.convolve(x, h)             # 一维卷积运算
array([ 4, 13, 28, 27, 18])


'''
# 二维图像卷积运算
# from scipy import signal
# from scipy import misc
# import matplotlib.pyplot as plt
# face = misc.face(gray=True)
# scharr = np.array([[ -3-3j, 0-10j,  +3 -3j],
#                    [-10+0j, 0+ 0j,  +10 +0j],
#                    [ -3+3j, 0+10j,  +3 +3j]])  # Gx + j*Gy
# grad = signal.convolve2d(face,scharr,boundary = 'sum',mode = 'same')

'''
pandas主要提供了3种数据结构：
1）Series，带标签的一维数组；
2）DataFrame，带标签且大小可变的二维表格结构；
3）Panel，带标签且大小可变的三维数组。
'''
import pandas as pd
x = pd.Series([1,3,5,np.nan])
print(x)
'''
0    1.0
1    3.0
2    5.0
3    NaN
dtype: float64
'''
y = pd.date_range(start='20221127',end='20221230',freq='H')
print(y)
'''
DatetimeIndex(['2022-11-27 00:00:00', '2022-11-27 01:00:00',
               '2022-11-27 02:00:00', '2022-11-27 03:00:00',
               '2022-11-27 04:00:00', '2022-11-27 05:00:00',
               '2022-11-27 06:00:00', '2022-11-27 07:00:00',
               '2022-11-27 08:00:00', '2022-11-27 09:00:00',
               ...
               '2022-12-29 15:00:00', '2022-12-29 16:00:00',
               '2022-12-29 17:00:00', '2022-12-29 18:00:00',
               '2022-12-29 19:00:00', '2022-12-29 20:00:00',
               '2022-12-29 21:00:00', '2022-12-29 22:00:00',
               '2022-12-29 23:00:00', '2022-12-30 00:00:00'],
              dtype='datetime64[ns]', length=793, freq='H')
'''
'''
>>> dates = pd.date_range(start='20210101', end='20211231', freq='D')
                                                               # 间隔为天
>>> dates
DatetimeIndex(['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',
               '2021-01-05', '2021-01-06', '2021-01-07', '2021-01-08',
               '2021-01-09', '2021-01-10',
               ...
               '2021-12-22', '2021-12-23', '2021-12-24', '2021-12-25',
               '2021-12-26', '2021-12-27', '2021-12-28', '2021-12-29',
               '2021-12-30', '2021-12-31'],
              dtype='datetime64[ns]', length=365, freq='D')

>>> dates = pd.date_range(start='20210101', end='20211231', freq='M')
                                                                 # 间隔为月
>>> dates
DatetimeIndex(['2021-01-31', '2021-02-28', '2021-03-31', '2021-04-30',
               '2021-05-31', '2021-06-30', '2021-07-31', '2021-08-31',
               '2021-09-30', '2021-10-31', '2021-11-30', '2021-12-31'],
              dtype='datetime64[ns]', freq='M')

>>> pd.period_range('20170601', '20170630', freq='W')
PeriodIndex(['2017-05-29/2017-06-04', '2017-06-05/2017-06-11',
             '2017-06-12/2017-06-18', '2017-06-19/2017-06-25',
             '2017-06-26/2017-07-02'],
            dtype='period[W-SUN]', freq='W-SUN')
>>> pd.period_range('20170601', '20170630', freq='D')
PeriodIndex(['2017-06-01', '2017-06-02', '2017-06-03', '2017-06-04',
             '2017-06-05', '2017-06-06', '2017-06-07', '2017-06-08',
             '2017-06-09', '2017-06-10', '2017-06-11', '2017-06-12',
             '2017-06-13', '2017-06-14', '2017-06-15', '2017-06-16',
             '2017-06-17', '2017-06-18', '2017-06-19', '2017-06-20',
             '2017-06-21', '2017-06-22', '2017-06-23', '2017-06-24',
             '2017-06-25', '2017-06-26', '2017-06-27', '2017-06-28',
             '2017-06-29', '2017-06-30'],
            dtype='period[D]', freq='D')

>>> pd.period_range('20170601', '20170630', freq='H')
PeriodIndex(['2017-06-01 00:00', '2017-06-01 01:00', '2017-06-01 02:00',
             '2017-06-01 03:00', '2017-06-01 04:00', '2017-06-01 05:00',
             '2017-06-01 06:00', '2017-06-01 07:00', '2017-06-01 08:00',
             '2017-06-01 09:00',
             ...
             '2017-06-29 15:00', '2017-06-29 16:00', '2017-06-29 17:00',
             '2017-06-29 18:00', '2017-06-29 19:00', '2017-06-29 20:00',
             '2017-06-29 21:00', '2017-06-29 22:00', '2017-06-29 23:00',
             '2017-06-30 00:00'],
            dtype='period[H]', length=697, freq='H')


生成DataFrame

>>> pd.DataFrame(np.random.randn(12,4), index=dates, columns=list('ABCD'))
                   A         B         C         D
2021-01-31  1.628310 -0.281223  0.247675 -1.604243
2021-02-28  0.071069  1.310116 -0.945838 -0.613267
2021-03-31  0.956887 -1.691863  0.170843 -0.387298
2021-04-30  0.869391 -1.939210  2.220454  1.654112
2021-05-31 -0.802416  0.558953  1.086787 -0.870317
2021-06-30  0.463761  2.451659  0.165985  0.913551
2021-07-31  1.755720  1.246089 -0.237590 -0.892358
2021-08-31  0.191604 -1.481263 -0.142491 -2.672721
2021-09-30 -0.146444  0.493261 -1.719681  0.676592
2021-10-31  1.153289  0.179862 -1.879004 -0.616305
2021-11-30 -0.500726  1.057525  0.140623 -0.113951
2021-12-31  0.229572 -0.778378 -0.682233  0.009218


>>> pd.DataFrame([np.random.randint(1, 100, 4) for i in range(12)],
	          index=dates, columns=list('ABCD'))   # 4列随机数
             A   B   C   D
2021-01-31  17  72  26  13
2021-02-28  61  42  88   3
2021-03-31  14  61  97  95
2021-04-30  73  87  55   1
2021-05-31  58  80  20   2
2021-06-30  41   6  40  70
2021-07-31  51  48  81  77
2021-08-31  56  54  76  61
2021-09-30  32  27  82  76
2021-10-31  21  78  91  15
2021-11-30  75  77  17  50
2021-12-31  54  12  75  53


>>> pd.DataFrame({'A':np.random.randint(1, 100, 4),
	  	   'B':pd.date_range(start='20210101', periods=4, freq='D'),
		   'C':pd.Series([1, 2, 3, 4],index=list(range(4)),dtype='float32'),
		   'D':np.array([3] * 4,dtype='int32'),
		   'E':pd.Categorical(["test","train","test","train"]),
		   'F':'foo'})
    A          B    C  D      E    F
0  65 2021-01-01  1.0  3   test  foo
1  18 2021-01-02  2.0  3  train  foo
2  24 2021-01-03  3.0  3   test  foo
3  32 2021-01-04  4.0  3  train  foo


>>> df = pd.DataFrame({'A':np.random.randint(1, 100, 4),
		        'B':pd.date_range(start='20210101', periods=4, freq='D'),
		        'C':pd.Series([1, 2, 3, 4],\
                               index=['zhang', 'li', 'zhou', 'wang'],dtype='float32'),
		        'D':np.array([3] * 4,dtype='int32'),
		        'E':pd.Categorical(["test","train","test","train"]),
		        'F':'foo'})
>>> df
        A          B    C  D      E    F
zhang  20 2021-01-01  1.0  3   test  foo
li     26 2021-01-02  2.0  3  train  foo
zhou   63 2021-01-03  3.0  3   test  foo
wang   69 2021-01-04  4.0  3  train  foo

'''
df = pd.DataFrame({'A':np.random.randint(1, 100, 4),
		        'B':pd.date_range(start='20210101', periods=4, freq='D'),
		        'C':pd.Series([1, 2, 3, 4],\
                               index=['zhang', 'li', 'zhou', 'wang'],dtype='float32'),
		        'D':np.array([3] * 4,dtype='int32'),
		        'E':pd.Categorical(["test","train","test","train"]),
		        'F':'foo'})


print(df)
'''
        A          B    C  D      E    F
zhang  71 2021-01-01  1.0  3   test  foo
li     79 2021-01-02  2.0  3  train  foo
zhou   70 2021-01-03  3.0  3   test  foo
wang   76 2021-01-04  4.0  3  train  foo
'''
print(df.head(2))
'''
        A          B    C  D      E    F
zhang  29 2021-01-01  1.0  3   test  foo
li     62 2021-01-02  2.0  3  train  foo
'''
'''
（3）二维数据查看

>>> df.head()        # 默认显示前5行
        A          B    C  D      E    F
zhang  20 2021-01-01  1.0  3   test  foo
li     26 2021-01-02  2.0  3  train  foo
zhou   63 2021-01-03  3.0  3   test  foo
wang   69 2021-01-04  4.0  3  train  foo
>>> df.head(3)       # 查看前3行
        A          B    C  D      E    F
zhang  20 2021-01-01  1.0  3   test  foo
li     26 2021-01-02  2.0  3  train  foo
zhou   63 2021-01-03  3.0  3   test  foo
>>> df.tail(2)       # 查看最后2行
       A          B    C  D      E    F
zhou  63 2021-01-03  3.0  3   test  foo
wang  69 2021-01-04  4.0  3  train  foo


（4）查看二维数据的索引、列名和数据

>>> df.index
Index(['zhang', 'li', 'zhou', 'wang'], dtype='object')
>>> df.columns
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
>>> df.values
array([[20, Timestamp('2021-01-01 00:00:00'), 1.0, 3, 'test', 'foo'],
       [26, Timestamp('2021-01-02 00:00:00'), 2.0, 3, 'train', 'foo'],
       [63, Timestamp('2021-01-03 00:00:00'), 3.0, 3, 'test', 'foo'],
       [69, Timestamp('2021-01-04 00:00:00'), 4.0, 3, 'train', 'foo']], dtype=object)

7）排序

>>> df.sort_index(axis=0, ascending=False)     # 对轴进行排序
        A          B    C  D      E    F
zhou   63 2021-01-03  3.0  3   test  foo
zhang  20 2021-01-01  1.0  3   test  foo
wang   69 2021-01-04  4.0  3  train  foo
li     26 2021-01-02  2.0  3  train  foo
>>> df.sort_index(axis=0, ascending=True)
        A          B    C  D      E    F
li     26 2021-01-02  2.0  3  train  foo
wang   69 2021-01-04  4.0  3  train  foo
zhang  20 2021-01-01  1.0  3   test  foo
zhou   63 2021-01-03  3.0  3   test  foo

（8）数据选择

>>> df['A']                                     # 选择列
zhang    20
li       26
zhou     63
wang     69
Name: A, dtype: int32
>>> 69 in df['A']
False
>>> 69 in df['A'].values
True

>>> df.iloc[0,1]                   # 查询第0行第1列位置的数据值
Timestamp('2021-01-01 00:00:00')
>>> df.iloc[2,2]                   # 查询第2行第2列位置的数据值
3.0
>>> df[df.A>50]                    # 按给定条件进行查询
       A          B    C  D      E    F
zhou  63 2021-01-03  3.0  3   test  foo
wang  69 2021-01-04  4.0  3  train  foo
>>> df[df['E']=='test']            # 按给定条件进行查询
        A          B    C  D     E    F
zhang  20 2021-01-01  1.0  3  test  foo
zhou   63 2021-01-03  3.0  3  test  foo
>>> df[df['A'].isin([20,69])]
        A          B    C  D      E    F
zhang  20 2021-01-01  1.0  3   test  foo
wang   69 2021-01-04  4.0  3  train  foo

>>> df.nlargest(3, ['C'])         # 返回指定列最大的前3行
       A          B    C  D      E    F
wang  69 2021-01-04  4.0  3  train  foo
zhou  63 2021-01-03  3.0  3   test  foo
li    26 2021-01-02  2.0  3  train  foo
>>> df.nlargest(3, ['A'])
       A          B    C  D      E    F
wang  69 2021-01-04  4.0  3  train  foo
zhou  63 2021-01-03  3.0  3   test  foo
li    26 2021-01-02  2.0  3  train  foo

（9）数据修改

>>> df.iat[0, 2] = 3                 # 修改指定行、列位置的数据值
>>> df.loc[:, 'D'] = np.random.randint(50, 60, 4)
                                     # 修改某列的值
>>> df['C'] = -df['C']               # 对指定列数据取反
>>> df                               # 查看修改结果
        A          B    C   D      E    F
zhang  20 2021-01-01 -3.0  53   test  foo
li     26 2021-01-02 -2.0  59  train  foo
zhou   63 2021-01-03 -3.0  59   test  foo
wang   69 2021-01-04 -4.0  50  train  foo





'''


'''
matplotlib模块依赖于numpy模块和tkinter模块，可以绘制多种形式的图形，包括折线图、直方图、饼状图、散点图、误差线图等等。
'''
# import numpy as np
# import pylab as pl
# import matplotlib.font_manager as fm
# import matplotlib.pylab as pl1
# myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\Calibri.ttf')   # 设置字体
# t = np.arange(0.0,2.0*np.pi,0.01)   # 自变量取值范围
# s = np.sin(t)    # 计算正弦函数值
# z = np.cos(t)    # 计算余弦函数值
# pl.plot(t,s,label='正弦')
# pl.plot(t,z,label='余弦')
# pl.xlabel('x-变量', fontproperties='Calibri', fontsize=18) # 设置x标签
# pl.ylabel('y-正弦余弦函数值', fontproperties='Calibri', fontsize=18)
# pl.title('sin-cos函数图像', fontproperties='Calibri', fontsize=24)
# pl.legend(prop=myfont)
# 设置图例
# pl.show()

# a = np.arange(0,2.0*np.pi,0.1)
# b = np.cos(a)
# pl.scatter(a,b)
# pl.scatter(a, b, s=20, marker='+')
# pl.show()
#
# x = np.random.random(100)
# y = np.random.random(100)
# pl1.scatter(x, y, s=x*500, c='r', marker='*')
# s指大小，c指颜色，marker指符号形状
# pl1.show()

# 绘制饼状图
# import numpy as np
# import matplotlib.pyplot as plt
#
# #The slices will be ordered and plotted counter-clockwise.
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# colors = ['yellowgreen', 'gold', '#FF0000', 'lightcoral']
# explode = (0, 0.1, 0, 0.1)              # 使饼状图中第2片和第4片裂开
#
# fig = plt.figure()
# ax = fig.gca()
# ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,
#        autopct='%1.1f%%', shadow=True, startangle=90,
#        radius=0.25, center=(0, 0), frame=True)   # autopct设置饼内百分比的格式
# ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,
#        autopct='%1.1f%%', shadow=True, startangle=45,
#        radius=0.25, center=(1, 1), frame=True)
# ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,
#        autopct='%1.1f%%', shadow=True, startangle=90,
#        radius=0.25, center=(0, 1), frame=True)
# ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,
#        autopct='%1.2f%%', shadow=False, startangle=135,
#        radius=0.35, center=(1, 0), frame=True)
# ax.set_xticks([0, 1])                    # 设置坐标轴刻度
# ax.set_yticks([0, 1])
#
# ax.set_xticklabels(["Sunny", "Cloudy"])  # 设置坐标轴刻度上的标签
# ax.set_yticklabels(["Dry", "Rainy"])
#
# ax.set_xlim((-0.5, 1.5))                 # 设置坐标轴跨度
# ax.set_ylim((-0.5, 1.5))
#
# ax.set_aspect('equal')                   # 设置纵横比相等
#
# plt.show()

# 使用pyplot绘制，多个图形在一起显示
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(0, 2*np.pi, 500)
# y = np.sin(x)
# z = np.cos(x*x)
# plt.figure(figsize=(8,4))
# # 标签前后加$将使用内嵌的LaTex引擎将其显示为公式
# plt.plot(x, y, label='$sin(x)$', color='red', linewidth=2) # 红色，2个像素宽
# plt.plot(x, z, 'b--', label='$cos(x^2)$')                  # 蓝色，虚线
# plt.xlabel('Time(s)')
# plt.ylabel('Volt')
# plt.title('Sin and Cos figure using pyplot')
# plt.ylim(-1.2, 1.2)
# plt.legend()                                         # 显示图例
# plt.show()                                           # 显示绘图窗口


# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.linspace(0, 2*np.pi, 500)           # 创建自变量数组
# y1 = np.sin(x)                             # 创建函数值数组
# y2 = np.cos(x)
# y3 = np.sin(x*x)
# plt.figure(1)                              # 创建图形
# ax1 = plt.subplot(2, 2, 1)                 # 第一行第一列图形
# ax2 = plt.subplot(2, 2, 2)                 # 第一行第二列图形
# ax3 = plt.subplot(212, facecolor='y')      # 第二行
# plt.sca(ax1)                               # 选择ax1
# plt.plot(x, y1, color='red')               # 绘制红色曲线
# plt.ylim(-1.2, 1.2)                        # 限制y坐标轴范围
# plt.sca(ax2)                               # 选择ax2
# plt.plot(x, y2, 'b--')                     # 绘制蓝色曲线
# plt.ylim(-1.2, 1.2)
# plt.sca(ax3)                               # 选择ax3
# plt.plot(x, y3, 'g--')
# plt.ylim(-1.2, 1.2)
# plt.show()

# 绘制三维图形
# import numpy as np
# import matplotlib.pyplot as plt
# import mpl_toolkits.mplot3d
#
# x,y = np.mgrid[-2:2:20j, -2:2:20j]        # 步长使用虚数
#                                           # 虚部表示点的个数
#                                           # 并且包含end
# z = 50 * np.sin(x+y)                      # 测试数据
# ax = plt.subplot(111, projection='3d')    # 三维图形
# ax.plot_surface(x, y, z, rstride=2, cstride=1, cmap=plt.cm.Blues_r)
# ax.set_xlabel('X')                        # 设置坐标轴标签
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()


# import pylab as pl
# import numpy as np
# import mpl_toolkits.mplot3d
# rho, theta = np.mgrid[0:1:40j, 0:2*np.pi:40j]
# z = rho**2
# x = rho*np.cos(theta)
# y = rho*np.sin(theta)
# ax = pl.subplot(111, projection='3d')
# ax.plot_surface(x, y, z)
# pl.show()


# import matplotlib as mpl
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import axes3d
#
# mpl.rcParams['legend.fontsize'] = 10        # 图例字号
# fig = plt.figure()
# ax = fig.gca(projection='3d')               # 三维图形
# theta = np.linspace(-4*np.pi, 4*np.pi, 100)
# z = np.linspace(-4, 4, 100)*0.3             # 测试数据
# r = z**3 + 1
# x = r * np.sin(theta)
# y = r * np.cos(theta)
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()
# plt.show()


import random
import string
import wordcloud


def show(s):
	# 创建wordcloud对象
	wc = wordcloud.WordCloud(
		r'C:\windows\fonts\simfang.ttf', width=500, height=400,
		background_color='white', font_step=3,
		random_state=False, prefer_horizontal=0.9)
	# 创建并显示词云
	t = wc.generate(s)
	t.to_image().save('t.png')


# 如果空间足够，就全部显示
# 如果词太多，就按频率显示，频率越高的词越大
show('''hello world 1 1 1 1 1 1 1 1 1 1 1 1 
 abc fgh yhnbgfd 1 1 1 1 1 1 1  Python great Python Python''')








































