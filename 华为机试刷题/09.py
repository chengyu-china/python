def ck(s, t, a, b):
    va = [0] * 10  # 用于记录各数字出现的次数（0-9）
    vb = [0] * 10
    
    # 检查四位数字
    for i in range(4):
        ss = s % 10
        tt = t % 10
        s //= 10
        t //= 10
 
        if ss == tt:  # 如果位置和数字都正确
            a -= 1  # 减少a的计数
        else:
            va[ss] += 1  # 记录数字ss出现的次数
            vb[tt] += 1  # 记录数字tt出现的次数
 
    # 检查位置不正确但数字正确的情况
    for i in range(10):
        b -= min(va[i], vb[i])  # 计算并减少b的计数
 
    return a == 0 and b == 0
 
 
n = int(input())  # 输入猜测的组数
v = []  # 存储每次猜测的数字和对应提示
 
# 输入每组猜测信息
for i in range(n):
    tmp = [0] * 3  # 临时存储当前猜测的数字和提示
    s = input().split()
    tmp[0] = int(s[0])  # 猜测的四位数字
    tmp[1] = int(s[1][0])  # 提示的X值，即位置正确的数字个数
    tmp[2] = int(s[1][2])  # 提示的Y值，即数字正确但位置不对的个数
    v.append(tmp)
 
ans = []  # 用于存储可能的答案
 
# 遍历所有可能的四位数字（0000到9999）
for val in range(10000):
    flag = True  # 标记当前数字是否符合所有提示
 
    # 检查当前数字是否符合所有已知提示
    for lis in v:
        if not ck(val, lis[0], lis[1], lis[2]):
            flag = False
            break
    
    if flag:
        ans.append(val)  # 如果符合，加入可能的答案列表
    
    if len(ans) > 1:  # 如果有多个可能的答案，跳出循环
        break
 
# 根据可能的答案数量输出结果
if len(ans) == 1:
    print(f"{ans[0]:04d}")  # 如果有且仅有一个答案，输出
elif len(ans) > 1:
    print("NA")  # 如果答案不唯一，输出NA