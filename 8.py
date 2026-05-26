import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

"""
======================================================
Python 第八课：异常处理 (try / except)
======================================================
"""

# ============================================
# 一、什么是异常？
# ============================================
print("=== 常见异常类型 ===")
print(f"{'异常':<20} {'说明'}")
print("-" * 45)
print(f"{'ZeroDivisionError':<20} {'除以0'}")
print(f"{'TypeError':<20} {'类型错误'}")
print(f"{'ValueError':<20} {'值错误'}")
print(f"{'IndexError':<20} {'索引越界'}")
print(f"{'KeyError':<20} {'字典键不存在'}")
print(f"{'FileNotFoundError':<20} {'文件不存在'}")
print(f"{'AttributeError':<20} {'属性不存在'}")

# ============================================
# 二、try-except 基本用法
# ============================================
print("\n=== try-except ===")

try:
    result = 10 / 0       # 这行会出错
    print(result)
except ZeroDivisionError:
    print("错误：不能除以0！")

print("程序继续运行...")   # 不会崩溃！

# ============================================
# 三、捕获多种异常
# ============================================
print("\n=== 多种异常 ===")

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "错误：除数不能为0"
    except TypeError:
        return "错误：请输入数字"

print(f"10/2 = {safe_divide(10, 2)}")
print(f"10/0 = {safe_divide(10, 0)}")
print(f"'a'/2 = {safe_divide('a', 2)}")

# 捕获所有异常（不推荐，但有时需要）
try:
    x = int("abc")
except Exception as e:
    print(f"捕获异常: {type(e).__name__}: {e}")

# ============================================
# 四、try-except-else-finally
# ============================================
print("\n=== else 和 finally ===")

def read_file_safe(filename):
    try:
        f = open(filename, "r", encoding="utf-8")
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
    else:
        # try 没出错才执行
        content = f.read()
        print(f"文件内容: {content.strip()}")
        f.close()
    finally:
        # 无论是否出错，都会执行
        print("（finally: 清理工作完成）")

read_file_safe("存在.txt")      # 不存在
read_file_safe("test.txt")      # 上一课创建的，应该存在

# ============================================
# 五、raise 手动抛出异常
# ============================================
print("\n=== raise 抛出异常 ===")

def set_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数！")
    if age > 150:
        raise ValueError("年龄不能超过150！")
    print(f"年龄设置为: {age}")

try:
    set_age(25)
    set_age(-5)
except ValueError as e:
    print(f"捕获到: {e}")

# ============================================
# 六、自定义异常
# ============================================
print("\n=== 自定义异常 ===")

class ScoreError(Exception):
    """自定义分数异常"""
    pass

def check_score(score):
    if score < 0 or score > 100:
        raise ScoreError(f"分数 {score} 不在0-100范围内")
    print(f"分数 {score} 有效")

try:
    check_score(85)
    check_score(150)
except ScoreError as e:
    print(f"成绩异常: {e}")

# ============================================
# 七、实战：安全的用户输入
# ============================================
print("\n=== 实战：安全输入 ===")

def get_number(prompt="请输入数字"):
    """不停地让用户输入，直到输入有效数字"""
    while True:
        try:
            user_input = input(prompt + ": ")
            return float(user_input)
        except ValueError:
            print("  输入无效，请输入一个数字！")
        except KeyboardInterrupt:
            print("\n  用户取消输入")
            return None

# 取消注释来体验：
# num = get_number("请输入一个数字")
# print(f"你输入的是: {num}")

print("（安全输入函数已定义，取消注释可体验）")

# ============================================
# 八、with 语句 + 异常处理
# ============================================
print("\n=== with + 异常处理 ===")

try:
    with open("不存在的文件.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("文件不存在，但 with 语句仍然会自动处理资源")
except PermissionError:
    print("没有权限读取该文件")

print("\n第八课结束！异常处理让程序更健壮~")
