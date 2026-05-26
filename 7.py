import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

"""
======================================================
Python 第七课：文件操作
======================================================
"""

# ============================================
# 一、写入文件 write
# ============================================
print("=== 写入文件 ===")

# "w" 模式：写入（会覆盖原内容）
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("第一行：Hello Python\n")
    f.write("第二行：文件操作很简单\n")
    f.write("第三行：记得关文件哦\n")

print("已写入 test.txt")

# ============================================
# 二、读取文件 read
# ============================================
print("\n=== 读取文件 ===")

# read()：一次性读取全部
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(f"read()全部内容:\n{content}")

# readlines()：按行读取，返回列表
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"readlines()按行: {lines}")

# readline()：一次读一行
with open("test.txt", "r", encoding="utf-8") as f:
    print("逐行读取:")
    line = f.readline()
    while line:
        print(f"  {line.strip()}")
        line = f.readline()

# 最常用的逐行遍历方式
print("\nfor 循环逐行读取:")
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"  {line.strip()}")

# ============================================
# 三、文件操作模式
# ============================================
print("\n=== 文件模式 ===")
print(f"{'模式':<6} {'说明'}")
print("-" * 30)
print(f"{'r':<6} {'只读（文件必须存在）'}")
print(f"{'w':<6} {'写入（覆盖原有内容）'}")
print(f"{'a':<6} {'追加（在末尾添加）'}")
print(f"{'r+':<6} {'读写（文件必须存在）'}")
print(f"{'x':<6} {'新建写入（文件已存在则报错）'}")

# 追加模式演示
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("第四行：这是追加的内容\n")

print("已追加内容到 test.txt")

# ============================================
# 四、with 语句（自动关闭文件）
# ============================================
print("\n=== with 语句 ===")

# with 语句会自动调用 f.close()，即使发生异常也会关闭
# 强烈推荐始终使用 with！

# 同时操作多个文件
with open("test.txt", "r", encoding="utf-8") as src:
    with open("copy.txt", "w", encoding="utf-8") as dst:
        dst.write(src.read())

print("已复制 test.txt → copy.txt")

# ============================================
# 五、判断文件是否存在
# ============================================
import os

print("\n=== 文件路径操作 ===")

print(f"当前目录: {os.getcwd()}")
print(f"test.txt 存在吗？{os.path.exists('test.txt')}")
print(f"这是一个文件夹吗？{os.path.isdir('test.txt')}")
print(f"文件名部分: {os.path.basename('d:/path/to/file.txt')}")

# ============================================
# 六、综合练习：笔记本程序
# ============================================

print("\n=== 综合练习（模拟） ===")

def save_note(filename, content):
    """保存笔记"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"笔记已保存到 {filename}")

def read_note(filename):
    """读取笔记"""
    if not os.path.exists(filename):
        return "文件不存在"
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def append_note(filename, content):
    """追加笔记"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(content + "\n")
    print(f"已追加到 {filename}")

# 模拟操作
save_note("mynote.txt", "今天学了Python文件操作\n感觉很有用！")
print(f"读取笔记:\n{read_note('mynote.txt')}")
append_note("mynote.txt", "明天继续学异常处理")
print(f"读取笔记:\n{read_note('mynote.txt')}")

# 清理测试文件（可选）
# os.remove("test.txt")
# os.remove("copy.txt")
# os.remove("mynote.txt")

print("\n第七课结束！文件操作是持久化数据的基础~")
