### Python中列表推导为什么比for循环快？
1. 解释器级的优化: 列表推导中，python在底层使用C语言的实现来处理迭代操作，会比逐步解释for循环中的每条语句要快。
2. for循环里面每条语句执行，如果涉及到函数调用，每次循环都会耗时。列表推导会把操作优化为一个单一的表达式，减少函数调用。 

实例对比:
```
result = []
for i in range(1000000):
    result.append(i * 2)

```

```
result = [i * 2 for i in range(1000000)]
```

### Python 使用类型注解，方法参数
在 Python 中，类型注解（Type Annotations）是一种静态类型检查工具，它允许我们为变量、函数参数和返回值提供明确的类型提示。这可以提高代码的可读性、可维护性，并帮助静态类型检查工具（如 mypy）检测潜在的类型错误。

```
def function_name(arg1: Type1, arg2: Type2) -> ReturnType:
    pass
```
1. 简单的参数类型注解 
```
def add_numbers(x: int, y: int) -> int:
    return x + y

# 调用
result = add_numbers(3, 5)
print(result)  # 输出: 8

```

2. 使用容器类型（如 list、dict）
```
from typing import List, Dict

def process_items(items: List[int]) -> Dict[str, int]:
    return {"sum": sum(items), "count": len(items)}

# 调用
result = process_items([1, 2, 3])
print(result)  # 输出: {'sum': 6, 'count': 3}

```
3. 可选参数和默认值 
```
from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if name:
        return f"Hello, {name}!"
    return "Hello, Stranger!"

# 调用
print(greet("Alice"))  # 输出: Hello, Alice!
print(greet())         # 输出: Hello, Stranger!

# 参数 name 可以是字符串 (str) 或 None。
# 返回值是字符串 (str)。

```

4. 联合类型（Union）

```
from typing import Union

def square(value: Union[int, float]) -> float:
    return value ** 2

# 调用
print(square(3))     # 输出: 9
print(square(3.5))   # 输出: 12.25

# 参数 value 可以是整数 (int) 或浮点数 (float)。
# 返回值是浮点数 (float)。

```

5. 可变参数（*args 和 **kwargs）

```
from typing import Any

def log_message(*args: str, **kwargs: Any) -> None:
    print("Args:", args)
    print("Kwargs:", kwargs)

# 调用
log_message("Error", "Critical", code=500, description="Server error")

# *args: str 表示可变参数列表中的每个参数都是字符串。
# **kwargs: Any 表示关键字参数的值可以是任意类型。

```

6. 自定义类型
可以使用 typing.NewType 创建自定义类型，或直接引用类。

```
from typing import NewType

UserId = NewType('UserId', int)

def get_user_name(user_id: UserId) -> str:
    # 模拟根据用户 ID 获取用户名
    return f"User_{user_id}"

# 调用
print(get_user_name(UserId(42)))  # 输出: User_42

```

7. 类方法的参数类型
对于类方法和实例方法，self 和 cls 不需要类型注解，但其他参数可以注解。
```
from typing import List

class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_friends(self) -> List[str]:
        return ["Alice", "Bob", "Cathy"]
# name 和 age 参数的类型为字符串和整数。
# get_friends 方法返回一个字符串列表 (List[str])。

```

### FastAPI



### Python 魔法函数
Python 的魔法函数（Magic Methods），又称为双下划线方法（Dunder Methods），是指以双下划线开头和结尾的方法名（如 __init__、__str__）。这些方法使得类的实例可以表现得像内置对象一样，并实现诸如运算符重载、对象自定义行为等功能。

魔法函数让 Python 类的行为更加灵活，能实现运算符重载、容器模拟、上下文管理等功能。使用时需注意：
避免过度复杂的实现，保持代码易读性。
谨慎使用影响全局行为的方法（如 __getattribute__）。


1. 构造与初始化

