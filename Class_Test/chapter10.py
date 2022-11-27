# coder:也
# 开发时间:2022/11/26 22:28

"""
文件夹也称为目录，用于分层保存文件。
"""
'''
Python没有直接操作目录的函数，需要使用内置的os及os.path模块实现。
路径—用于定位文件或目录的字符串。
相对路径：依赖于当前工作目录。‘work\Pizza.py’
绝对路径：不依赖于当前工作目录。’ D:\Program Files\Python310\work\Pizza.py’
Python下路径表示(Window操作系统)
r’ D:\Program Files\Python310\work\Pizza.py’
’ D:\\Program Files\\Python310\\work\\Pizza.py’
’ D:/Program Files/Python310/work/Pizza.py’

目录操作函数
函数名称	使用说明
mkdir(path[, mode=0o777])	创建目录，要求上级目录必须存在
makedirs(path1/path2…,     mode=511)	创建多级目录，会根据需要自动创建中间缺失的目录
rmdir(path)	删除目录，要求该文件夹中不能有文件或子文件夹
removedirs(path1/path2…)	删除多级目录
listdir(path) 	返回指定目录下所有文件信息
getcwd()	返回当前工作目录
chdir(path) 	把path设为当前工作目录
walk(top, topdown=True, onerror=None)	遍历目录树，该方法返回一个元组，包括3个元素：所有路径名、所有目录列表与文件列表

文件操作函数
方法（属性）	功能说明
os.curdir	当前文件夹
os.environ	包含系统环境变量和值的字典
os.extsep	当前操作系统所使用的文件扩展名分隔符
os.get_exec_path()	返回可执行文件的搜索路径
os.sep	当前操作系统所使用的路径分隔符
os.stat(path)	返回文件的所有属性
方法	功能说明
access(path, mode)	测试是否可以按照mode指定的权限访问文件
chmod(path, mode, *, dir_fd=None, follow_symlinks=True)	改变文件的访问权限
remove(path)	删除指定的文件，要求用户拥有删除文件的权限，并且文件没有只读或其他特殊属性
rename(src, dst)	重命名文件或目录，可以实现文件的移动，若目标文件已存在则抛出异常，不能跨越磁盘或分区
replace(old, new)	重命名文件或目录，若目标文件已存在则直接覆盖，不能跨越磁盘或分区
scandir(path='.')	返回包含指定文件夹中所有DirEntry对象的迭代对象，遍历文件夹时比listdir()更加高效
startfile(filepath [, operation])	使用关联的应用程序打开指定文件或启动指定应用程序
system()	启动外部程序


如果需要遍历指定目录下所有子目录和文件，可以使用递归的方法。
from os import listdir
from os.path import join, isfile, isdir

def listDirDepthFirst(directory):
    
    #遍历文件夹，如果是文件就直接输出
    #如果是文件夹，就输出显示，然后递归遍历该文件夹
    for subPath in listdir(directory):
        path = join(directory, subPath)
        if isfile(path):
            print(path)
        elif isdir(path):
            print(path)
            listDirDepthFirst(path)

下面的代码使用了广度优先遍历方法。

from os import listdir
from os.path import join, isfile, isdir

def listDirWidthFirst(directory):
    #使用列表模拟双端队列，效率稍微受影响，不过关系不大
    dirs = [directory]
    #如果还有没遍历过的文件夹，继续循环
    while dirs:
        #遍历还没遍历过的第一项
        current = dirs.pop(0)
        #遍历该文件夹，如果是文件就直接输出显示
        #如果是文件夹，输出显示后，标记为待遍历项
        for subPath in listdir(current):
            path = join(current, subPath)
            if isfile(path):
                print(path)
            elif isdir(path):
                print(path)
                dirs.append(path)

os.path模块
方法	功能说明
abspath(path)	返回给定路径的绝对路径
basename(path)	返回指定路径的最后一个组成部分
commonpath(paths)	返回给定的多个路径的最长公共路径
commonprefix(paths)	返回给定的多个路径的最长公共前缀
dirname(p)	返回给定路径的文件夹部分
exists(path)	判断文件是否存在
getatime(filename)	返回文件的最后访问时间 
getctime(filename)	返回文件的创建时间 
getmtime(filename)	返回文件的最后修改时间
getsize(filename)	返回文件的大小
isabs(path)	判断path是否为绝对路径
isdir(path)	判断path是否为文件夹
isfile(path)	判断path是否为文件
join(path, *paths)	连接两个或多个path
realpath(path)	返回给定路径的绝对路径
relpath(path)	返回给定路径的相对路径，不能跨越磁盘驱动器或分区
samefile(f1, f2)	测试f1和f2这两个路径是否引用的同一个文件
split(path)	以路径中的最后一个斜线为分隔符把路径分隔成两部分，以元组形式返回
splitext(path)	从路径中分隔文件的扩展名
splitdrive(path)	从路径中分隔驱动器的名称

>>> path='D:\\mypython_exp\\new_test.txt'
>>> os.path.dirname(path)                      #返回路径的文件夹名
'D:\\mypython_exp'
>>> os.path.basename(path)                     #返回路径的最后一个组成部分
'new_test.txt'
>>> os.path.split(path)                        #切分文件路径和文件名
('D:\\mypython_exp', 'new_test.txt')
>>> os.path.split('')                          #切分结果为空字符串
('', '')
>>> os.path.split('C:\\windows')               #以最后一个斜线为分隔符
('C:\\', 'windows')
>>> os.path.split('C:\\windows\\')
('C:\\windows', '')
>>> os.path.splitdrive(path)                   #切分驱动器符号
('D:', '\\mypython_exp\\new_test.txt')
>>> os.path.splitext(path)                     #切分文件扩展名
('D:\\mypython_exp\\new_test', '.txt')
>>> os.path.commonpath([r'C:\windows\notepad.exe', r'C:\windows\system'])
'C:\\windows'
>>> os.path.commonpath([r'a\b\c\d', r'a\b\c\e'])    #返回路径中的共同部分
'a\\b\\c'
>>> os.path.commonprefix([r'a\b\c\d', r'a\b\c\e'])  #返回字符串的最长公共前缀
'a\\b\\c\\'
>>> os.path.realpath('tttt.py')                     #返回绝对路径
'C:\\Python 3.5\\tttt.py'
>>> os.path.abspath('tttt.py')                      #返回绝对路径
'C:\\Python 3.5\\tttt.py'
>>> os.path.relpath('C:\\windows\\notepad.exe')     #返回相对路径
'..\\windows\\notepad.exe'
>>> os.path.relpath('D:\\windows\\notepad.exe')     #相对路径不能跨越分区
ValueError: path is on mount 'D:', start on mount 'C:'
>>> os.path.relpath('C:\\windows\\notepad.exe','dlls')
                                              #指定相对路径的基准位置
'..\\..\\windows\\notepad.exe'

shutil模块
方法	功能说明
copy(src, dst)	复制文件，新文件具有同样的文件属性，如果目标文件已存在则抛出异常
copy2(src, dst)	复制文件，新文件具有原文件完全一样的属性，包括创建时间、修改时间和最后访问时间等等，如果目标文件已存在则抛出异常
copyfile(src, dst)	复制文件，不复制文件属性，如果目标文件已存在则直接覆盖
copyfileobj(fsrc, fdst)	在两个文件对象之间复制数据，例如copyfileobj(open('123.txt'), open('456.txt', 'a'))
copymode(src, dst)	把src的模式位（mode bit）复制到dst上，之后二者具有相同的模式
copystat(src, dst)	把src的模式位、访问时间等所有状态都复制到dst上
copytree(src, dst)	递归复制文件夹
disk_usage(path)	查看磁盘使用情况
move(src, dst)	移动文件或递归移动文件夹，也可以给文件和文件夹重命名
rmtree(path)	递归删除文件夹
make_archive(base_name, format, root_dir=None, base_dir=None)	创建tar或zip格式的压缩文件
unpack_archive(filename, extract_dir=None, format=None)	解压缩压缩文件

下面的代码演示了如何使用标准库shutil的copyfile()方法复制文件。
>>> import shutil                                   #导入shutil模块
>>> shutil.copyfile('C:\\dir.txt', 'C:\\dir1.txt')  #复制文件
下面的代码将C:\Python38\Dlls文件夹以及该文件夹中所有文件压缩至D:\a.zip文件：
>>> shutil.make_archive('D:\\a', 'zip', 'C:\\Python38', 'Dlls')
'D:\\a.zip'
下面的代码将刚压缩得到的文件D:\a.zip解压缩至D:\a_unpack文件夹：
>>> shutil.unpack_archive('D:\\a.zip', 'D:\\a_unpack')
下面的代码使用shutil模块的方法删除刚刚解压缩得到的文件夹：
>>> shutil.rmtree('D:\\a_unpack')

下面的代码使用shutil的copytree()函数递归复制文件夹，并忽略扩展名为pyc的文件和以“新”字开头的文件和子文件夹：

>>> from shutil import copytree, ignore_patterns
>>> copytree('C:\\python38\\test', 'D:\\des_test', 
             ignore=ignore_patterns('*.pyc', '新*'))


例10-1   把指定文件夹中的所有文件名批量随机化，保持文件类型不变。
from string import ascii_letters
from os import listdir, rename
from os.path import splitext, join
from random import choice, randint

def randomFilename(directory):
    for fn in listdir(directory):
        #切分，得到文件名和扩展名
        name, ext = splitext(fn)
        n = randint(5, 20)
        #生成随机字符串作为新文件名
        newName = ''.join((choice(ascii_letters) for i in range(n)))
        #修改文件名
        rename(join(directory, fn), join(directory, newName+ext))

randomFilename('C:\\test')


例10-2  编写程序，进行文件夹增量备份。
程序功能与用法：指定源文件夹与目标文件夹，自动检测自上次备份以来源文件夹中内容的改变，包括修改的文件、新建的文件、新建的文件夹等等，自动复制新增或修改过的文件到目标文件夹中，自上次备份以来没有修改过的文件将被忽略而不复制，从而实现增量备份。本例属于系统运维的范畴。
import os
import filecmp
import shutil
import sys
def autoBackup(scrDir, dstDir):
    if ((not os.path.isdir(scrDir)) or (not os.path.isdir(dstDir)) or
      (os.path.abspath(scrDir)!=scrDir) or (os.path.abspath(dstDir)!=dstDir)):
        usage()
    for item in os.listdir(scrDir):
        scrItem = os.path.join(scrDir, item)
        dstItem = scrItem.replace(scrDir,dstDir)
        if os.path.isdir(scrItem):
            #创建新增的文件夹，保证目标文件夹的结构与原始文件夹一致
            if not os.path.exists(dstItem):
                os.makedirs(dstItem)
                print('make directory'+dstItem)
            #递归调用自身函数
            autoBackup(scrItem, dstItem)
        elif os.path.isfile(scrItem):
            #只复制新增或修改过的文件
            if ((not os.path.exists(dstItem)) or
               (not filecmp.cmp(scrItem, dstItem, shallow=False))):
                shutil.copyfile(scrItem, dstItem)
                print('file:'+scrItem+'==>'+dstItem)
def usage():
    print('scrDir and dstDir must be existing absolute path of certain directory')
    print('For example:{0} c:\\olddir c:\\newdir'.format(sys.argv[0]))
    sys.exit(0)
    
if __name__=='__main__':
    if len(sys.argv)!=3:
        usage()
    scrDir, dstDir= sys.argv[1], sys.argv[2]
    autoBackup(scrDir, dstDir)


例10-3   编写程序，统计指定文件夹大小以及文件和子文件夹数量。本例也属于系统运维范畴，可用于磁盘配额的计算，例如email、博客、FTP、快盘等系统中每个账号所占空间大小的统计。
import os

totalSize = 0
fileNum = 0
dirNum = 0
def visitDir(path):
    global totalSize
    global fileNum
    global dirNum
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        if os.path.isfile(sub_path):
            fileNum = fileNum+1                              #统计文件数量
            totalSize = totalSize+os.path.getsize(sub_path)  #统计文件总大小
        elif os.path.isdir(sub_path):
            dirNum = dirNum+1                                #统计文件夹数量
            visitDir(sub_path)                               #递归遍历子文件夹
def main(path):
    if not os.path.isdir(path):
        print('Error:"', path, '" is not a directory or does not exist.')
        return
    visitDir(path)

def sizeConvert(size):                                   #单位换算
    K, M, G = 1024, 1024**2, 1024**3
    if size >= G:
        return str(size/G)+'G Bytes'
    elif size >= M:
        return str(size/M)+'M Bytes'
    elif size >= K:
        return str(size/K)+'K Bytes'
    else:
        return str(size)+'Bytes'
def output(path):
    print('The total size of '+path+' is:'+sizeConvert(totalSize)
          +'('+str(totalSize)+' Bytes)')
    print('The total number of files in '+path+' is:',fileNum)
    print('The total number of directories in '+path+' is:',dirNum)

if __name__=='__main__':
    path = r'd:\idapro6.5plus'
    main(path)
    output(path)


例10-4   编写程序，递归删除指定文件夹中指定类型的文件和大小为0的文件。
from os.path import isdir, join, splitext
from os import remove, listdir, chmod, stat

filetypes = ('.tmp', '.log', '.obj', '.txt')     #指定要删除的文件类型

def delCertainFiles(directory):
    if not isdir(directory):
        return
    for filename in listdir(directory):
        temp = join(directory, filename)
        if isdir(temp):
            delCertainFiles(temp)                #递归调用
        elif splitext(temp)[1] in filetypes or stat(temp).st_size==0:
            chmod(temp, 0o777)                   #修改文件属性，获取删除权限
            remove(temp)                         #删除文件
            print(temp, ' deleted....')

delCertainFiles(r'C:\test')











'''





































































