NumPy 是 Python 中一个强大的数值计算库，提供了高效的多维数组对象和多种用于数组操作的函数。

### 创建 NumPy 数组
NumPy 提供了多种方式来创建数组，最常见的是使用 np.array()、np.zeros()、np.ones()、np.arange()、np.linspace() 等。
```
import numpy as np
# 从列表创建 NumPy 数组
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 创建全零数组
arr_zeros = np.zeros((3, 4))  # 创建一个 3x4 的全零数组
print(arr_zeros)

# 创建全一数组
arr_ones = np.ones((2, 3))  # 创建一个 2x3 的全一数组
print(arr_ones)

# 创建均匀间隔的数组
arr_range = np.arange(0, 10, 2)  # 创建一个从 0 到 10 步长为 2 的数组
print(arr_range)

# 创建指定范围的数组
arr_linspace = np.linspace(0, 1, 5)  # 创建一个从 0 到 1 的数组，包含 5 个等间隔的值
print(arr_linspace)

```

### 数组属性
NumPy 数组有多个属性，如形状、维度、大小等，可以用来查看数组的基本信息。

```
import numpy as np

# 查看数组的形状和维度
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)  # 输出 (2, 3)，表示有 2 行 3 列
print(arr.ndim)  # 输出 2，表示是二维数组
print(arr.size)  # 输出 6

# 查看数组的数据类型
arr = np.array([1, 2, 3])
print(arr.dtype)  # 输出 int64，表示数据类型

```

### 数组操作
NumPy 提供了丰富的数组操作方法，包括数学计算、切片、索引等。
```
import numpy as np

# 数组的基本数学操作 加减乘除
arr = np.array([1, 2, 3])

arr_add = arr + 5
print(arr_add)  # 输出 [6 7 8]

arr_sub = arr - 1
print(arr_sub)  # 输出 [0 1 2]

arr_mul = arr * 2
print(arr_mul)  # 输出 [2 4 6]

arr_div = arr / 2
print(arr_div)  # 输出 [0.5 1.  1.5]

# 矩阵乘法
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr_dot = np.dot(arr1, arr2)
print(arr_dot)

# 数组切片和索引
arr = np.array([10, 20, 30, 40, 50])

print(arr[:3])  # 取前 3 个元素， 输出 [10 20 30]
print(arr[2:])  # 取从索引 2 开始到结尾的元素，输出 [30 40 50]
print(arr[1:4])  # 取第 2 到第 4 个元素，输出 [20 30 40]
print(arr[-2:])  # 使用负索引，输出 [40 50]

```

### 数组的聚合函数
NumPy 提供了多种聚合函数，如 sum()、mean()、std() 等，帮助你对数据进行统计计算。

```
import numpy as np

# 求和、均值和标准差
arr = np.array([1, 2, 3, 4, 5])

print(np.sum(arr))  # 求和 输出 15
print(np.mean(arr))  # 求均值 输出 3.0
print(np.std(arr))  # 求标准差 输出 1.4142135623730951

# 按轴进行聚合
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(arr, axis=0))  ## 按列求和 输出 [5 7 9]
print(np.sum(arr, axis=1))  # 按行求和输出 [6 15]

```

### 数组的条件筛选

```
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# 筛选出大于 3 的元素
arr_filtered = arr[arr > 3]
print(arr_filtered)  # 输出 [4 5]

```

### 数组的重塑和转置
NumPy 提供了 reshape() 和 T（转置）方法来改变数组的形状。

```
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# 重塑为 2 行 3 列的矩阵
arr_reshaped = arr.reshape(2, 3)
print(arr_reshaped)

# 数组转置
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr_transposed = arr.T
print(arr_transposed)

```

