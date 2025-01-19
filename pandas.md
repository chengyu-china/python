Pandas 是一个强大的 Python 库，用于数据处理、分析和操作。它提供了两种基本的数据结构：Series（一维数据）和 DataFrame（二维数据）。Pandas似乎都是按列处理。


### 创建 DataFrame 和 Series

```
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

s = pd.Series([10, 20, 30, 40])
print(s)

```

###  数据查看

```
print(df.head(2))  # 查看前 2 行
print(df.info())  # 显示 DataFrame 的列、非空值数量、数据类型等
print(df.describe())  # 查看数值型列的统计描述（均值、标准差、最小值、最大值等）
print(df.columns)  # 输出所有列名

```

### 选择和过滤数据

```
print(df['Name'])  # 选择 'Name' 列
print(df[['Name', 'Age']])  # 选择多个列

print(df.iloc[0])  # 选择第一行
print(df.loc[0])  # 通过索引选择第一行

print(df[df['Age'] > 24])  # 筛选出 Age 大于 24 的行

```

### 修改数据

```
df['Age'] = df['Age'] + 1  # 对 'Age' 列的值加 1
print(df)


df.at[0, 'City'] = 'San Francisco'  # 修改第 0 行 'City' 列的值
print(df)

df['Salary'] = [50000, 60000, 55000]  # 添加新的 'Salary' 列
print(df)

```

### 清洗数据
```
print(df.isnull())  # 查看每个元素是否为空

df['Age'].fillna(df['Age'].mean(), inplace=True)  # 用平均值填充缺失的 'Age'

df.dropna(inplace=True)  # 删除任何含有缺失值的行

df.drop_duplicates(inplace=True)  # 删除重复的行

```

### 数据合并与连接

```
# 按列连接（列方向）
df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [24, 27]})
df2 = pd.DataFrame({'City': ['New York', 'Los Angeles']})
df = pd.concat([df1, df2], axis=1)
print(df)

# 按行连接（行方向）
df3 = pd.DataFrame({'Name': ['Charlie'], 'Age': [22]})
df = pd.concat([df1, df3], axis=0, ignore_index=True)
print(df)

# 合并（类似 SQL 的 join 操作）
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 3], 'Age': [24, 22]})
df = pd.merge(df1, df2, on='ID', how='inner')  # 按 ID 合并
print(df)

```

### 排序和重排

```
df_sorted = df.sort_values(by='Age', ascending=False)  # 按 Age 排序
print(df_sorted)


df_reset = df.reset_index(drop=True)  # 重设索引，drop=True 不保留原索引
print(df_reset)

```

### 分组和聚合

```
grouped = df.groupby('City')['Age'].mean()  # 按 City 分组并计算平均 Age
print(grouped)


grouped = df.groupby('City').agg({'Age': ['mean', 'max'], 'Salary': 'sum'})
print(grouped)

```


### 透视表和交叉表

```
# 透视表
df_pivot = df.pivot_table(values='Age', index='City', aggfunc='mean')  # 计算每个城市的平均年龄
print(df_pivot)


# 交叉表
df_crosstab = pd.crosstab(df['City'], df['Age'])  # 创建一个交叉表
print(df_crosstab)

```

### 时间序列

```
# 生成时间序列
date_range = pd.date_range(start='2022-01-01', periods=5, freq='D')  # 生成日期范围
print(date_range)

# 日期列转换为 datetime 类型
df['Date'] = pd.to_datetime(df['Date'])

# 提取日期信息

df['Year'] = df['Date'].dt.year  # 提取年份
df['Month'] = df['Date'].dt.month  # 提取月份
df['Day'] = df['Date'].dt.day  # 提取日期

```

## 读取文件

```
import pandas as pd

# 从本地 CSV 文件读取数据

df = pd.read_csv('data.csv')
print(df)

df = pd.read_csv(
    'data.csv',
    sep=',',           # 指定分隔符，默认是逗号
    header=0,          # 指定表头行，默认是第 0 行
    names=['A', 'B'],  # 自定义列名
    usecols=['A', 'B'], # 读取特定列
    nrows=10,          # 只读取前 10 行
    encoding='utf-8'   # 指定文件编码
)

# 从 Excel 文件读取
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
print(df)

df = pd.read_excel(
    'data.xlsx',
    sheet_name=0,        # 读取第一个工作表
    usecols="A:C",       # 指定列范围（按列名）
    skiprows=2,          # 跳过前两行
    nrows=10             # 读取前 10 行
)

# 从 JSON 文件读取
df = pd.read_json('data.json')
print(df)

# 从 JSON 字符串读取
json_data = '{"Name":["Alice","Bob"],"Age":[24,27]}'
df = pd.read_json(json_data)
print(df)

# 读取SQL数据

from sqlalchemy import create_engine

engine = create_engine('sqlite:///example.db')  # 创建数据库连接

df = pd.read_sql('SELECT * FROM table_name', engine) # 从 SQL 查询读取数据
print(df)

# 从 Parquet 文件读取
df = pd.read_parquet('data.parquet')
print(df)

# 分块读取 CSV 文件 大文件
chunks = pd.read_csv('large_data.csv', chunksize=1000)
for chunk in chunks:
    print(chunk.head())

```

### 数据保存

```
df.to_csv('output.csv', index=False)  # 不保存索引列


df.to_excel('output.xlsx', index=False)

```