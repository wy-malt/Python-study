# coder:也
# 开发时间:2022/11/25 18:39

""""""
'''
定义了类之后，就可以用来实例化对象，并通过“对象名.成员”的方式来访问其中的数据成员或成员方法。
实例创建语法：instanceName = ClassName(parameter list)
成员访问： instanceName.成员名称
>>> car = Car()               #实例化对象
>>> car.infor()               #调用对象的成员方法
This is a car
'''
'''
特殊方法：__init__(self)。
类似Java中构造方法，每当创建类的新实例时，都是自动调用它，必有self参数（this），而且是第一个参数，指向实例本身，用于访问类中的属性和方法。
在方法调用时会自动传递实际参数self
'''


class Car:
    def __init__(self):
        self.color = 'blue'
        print("There is a car")


car = Car()
'''
>>> class Dog:
	    def __init__(self, color=‘Black’, name=‘Tom’, weight=10):
		self._color = color
		self.__name = name
       self.weight =weight

	    def setValue(self, color, name):
		self._color = color
		self.__name = name
	
    def show(self):
		print(self._color)
		print(self.__name)

>>> myDog = Dog()
>>> myDog._color
‘black’
>>> myDog._Dog__name             #在外部访问对象的私有数据成员
‘Tom’
>>> myDog.__name
AttributeError: 'Dog' object has no attribute '__name'
'''
'''
在Python中，以下划线开头的变量名和方法名有特殊的含义，尤其是在类的定义中。
_xxx：受保护成员；
__xxx__：系统定义的特殊成员；
__xxx：私有成员，只有类对象自己能访问，子类对象不能直接访问到这个成员，但在对象外部可以通过“对象名._类名__xxx”这样的特殊方式来访问。
注意：Python中不存在严格意义上的私有成员
'''
'''
利用类数据成员的共享性，可以实时获得该类的对象数量，并且可以控制该类可以创建的对象最大数量。例如：
>>> class Demo(object):
    total = 0
    def __new__(cls, *args, **kwargs):           #该方法在__init__()之前被调用
        if cls.total >= 3:                       #最多允许创建3个对象
            raise Exception('最多只能创建3个对象')
        else:
            return object.__new__(cls)
    def __init__(self):
        Demo.total = Demo.total + 1		
>>> t1 = Demo()
>>> t1
<__main__.Demo object at 0x00000000034A0278>
>>> t2 = Demo()
>>> t3 = Demo()
>>> t4 = Demo()
Exception: 最多只能创建3个对象
>>> t4
NameError: name 't4' is not defined
'''


class Root:
    __total = 0


    def __init__(self,v):    # 构造方法
        self.__value = v
        Root.__total += 1


    def show(self):
        print('self.__value:',self.__value)
        print('Root.__total:', Root.__total)


    @classmethod                # 修饰器，声明类方法
    def classShowTotal(cls):    # 类方法
        print(cls.__total)


    @staticmethod               # 修饰器。声明静态方法
    def staticShowTotal():      #静态方法
        print(Root.__total)


r = Root(3)
r.classShowTotal()
r.staticShowTotal()
r.show()
# Root.show()     # 类名无法直接调用实例方法
'''
Traceback (most recent call last):
  File "E:\pythonProject\Test\Class_Test\chapter6.py", line 108, in <module>
    Root.show()
TypeError: Root.show() missing 1 required positional argument: 'self'
'''
Root.show(r)    # 但是可以通过这种方法来调用方法并访问实例成员

# 抽象方法一般在抽象类中定义，并且要求在派生类中必须重新实现，否则不允许派生类创建实例。
import abc
class Foo(metaclass=abc.ABCMeta):   # 抽象类
    def f1(self):
        print(123)
    def f2(self):
        print(456)
    @abc.abstractmethod     # 抽象方法
    def f3(self):
        raise Exception('You musr reimplement this method.')
class Bar(Foo):
    def f3(self):
        print(2546165)
b = Bar()
b.f3()