```
class Person:
    def __new__(cls, *args, **kwargs):
        print("Creating instance")
        return super().__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Initialized {self.name}, {self.age}")

p = Person("Alice", 30)

# __new__(cls, ...): 控制实例的创建，返回一个实例。
# __init__(self, ...): 初始化实例，设置初始属性。

```
2. 字符串表示
控制对象的字符串表示形式。

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 30)
print(str(p))   # Person(name=Alice, age=30)
print(repr(p))  # Person('Alice', 30)

# __str__(self): 为用户提供友好的字符串表示，str() 或 print() 调用。
# __repr__(self): 为开发者提供对象的官方字符串表示，repr() 调用。

```

3. 运算符重载
允许定义类实例在操作符中的行为。

```
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)

# __add__(self, other): +
# __sub__(self, other): -
# __mul__(self, other): *
# __truediv__(self, other): /
# 其他：__floordiv__, __mod__, __pow__, __neg__...

```

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
print(p1 < p2)  # True

# __eq__(self, other): ==
# __ne__(self, other): !=
# __lt__(self, other): <
# __le__(self, other): <=
# __gt__(self, other): >
# __ge__(self, other): >=

```

4. 容器相关
定义对象作为容器（如列表、字典）的行为。

```
class CustomList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

c = CustomList([1, 2, 3])
print(len(c))  # 3
print(c[1])    # 2
c[1] = 5
print(c[1])    # 5

# __len__(self): 返回容器的长度，len() 调用。
# __getitem__(self, key): 获取元素，obj[key] 调用。
# __setitem__(self, key, value): 设置元素，obj[key] = value。
# __delitem__(self, key): 删除元素，del obj[key]。
# __iter__(self): 返回一个迭代器，for 循环调用。
# __contains__(self, item): 判断元素是否存在于容器中，in 操作。

```

5. 属性访问
定义属性访问的行为

```
class Example:
    def __getattr__(self, name):
        return f"{name} is not found!"

    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        self.__dict__[name] = value

e = Example()
print(e.some_attribute)  # some_attribute is not found!
e.new_attribute = 42      # Setting new_attribute to 42

# __getattr__(self, name): 当访问不存在的属性时调用。
# __getattribute__(self, name): 每次访问任何属性时调用（慎用）。
# __setattr__(self, name, value): 设置属性时调用。
# __delattr__(self, name): 删除属性时调用。

```

6. 上下文管理
支持 with 语句.

```
class Resource:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with Resource() as res:
    print("Inside context")

# __enter__(self): 在进入上下文时调用。
# __exit__(self, exc_type, exc_value, traceback): 在退出上下文时调用。

```

7. 调用行为
使对象像函数一样调用.
```
class CallableClass:
    def __call__(self, x):
        return x ** 2

c = CallableClass()
print(c(5))  # 25
```

8. 其他魔法函数
```
# __del__(self): 定义对象被销毁时的行为（不推荐用作关键逻辑）。
# __bool__(self): 定义对象在布尔上下文中的值。
# __hash__(self): 定义对象的哈希值，支持集合操作。
# __format__(self, format_spec): 定义 format() 的行为。
```

### Python 基础数据类型

|类型|描述|示例|
|:---|:---|:---|
|int|整数|42, 0b1010|
|float|浮点数|3.14, 1e-4|
|complex|复数|1+2j|
|bool|布尔值|True, False|
|str|字符串|"hello", 'world'|
|list|可变列表|[1, 2, 3]|
|tuple|不可变元组|(1, 2, 3)|
|set|无序集合|{1, 2, 3}|
|dict|键值对字典|{"a": 1, "b": 2}|
|NoneType|空值|None|
|bytes|不可变字节序列|b'hello'|
|bytearray|可变字节序列|bytearray(b'hello')|
|range|不可变整数序列|range(1, 5)|

### tuple 和 set 

tuple: 有序的数据结构，元素可以重复，不可变的，使用圆括号 () 定义 ： (1, 2, 3) 或 tuple([1, 2, 3]) 。

