import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

"""
======================================================
Python 第三课：条件判断 (if / elif / else)
======================================================
"""

# ============================================
# 一、比较运算符
# ============================================
print("--- 比较运算符 ---")
a = 10
b = 5

print(f"a = {a}, b = {b}")
print(f"a == b : {a == b}")   # 等于
print(f"a != b : {a != b}")   # 不等于
print(f"a > b  : {a > b}")    # 大于
print(f"a < b  : {a < b}")    # 小于
print(f"a >= b : {a >= b}")   # 大于等于
print(f"a <= b : {a <= b}")   # 小于等于

# ============================================
# 二、if 语句（单一条件）
# ============================================
print("\n--- if 语句 ---")

score = 85

if score >= 60:
    print(f"你的分数是{score}，及格了！")
    # 注意：if 里面的代码要缩进（Tab 或 4个空格）

# ============================================
# 三、if-else 语句（二选一）
# ============================================
print("\n--- if-else 语句 ---")

age = 16

if age >= 18:
    print("你已经成年了，可以进网吧")
else:
    print("你还未成年，不能进网吧")

# ============================================
# 四、if-elif-else 语句（多选一）
# ============================================
print("\n--- if-elif-else 语句 ---")

score = 78

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F（不及格）"

print(f"分数：{score}，等级：{grade}")

# ============================================
# 五、逻辑运算符 (and / or / not)
# ============================================
print("\n--- 逻辑运算符 ---")

# and：所有条件都成立才为 True
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("可以入场看电影")
else:
    print("不能入场")

# or：任一条件成立就为 True
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("今天是休息日，不用上班！")
else:
    print("今天要上班...")

# not：取反
is_raining = False

if not is_raining:
    print("没下雨，可以出门玩")
else:
    print("下雨了，带把伞吧")

# ============================================
# 六、in 关键字（判断是否包含）
# ============================================
print("\n--- in 关键字 ---")

languages = ["Python", "Java", "C++", "JavaScript"]

if "Python" in languages:
    print("列表中有 Python！")

# 也适用于字符串
email = "hello@gmail.com"
if "@" in email:
    print("这是一个有效的邮箱地址")

# ============================================
# 七、三目表达式（一行写法）
# ============================================
print("\n--- 三目表达式 ---")

age = 20
# 语法：值1 if 条件 else 值2
status = "成年" if age >= 18 else "未成年"
print(f"年龄 {age}，状态：{status}")

# ============================================
# 八、综合练习：简易登录判断
# ============================================
print("\n--- 综合练习 ---")

# 预设的用户名和密码
correct_username = "admin"
correct_password = "123456"

# 取消下面的注释来体验交互程序：
# username = input("请输入用户名：")
# password = input("请输入密码：")
#
# if username == correct_username and password == correct_password:
#     print("登录成功！欢迎回来！")
# elif username != correct_username:
#     print("用户名错误！")
# else:
#     print("密码错误！")

print("\n第三课结束！试试取消最后的注释，做一个登录程序~")