'''
在Python中比较特殊的是，可以动态地为自定义类和对象增加或删除成员，
这一点是和很多面向对象程序设计语言不同的，也是Python动态类型特点的一种重要体现
class Car:
    price = 100000                     #定义类属性
    def __init__(self, c):
        self.color = c                 #定义实例属性

car1 = Car("Red")                      #实例化对象
car2 = Car("Blue")
print(car1.color, Car.price)           #查看实例属性和类属性的值
Car.price = 110000                     #修改类属性
Car.name = 'QQ'                        #动态增加类属性
car1.color = "Yellow"                  #修改实例属性
print(car2.color, Car.price, Car.name)
print(car1.color, Car.price, Car.name)


import types
def setSpeed(self, s): 
    self.speed = s
car1.setSpeed = types.MethodType(setSpeed, car1) #动态增加成员方法
car1.setSpeed(50)                                #调用成员方法
print(car1.speed)

>>> zhang = Person('zhang')
>>> zhang.sing()                               #用户不具有该行为
AttributeError: 'Person' object has no attribute 'sing'
>>> zhang.sing = types.MethodType(sing, zhang) #动态增加一个新行为
>>> zhang.sing()
zhang can sing.
>>> zhang.walk()
AttributeError: 'Person' object has no attribute 'walk'
>>> zhang.walk = types.MethodType(walk, zhang)
>>> zhang.walk()
zhang can walk.
>>> del zhang.walk                             #删除用户行为
>>> zhang.walk()
AttributeError: 'Person' object has no attribute 'walk'


'''

'''
封装、继承、多态是面向对象程序设计的三大要素

类的封装有两层含义，一个是对数据的封装，一个是对实现逻辑即方法的封装。
class MyClass(object):
    def __init__(self,data1,data2):
        self.__data1=data1
        self.data2=data2    
        
class1=MyClass('first_data','sencond_data')
print(class1.data2)

类MyClass的实例化对象class1就具有了两个属性，分别是data1和data2，
data1是私有属性，只能在类内使用，data2是公有属性，可以在类外使用。
data1和data2就是对数据（属性）的封装。

继承是用来实现代码复用和设计复用的机制，是面向对象程序设计的重要特性之一。设计一个新类时，如果可以继承一个已有的设计良好的类然后进行二次开发，无疑会大幅度减少开发工作量。
在继承关系中，已有的、设计好的类称为父类或基类，新设计的类称为子类或派生类。派生类可以继承父类的公有成员，但是不能继承其私有成员。如果需要在派生类中调用基类的方法，可以使用内置函数super()或者通过“基类名.方法名()”的方式来实现这一目的。
Python支持多继承，如果父类中有相同的方法名，而在子类中使用时没有指定父类名，则Python解释器将从左向右按顺序进行搜索。

所谓多态（polymorphism），是指基类的同一个方法在不同派生类对象中具有不同的表现和行为。派生类继承了基类行为和属性之后，还会增加某些特定的行为和属性，同时还可能会对继承来的某些行为进行一定的改变，这都是多态的表现形式。
Python大多数运算符可以作用于多种不同类型的操作数，并且对于不同类型的操作数往往有不同的表现，这本身就是多态，是通过特殊方法与运算符重载实现的。
>>> class Animal(object):      #定义基类
    def show(self):
        print('I am an animal.')
>>> class Cat(Animal):         #派生类，覆盖了基类的show()方法
    def show(self):
        print('I am a cat.')
>>> class Dog(Animal):         #派生类
    def show(self):
        print('I am a dog.')
>>> class Tiger(Animal):       #派生类
    def show(self):
        print('I am a tiger.')
>>> class Test(Animal):        #派生类，没有覆盖基类的show()方法
    pass
>>> x = [item() for item in (Animal, Cat, Dog, Tiger, Test)]
>>> for item in x:        #遍历基类和派生类对象并调用show()方法
    item.show()

I am an animal.
I am a cat.
I am a dog.
I am a tiger.
I am an animal.
'''






