set: 无序的数据结构，元素不能重复，集合是可变的（mutable），可以动态添加或删除元素，但集合的元素必须是可哈希的（immutable），使用大括号 {} 或 set() 定义：{1, 2, 3} 或 set([1, 2, 3])。
常用于，去重，集合运算，交集，并集，差集。
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)  # 交集：{3}
print(set1 | set2)  # 并集：{1, 2, 3, 4, 5}
print(set1 - set2)  # 差集：{1, 2}


### with as 
with...as 是 Python 中的上下文管理语句，用于简化资源管理，确保资源（如文件、网络连接、锁等）在使用后被正确释放，避免资源泄露问题。

基本用法：
```
with <expression> as <variable>:
    <block>

# <expression>：上下文管理器对象，必须实现 __enter__() 和 __exit__() 方法。
# <variable>：上下文管理器返回的对象，通常是资源的句柄。
# <block>：要执行的代码块，在上下文中运行。

```

1. 文件操作
with...as 常用于文件操作，确保文件在操作完成后正确关闭。
```
# 使用传统方式打开和关闭文件
file = open("example.txt", "r")
try:
    content = file.read()
finally:
    file.close()

# 使用 with...as 自动管理资源
with open("example.txt", "r") as file:
    content = file.read()
# 文件在退出 with 块后自动关闭

```
2. 数据库连接
确保数据库连接在操作完成后自动关闭。
```
import sqlite3

with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
    conn.commit()
# 数据库连接自动关闭

```
3. 锁管理
确保线程锁在使用后自动释放。
```
from threading import Lock

lock = Lock()

with lock:
    # 线程安全代码块
    print("Lock acquired")
# 锁自动释放

```

### 装饰器

装饰器（Decorator）是 Python 中的一种强大功能，主要用于在不改变原始函数或类的情况下，动态地扩展其功能。它以一种优雅的方式实现了代码复用和逻辑增强。
装饰器是一个接受函数或类作为输入，并返回一个新函数或类的函数。 装饰器也可以装饰类。 
使用 @decorator_name 语法来简化装饰器的使用。

```
# 首先是要定一个装饰器
def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

# @decorator_name 语法来使用装饰器。 相当于 my_function = simple_decorator(say_hello)
@simple_decorator 
def say_hello():
    print("Hello, world!")

say_hello()

```

如果被装饰的函数接受参数，需要在装饰器中处理这些参数。
```

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@logging_decorator
def add(a, b):
    return a + b

add(3, 5)

```
装饰器本身也可以接受参数，需要再嵌套一层。
```
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

```


### 生成器和迭代器
在 Python 中，生成器和迭代器是实现迭代的两种重要机制。它们提供了惰性求值的能力，允许在需要时按需生成数据，而不是一次性加载所有数据，从而节省内存。

**迭代器（Iterator）**

迭代器是一个对象，实现了 __iter__() 和 __next__() 方法。
特点：可以使用 next() 方法按需返回下一个值。
用途：用来逐个访问可迭代对象中的元素，而无需一次性加载所有数据。

**生成器**

生成器是一个特殊的迭代器，可以用更简洁的语法创建。
使用 yield 关键字生成值，而不是返回值。
每次调用 yield 时，函数的执行会暂停，状态会被保存，以便下次继续执行。

gen = (x ** 2 for x in range(5))

### 设计模式



### Python 闭包
闭包是一个函数对象，它不仅包含函数的代码，还保存了函数外部作用域的变量。当一个函数在其外部函数的作用域内被定义，并且该函数引用了外部函数中的变量时，就形成了一个闭包。

闭包的定义包括三个要素：
1. 函数嵌套：一个函数定义在另一个函数内部。
2. 内部函数引用外部函数的变量。
3. 外部函数返回内部函数。

闭包能够访问外部函数的变量，即使外部函数的执行已经结束。这种特性使得闭包在一些场景中非常有用，比如工厂函数、回调函数、保持状态等。

