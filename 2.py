import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

"""
======================================================
Python 第二课：字符串操作与输入输出
======================================================
"""

# ============================================
# 一、字符串拼接
# ============================================
first_name = "张"
last_name = "三"

# 方法1：用 + 号拼接
full_name = first_name + last_name
print("用 + 拼接:", full_name)

# 方法2：用逗号拼接（print 会自动加空格）
print("用逗号拼接:", first_name, last_name)

# 方法3：字符串乘法（重复）
line = "-" * 20  # 重复 20 次
print(line)

# ============================================
# 二、f-string 格式化（最常用！）
# ============================================
name = "小明"
age = 25
height = 1.75

# f 开头，变量用 { } 包起来
print(f"我叫{name}，今年{age}岁，身高{height}米")

# 可以放表达式
print(f"明年我就{age + 1}岁了")
print(f"身高保留一位小数：{height:.1f}")

# ============================================
# 三、字符串常用方法
# ============================================
text = "  Hello Python  "

print("原始:", repr(text))           # repr() 可以看到空格
print("去两边空格:", text.strip())    # 去掉首尾空格
print("全大写:", text.upper())        # HELLO PYTHON
print("全小写:", text.lower())        # hello python
print("替换:", text.replace("Python", "World"))  # 替换文字

# 判断开头结尾
filename = "photo.jpg"
print(f"是图片吗？{filename.endswith('.jpg')}")   # True
print(f"以 photo 开头吗？{filename.startswith('photo')}")  # True

# 查找和计数
sentence = "我爱Python，Python很有趣"
print(f"'Python'出现次数: {sentence.count('Python')}")   # 2
print(f"'Python'首次出现位置: {sentence.find('Python')}")  # 2（索引从0开始）

# ============================================
# 四、字符串索引和切片
# ============================================
word = "Hello Python"

# 索引（从 0 开始）
print(f"第0个字符: {word[0]}")   # H
print(f"第6个字符: {word[6]}")   # P
print(f"最后一个字符: {word[-1]}")  # n（负数从右边数）

# 切片 [开始:结束:步长]（包左不包右）
print(f"前5个字符: {word[0:5]}")     # Hello
print(f"第6到结尾: {word[6:]}")      # Python
print(f"倒数6个: {word[-6:]}")       # Python
print(f"每隔一个取: {word[::2]}")    # HloPto

# ============================================
# 五、用户输入 input()
# ============================================
# input() 会让程序停下来，等待用户输入

# 先注释掉，避免自动运行卡住。你可以取消注释试试！
# your_name = input("请输入你的名字：")
# print(f"你好，{your_name}！")

# 注意：input() 返回的永远是字符串！
# age_input = input("请输入年龄：")
# print(f"你输入的类型是：{type(age_input)}")  # <class 'str'>
# 如果要做数学运算，需要用 int() 或 float() 转换

# ============================================
# 六、类型转换
# ============================================
print("\n--- 类型转换 ---")
# 字符串 → 数字
num_str = "123"
num_int = int(num_str)      # "123" → 123
num_float = float("3.14")   # "3.14" → 3.14
print(f"int 转换: {num_int}, 类型: {type(num_int)}")
print(f"float 转换: {num_float}, 类型: {type(num_float)}")

# 数字 → 字符串
num = 100
num_to_str = str(num)
print(f"str 转换: {num_to_str}, 类型: {type(num_to_str)}")

# ============================================
# 七、split() 分割字符串
# ============================================
fruits = "苹果,香蕉,橘子,葡萄"
fruit_list = fruits.split(",")  # 按逗号分割
print(f"分割结果: {fruit_list}")

# join() 合并字符串
joined = " | ".join(fruit_list)
print(f"合并结果: {joined}")

print("\n第二课结束！试试取消 input() 的注释，体验交互程序~")
