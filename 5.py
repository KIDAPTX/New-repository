import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

"""
======================================================
Python 第五课：列表、元组、字典、集合
======================================================
"""

# ============================================
# 一、列表 (list) —— 最常用的数据结构
# ============================================
print("=== 列表 (list) ===")

# 创建列表
fruits = ["苹果", "香蕉", "橘子"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "你好", 3.14, True]  # 可以混合类型

print(f"水果列表: {fruits}")
print(f"长度: {len(fruits)}")

# --- 增 ---
fruits.append("葡萄")        # 追加到末尾
print(f"append后: {fruits}")

fruits.insert(1, "西瓜")     # 在索引1位置插入
print(f"insert后: {fruits}")

# --- 删 ---
fruits.remove("香蕉")        # 按值删除
print(f"remove后: {fruits}")

popped = fruits.pop()        # 弹出最后一个，返回它
print(f"pop了'{popped}', 剩余: {fruits}")

del fruits[0]                # 按索引删除
print(f"del索引0后: {fruits}")

# --- 改 ---
fruits = ["苹果", "香蕉", "橘子"]
fruits[1] = "芒果"           # 直接赋值修改
print(f"修改后: {fruits}")

# --- 查 ---
print(f"fruits[0]: {fruits[0]}")
print(f"fruits[-1]: {fruits[-1]}")
print(f"fruits[0:2]: {fruits[0:2]}")  # 切片

# --- 常用方法 ---
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()                  # 原地排序
print(f"排序: {nums}")

nums.sort(reverse=True)      # 降序
print(f"降序: {nums}")

print(f"最大值: {max(nums)}, 最小值: {min(nums)}, 求和: {sum(nums)}")
print(f"1出现了{list(nums).count(1)}次")

# 列表推导式（很常用！）
squares = [x**2 for x in range(1, 6)]
print(f"列表推导式 1-5的平方: {squares}")

even = [x for x in range(1, 11) if x % 2 == 0]
print(f"1-10中的偶数: {even}")

# ============================================
# 二、元组 (tuple) —— 不可变的列表
# ============================================
print("\n=== 元组 (tuple) ===")

point = (3, 4)               # 用小括号
rgb = (255, 128, 0)

print(f"坐标: {point}, x={point[0]}, y={point[1]}")
print(f"颜色: {rgb}")

# point[0] = 5               # 报错！元组不能修改

# 元组解包
x, y = point
print(f"解包: x={x}, y={y}")

# 单个元素的元组（注意逗号！）
single = (42,)                # 必须加逗号
print(f"单元素元组: {single}, 类型: {type(single)}")

# ============================================
# 三、字典 (dict) —— 键值对，像查字典一样
# ============================================
print("\n=== 字典 (dict) ===")

# 创建字典
student = {
    "name": "小明",
    "age": 20,
    "score": 95
}
print(f"学生信息: {student}")

# --- 查 ---
print(f"姓名: {student['name']}")
print(f"年龄: {student.get('age')}")
print(f"不存在的键: {student.get('height', '未填写')}")  # 安全取值

# --- 增 / 改 ---
student["height"] = 1.75     # 新增键
student["score"] = 98        # 修改已有的键
print(f"更新后: {student}")

# --- 删 ---
del student["age"]
print(f"删除age后: {student}")

# --- 遍历 ---
print("\n遍历字典:")
for key, value in student.items():
    print(f"  {key}: {value}")

print("\n遍历键:")
for key in student.keys():
    print(f"  {key}", end=" ")
print()

print("遍历值:")
for value in student.values():
    print(f"  {value}", end=" ")
print()

# 字典推导式
word = "hello"
char_count = {c: word.count(c) for c in word}
print(f"\n字符计数: {char_count}")

# ============================================
# 四、集合 (set) —— 无序、不重复
# ============================================
print("\n=== 集合 (set) ===")

# 创建集合
numbers = {1, 2, 3, 3, 2, 1}     # 自动去重
print(f"集合自动去重: {numbers}")

chars = set("hello world")        # 字符串转集合
print(f"字符串去重: {chars}")

# --- 集合运算 ---
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"\na = {a}")
print(f"b = {b}")
print(f"交集 a & b : {a & b}")       # 共同的
print(f"并集 a | b : {a | b}")       # 全部（去重）
print(f"差集 a - b : {a - b}")       # a有b没有
print(f"对称差 a ^ b : {a ^ b}")     # 只在一边的

# --- 增删 ---
s = {1, 2, 3}
s.add(4)
print(f"\nadd后: {s}")
s.remove(2)
print(f"remove后: {s}")

# 快速去重（列表→集合→列表）
dup_list = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(dup_list))
print(f"\n列表去重: {dup_list} → {unique}")

# ============================================
# 五、四种数据结构对比
# ============================================
print("\n=== 四种数据结构对比 ===")
print(f"{'类型':<6} {'有序':<6} {'可改':<6} {'可重复':<8} {'符号':<10} {'场景'}")
print("-" * 50)
print(f"{'列表':<6} {'是':<6} {'是':<6} {'是':<8} {'[ ]':<10} {'存储有序数据'}")
print(f"{'元组':<6} {'是':<6} {'否':<6} {'是':<8} {'( )':<10} {'不可变数据（坐标等）'}")
print(f"{'字典':<6} {'是*':<6} {'是':<6} {'键不重复':<8} {'{k:v}':<10} {'键值对（配置、缓存）'}")
print(f"{'集合':<6} {'否':<6} {'是':<6} {'否':<8} {'{ }':<10} {'去重、集合运算'}")

print("\n第五课结束！四种数据结构是编程的基石~")