```
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# 创建闭包
closure = outer_function(10)

# 调用闭包
print(closure(5))  # 输出 15

```

1. 如工厂函数

```
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add_five = make_adder(5)
print(add_five(10))  # 输出 15

```
2. 回调函数
```
def outer_function():
    message = "Hello"
    def callback():
        print(message)
    return callback

callback_fn = outer_function()
callback_fn()  # 输出 "Hello"

```

### Python 并发
在 Python 中，常见的并发实现方式有以下三种：
1. 多线程（Threading）：通过线程实现并发，适合 I/O 密集型任务。
2. 多进程（Multiprocessing）：通过进程实现并发，适合 CPU 密集型任务。
3. 异步编程（Asyncio）：通过协程实现并发，适合 I/O 密集型任务且对性能要求较高。

```
# 多线程
import threading
import time

def worker(name):
    print(f"{name} is starting")
    time.sleep(2)
    print(f"{name} is finished")

# 创建多个线程
threads = []
for i in range(5):
    thread = threading.Thread(target=worker, args=(f"Thread-{i}",))
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print("All threads finished")

```

```
#多进程

import multiprocessing
import time

def worker(name):
    print(f"{name} is starting")
    time.sleep(2)
    print(f"{name} is finished")

# 创建多个进程
processes = []
for i in range(5):
    process = multiprocessing.Process(target=worker, args=(f"Process-{i}",))
    processes.append(process)
    process.start()

# 等待所有进程完成
for process in processes:
    process.join()

print("All processes finished")

```

```
#异步编程
import asyncio

async def worker(name):
    print(f"{name} is starting")
    await asyncio.sleep(2)
    print(f"{name} is finished")

async def main():
    tasks = [worker(f"Task-{i}") for i in range(5)]
    await asyncio.gather(*tasks)

# 运行事件循环
asyncio.run(main())

```

如何控制并行度？
1. 多线程并行度控制 使用 ThreadPoolExecutor 或者 threading.Semaphore。

```
# ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    print(f"{name} is starting")
    time.sleep(2)
    print(f"{name} is finished")

# 设置最大并行线程数为3
with ThreadPoolExecutor(max_workers=3) as executor:
    tasks = [executor.submit(task, f"Thread-{i}") for i in range(10)]


# threading.Semaphore。
import threading
import time

semaphore = threading.Semaphore(3)  # 限制最大并行线程数为3

def task(name):
    with semaphore:
        print(f"{name} is starting")
        time.sleep(2)
        print(f"{name} is finished")

threads = []
for i in range(10):
    thread = threading.Thread(target=task, args=(f"Thread-{i}",))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

```

2. 多进程并行度控制。使用 ProcessPoolExecutor 或者 multiprocessing.Semaphore

```
# ProcessPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

def task(name):
    print(f"{name} is starting")
    time.sleep(2)
    print(f"{name} is finished")

# 设置最大并行进程数为3
with ProcessPoolExecutor(max_workers=3) as executor:
    tasks = [executor.submit(task, f"Process-{i}") for i in range(10)]

# multiprocessing.Semaphore 

import multiprocessing
import time

semaphore = multiprocessing.Semaphore(3)  # 限制最大并行进程数为3

def task(name):
    with semaphore:
        print(f"{name} is starting")
        time.sleep(2)
        print(f"{name} is finished")

processes = []
for i in range(10):
    process = multiprocessing.Process(target=task, args=(f"Process-{i}",))
    processes.append(process)
    process.start()

for process in processes:
    process.join()

```

3. 异步编程并行度控制. 使用 asyncio.Semaphore 

```
import asyncio

semaphore = asyncio.Semaphore(3)  # 限制最大并发任务数为3

async def task(name):
    async with semaphore:
        print(f"{name} is starting")
        await asyncio.sleep(2)
        print(f"{name} is finished")

async def main():
    tasks = [task(f"Task-{i}") for i in range(10)]
    await asyncio.gather(*tasks)

asyncio.run(main())

```
### Python 构造函数
