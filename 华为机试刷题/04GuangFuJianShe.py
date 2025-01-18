import sys

data = sys.stdin.read().split()

region_length = int(data[0])
region_width = int(data[1])
square_side = int(data[2])
min_power = int(data[3])

# print(data)

# 初始化二维数组
# region_length = 2 
# region_width = 5

power_grid = [[0]*(region_width + 1) for _ in range(region_length + 1)]

# 录入数据

index = 4

for i in range(1,region_length + 1):
    for j in range(1,region_width + 1):
        power_grid[i][j] = int(data[index])
        # print(data[index])
        index += 1

print(power_grid)

# 构建前缀和矩阵
for i in range(1,region_length + 1):
    for j in range(1,region_width + 1):
        power_grid[i][j] += power_grid[i][j-1] + power_grid[i-1][j] - power_grid[i-1][j-1]

count = 0
# 

for i in range(1,region_length - square_side + 2):
    for j in range(1,region_width - square_side + 2):
        x2 = i + square_side - 1 
        y2 = j + square_side - 1

        total_power = power_grid[x2][y2] - power_grid[i-1][y2] - power_grid[x2][j-1] + power_grid[i-1][j-1]

        if total_power >= min_power:
            count += 1

print(count)
