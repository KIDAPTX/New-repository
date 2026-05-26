import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

"""
======================================================
Python 第九课：面向对象编程 (OOP)
======================================================
"""

# ============================================
# 一、类与对象（基本概念）
# ============================================
print("=== 类与对象 ===")

# 定义类（蓝图）
class Dog:
    """狗类"""

    # __init__ 是构造函数，创建对象时自动调用
    def __init__(self, name, age):
        self.name = name    # self.name 是实例属性
        self.age = age

    # 方法（类里面的函数）
    def bark(self):
        print(f"{self.name}：汪汪！")

    def introduce(self):
        print(f"我叫{self.name}，今年{self.age}岁")

# 创建对象（实例化）
dog1 = Dog("旺财", 3)
dog2 = Dog("来福", 1)

dog1.introduce()
dog1.bark()
dog2.introduce()

# ============================================
# 二、self 是什么？
# ============================================
print("\n=== self 的奥秘 ===")

# self 代表调用这个方法的对象本身
# dog1.bark() 等价于 Dog.bark(dog1)

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self, other):
        print(f"{self.name} 对 {other.name} 说：你好！")

p1 = Person("小明")
p2 = Person("小红")
p1.say_hello(p2)

# ============================================
# 三、类属性 vs 实例属性
# ============================================
print("\n=== 类属性 vs 实例属性 ===")

class Student:
    school = "第一中学"      # 类属性，所有对象共享

    def __init__(self, name, score):
        self.name = name     # 实例属性，每个对象独有
        self.score = score

s1 = Student("小明", 90)
s2 = Student("小红", 95)

print(f"s1: {s1.name}, {s1.school}, {s1.score}")
print(f"s2: {s2.name}, {s2.school}, {s2.score}")

# 修改类属性，所有对象都受影响
Student.school = "第二中学"
print(f"修改后 s1: {s1.school}, s2: {s2.school}")

# ============================================
# 四、继承（复用代码）
# ============================================
print("\n=== 继承 ===")

# 父类（基类）
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} 在吃东西")

# 子类（派生类）
class Cat(Animal):           # Cat 继承 Animal
    def meow(self):
        print(f"{self.name}：喵喵！")

    # 重写父类方法
    def eat(self):
        print(f"{self.name} 在优雅地吃鱼")

class Bird(Animal):
    def fly(self):
        print(f"{self.name} 在飞")

    def eat(self):
        super().eat()        # 调用父类的方法
        print(f"{self.name} 吃完了虫子")

cat = Cat("小花")
cat.eat()                    # 调用重写后的方法
cat.meow()

bird = Bird("小飞")
bird.eat()                   # 先调父类，再调自己的
bird.fly()

# ============================================
# 五、私有属性和方法
# ============================================
print("\n=== 私有成员 ===")

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance     # 双下划线开头 = 私有

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"存入 {amount}，余额: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"取出 {amount}，余额: {self.__balance}")
        else:
            print("余额不足")

    def get_balance(self):           # 通过公开方法访问私有属性
        return self.__balance

account = BankAccount("小明", 1000)
account.deposit(500)
account.withdraw(200)
print(f"当前余额: {account.get_balance()}")
# print(account.__balance)           # 报错！不能直接访问私有属性

# ============================================
# 六、特殊方法（魔术方法）
# ============================================
print("\n=== 特殊方法 ===")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):               # 打印时调用
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):              # 调试时调用
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):        # + 运算符
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):         # == 运算符
        return self.x == other.x and self.y == other.y

    def __len__(self):               # len() 函数
        return 2

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2                        # 自动调用 __add__
print(f"{v1} + {v2} = {v3}")
print(f"v1 == v2? {v1 == v2}")
print(f"len(v1) = {len(v1)}")

# ============================================
# 七、@property 装饰器（优雅的 getter/setter）
# ============================================
print("\n=== @property ===")

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):                # getter
        return self._radius

    @radius.setter
    def radius(self, value):         # setter
        if value <= 0:
            raise ValueError("半径必须大于0")
        self._radius = value

    @property
    def area(self):                  # 计算属性
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(f"半径: {c.radius}, 面积: {c.area:.2f}")
c.radius = 10                        # 就像直接赋值一样
print(f"修改后 半径: {c.radius}, 面积: {c.area:.2f}")

print("\n第九课结束！面向对象是大型项目的基石~")
