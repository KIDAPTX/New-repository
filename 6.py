import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

"""
======================================================
Python 第六课：函数 (def)
======================================================
"""

# ============================================
# 一、定义和调用函数
# ============================================
print("=== 定义函数 ===")

def greet():
    """这是一个简单的问候函数"""
    print("你好，欢迎学习函数！")

greet()  # 调用函数
greet()  # 可以多次调用

# ============================================
# 二、参数（让函数变灵活）
# ============================================
print("\n=== 参数 ===")

# 位置参数
def greet_person(name):
    print(f"你好，{name}！")

greet_person("小明")
greet_person("小红")

# 多个参数
def add(a, b):
    print(f"{a} + {b} = {a + b}")

add(3, 5)
add(10, 20)

# 默认参数（有默认值的参数放后面）
def introduce(name, city="北京"):
    print(f"我叫{name}，来自{city}")

introduce("小明")              # 不传 city，用默认值
introduce("小红", "上海")      # 传了 city，覆盖默认值

# 关键字参数（不按顺序传参）
introduce(city="广州", name="小刚")

# ============================================
# 三、返回值 return
# ============================================
print("\n=== 返回值 ===")

def square(n):
    return n * n               # 把结果返回给调用者

result = square(5)
print(f"5的平方是: {result}")
print(f"7的平方是: {square(7)}")  # 直接使用返回值

# 返回多个值（实际返回的是元组）
def get_user_info():
    name = "小明"
    age = 20
    return name, age

n, a = get_user_info()         # 解包接收
print(f"姓名: {n}, 年龄: {a}")

# 提前返回
def check_age(age):
    if age < 0:
        return "年龄不能为负数"    # 遇到 return 函数立刻结束
    if age >= 18:
        return "已成年"
    return "未成年"               # 前面的条件都不满足才到这

print(f"25岁: {check_age(25)}")
print(f"12岁: {check_age(12)}")
print(f"-5岁: {check_age(-5)}")

# ============================================
# 四、*args 和 **kwargs（可变参数）
# ============================================
print("\n=== 可变参数 ===")

# *args：接收任意个位置参数，打包成元组
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(f"求和 1,2,3: {sum_all(1, 2, 3)}")
print(f"求和 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")

# **kwargs：接收任意个关键字参数，打包成字典
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("学生信息:")
print_info(name="小明", age=20, score=95)

# ============================================
# 五、作用域（局部变量 vs 全局变量）
# ============================================
print("\n=== 作用域 ===")

total = 100  # 全局变量

def show():
    local_var = 50  # 局部变量，只在函数内部有效
    print(f"函数内可访问全局变量 total={total}")
    print(f"局部变量 local_var={local_var}")

show()
# print(local_var)  # 报错！局部变量不能在函数外访问

# 修改全局变量
def modify_global():
    global total         # 声明要修改全局变量
    total = 999

modify_global()
print(f"修改后的全局 total: {total}")

# ============================================
# 六、lambda 匿名函数（一行函数）
# ============================================
print("\n=== lambda 函数 ===")

# 普通函数
def double(x):
    return x * 2

# lambda 等价写法：lambda 参数: 返回值
double_lambda = lambda x: x * 2

print(f"普通函数: {double(5)}")
print(f"lambda: {double_lambda(5)}")

# lambda 常用于 sorted/map/filter
students = [
    {"name": "小明", "score": 85},
    {"name": "小红", "score": 92},
    {"name": "小刚", "score": 78},
]

# 按分数排序
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print(f"按分数排名: {sorted_students}")

# map：对每个元素应用函数
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print(f"map 平方: {squared}")

# filter：筛选符合条件的元素
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"filter 偶数: {evens}")

# ============================================
# 七、类型提示（Python 3.5+ 推荐写法）
# ============================================
print("\n=== 类型提示 ===")

def add_typed(a: int, b: int) -> int:
    """带类型提示的加法函数"""
    return a + b

print(f"add_typed(3, 5) = {add_typed(3, 5)}")
# 类型提示只是提示，不强制检查，传字符串也能运行

# ============================================
# 八、综合练习：简易计算器
# ============================================
print("\n=== 综合练习：简易计算器 ===")

def calculator(a, b, operator):
    """简易计算器"""
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "错误：不能除以0"
        return a / b
    else:
        return "不支持的运算符"

print(f"10 + 5 = {calculator(10, 5, '+')}")
print(f"10 - 5 = {calculator(10, 5, '-')}")
print(f"10 * 5 = {calculator(10, 5, '*')}")
print(f"10 / 5 = {calculator(10, 5, '/')}")
print(f"10 / 0 = {calculator(10, 0, '/')}")

print("\n第六课结束！函数让代码可以复用，是编程的核心~")
