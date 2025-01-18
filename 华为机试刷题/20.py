
# nums = [3,2,1,3]

# def maxMoney(nums,index):
#     if index < 0 or nums == None:
#         return 0
#     if index == 0:
#         return nums[0]

#     return max(maxMoney(nums,index-1),maxMoney(nums,index-2) + nums[index])

# def maxMoney1(nums):
#     length = len(nums)
#     dp = [0]*length
#     length = len(nums)

#     if length == 0:
#         return 0
#     if length == 1:
#         return nums[0]
    
#     dp[0] = nums[0]
#     dp[1] = max(nums[0],nums[1])

#     i = 2
#     while i < length:
#         dp[i] = max(dp[i - 1],dp[i-2] + nums[i])
#         i += 1
    
#     return dp[length - 1]


# # print(maxMoney(nums,len(nums)-1))

# print(maxMoney1(nums))


# def maximize_reward(T, n, tasks):
#     # 初始化 DP 数组，长度为 T + 1，初始值为 0
#     dp = [0] * (T + 1)
    
#     # 遍历每个任务，读取任务所需时间 t 和报酬 w
#     for t, w in tasks:
#         # 从后向前更新 DP 数组
#         for j in range(T, t - 1, -1):
#             dp[j] = max(dp[j], dp[j - t] + w)
    
#     # 返回在 T 时间内能获得的最大报酬
#     return dp[T]
 
# if __name__ == "__main__":
#     # 读取输入
#     T, n = map(int, input().split())
#     tasks = []
 
#     for _ in range(n):
#         t, w = map(int, input().split())
#         tasks.append((t, w))
    
#     # 调用函数并输出结果
#     result = maximize_reward(T, n, tasks)
#     print(result)


T , n = map(int,input().split())

tasks = []

for i in range(n):
    t, w = map(int,input().split())
    tasks.append((t,w))

dp = [[0]* (T+1) for _ in range(n+1)]

for i in range(0,n):
    for j in range(1,T + 1):
        if j < tasks[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            data1 = dp[i-1][j]
            data2 = dp[i-1][j-tasks[i][0]] + tasks[i][1]
            dp[i][j] = max(data1,data2)

maxw = 0 

for e in dp:
    w = max(e)
    if w > maxw:
        maxw = w

print(maxw)