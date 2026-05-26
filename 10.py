import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

"""
======================================================
Python 第十课：小项目实战 —— 通讯录管理系统
======================================================
融合前9课的知识：变量、字符串、条件、循环、
列表字典、函数、文件操作、异常处理、面向对象
"""

import os

# ============================================
# 一、定义联系人数据模型
# ============================================

class Contact:
    """联系人类"""
    def __init__(self, name, phone, email="", address=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name:<8} {self.phone:<15} {self.email:<20} {self.address}"

    def to_dict(self):
        """转为字典（方便保存）"""
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }

    @classmethod
    def from_dict(cls, data):
        """从字典创建联系人"""
        return cls(data["name"], data["phone"],
                   data.get("email", ""), data.get("address", ""))

# ============================================
# 二、定义通讯录管理器
# ============================================

class AddressBook:
    """通讯录管理类"""
    def __init__(self, filename="contacts.txt"):
        self.filename = filename
        self.contacts = []     # 存储所有联系人
        self.load()

    def add(self, contact):
        """添加联系人"""
        self.contacts.append(contact)
        print(f"已添加联系人: {contact.name}")

    def delete(self, name):
        """删除联系人"""
        for i, c in enumerate(self.contacts):
            if c.name == name:
                del self.contacts[i]
                print(f"已删除联系人: {name}")
                return True
        print(f"未找到联系人: {name}")
        return False

    def search(self, keyword):
        """搜索联系人（按姓名或电话）"""
        results = []
        for c in self.contacts:
            if keyword in c.name or keyword in c.phone:
                results.append(c)
        return results

    def list_all(self):
        """列出所有联系人"""
        if not self.contacts:
            print("通讯录为空")
            return
        print(f"{'姓名':<8} {'电话':<15} {'邮箱':<20} {'地址'}")
        print("-" * 60)
        for c in self.contacts:
            print(c)
        print(f"\n共 {len(self.contacts)} 个联系人")

    def save(self):
        """保存到文件"""
        data = [c.to_dict() for c in self.contacts]
        with open(self.filename, "w", encoding="utf-8") as f:
            import json
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"已保存 {len(self.contacts)} 个联系人到 {self.filename}")

    def load(self):
        """从文件加载"""
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                import json
                data = json.load(f)
                self.contacts = [Contact.from_dict(d) for d in data]
            print(f"已加载 {len(self.contacts)} 个联系人")
        except Exception as e:
            print(f"加载失败: {e}")

# ============================================
# 三、交互式菜单
# ============================================

def show_menu():
    """显示菜单"""
    print("\n" + "=" * 40)
    print("        通讯录管理系统")
    print("=" * 40)
    print("  1. 添加联系人")
    print("  2. 查看所有联系人")
    print("  3. 搜索联系人")
    print("  4. 删除联系人")
    print("  5. 保存")
    print("  0. 退出")
    print("-" * 40)

def get_input(prompt, allow_empty=False):
    """安全获取用户输入"""
    while True:
        try:
            value = input(prompt).strip()
            if not allow_empty and not value:
                print("输入不能为空，请重新输入")
                continue
            return value
        except KeyboardInterrupt:
            print("\n")
            return None
        except EOFError:
            return None

def main():
    """主程序"""
    book = AddressBook()

    while True:
        show_menu()
        choice = get_input("请选择操作 (0-5): ")

        if choice is None or choice == "0":
            book.save()
            print("再见！")
            break

        elif choice == "1":
            print("\n--- 添加联系人 ---")
            name = get_input("姓名: ")
            if name is None: continue
            phone = get_input("电话: ")
            if phone is None: continue
            email = get_input("邮箱 (可选): ", allow_empty=True) or ""
            address = get_input("地址 (可选): ", allow_empty=True) or ""

            book.add(Contact(name, phone, email, address))

        elif choice == "2":
            print("\n--- 所有联系人 ---")
            book.list_all()

        elif choice == "3":
            keyword = get_input("\n请输入搜索关键词: ")
            if keyword is None: continue
            results = book.search(keyword)
            if results:
                print(f"\n找到 {len(results)} 个联系人:")
                print(f"{'姓名':<8} {'电话':<15} {'邮箱':<20} {'地址'}")
                print("-" * 60)
                for c in results:
                    print(c)
            else:
                print(f"未找到与 '{keyword}' 相关的联系人")

        elif choice == "4":
            name = get_input("\n请输入要删除的联系人姓名: ")
            if name is None: continue
            confirm = get_input(f"确认删除 {name}? (y/n): ")
            if confirm and confirm.lower() == "y":
                book.delete(name)
            else:
                print("已取消")

        elif choice == "5":
            book.save()

        else:
            print("无效的选择，请重试")

# ============================================
# 快速演示（自动运行，无需手动输入）
# ============================================

def demo():
    """演示模式：展示核心功能"""
    print("\n" + "=" * 50)
    print("    【演示模式】自动展示通讯录功能")
    print("=" * 50)

    book = AddressBook("demo_contacts.txt")

    # 添加几个联系人
    print("\n1. 添加联系人:")
    book.add(Contact("张三", "13800138001", "zhangsan@qq.com", "北京"))
    book.add(Contact("李四", "13900139002", "lisi@163.com", "上海"))
    book.add(Contact("王五", "13700137003", "wangwu@gmail.com", "广州"))

    # 查看所有
    print("\n2. 查看所有联系人:")
    book.list_all()

    # 搜索
    print("\n3. 搜索 '李四':")
    results = book.search("李四")
    for c in results:
        print(f"  {c}")

    # 删除
    print("\n4. 删除 '王五':")
    book.delete("王五")
    book.list_all()

    # 保存
    print("\n5. 保存到文件:")
    book.save()

    # 重新加载
    print("\n6. 重新加载验证:")
    book2 = AddressBook("demo_contacts.txt")
    book2.list_all()

    print("\n演示结束！取消下方 main() 的注释体验交互模式~")

# 先运行演示模式
demo()

# 想要交互式体验？注释掉上面的 demo()，取消下面这行的注释：
# main()

print("\n第十课结束！🎉 10节课全部完成，你已经入门Python了！")
