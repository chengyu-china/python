
# num = int(input())
# days = int(input())
# items = list(map(int,input().split()))

# ans = 0 

# for i in range(num):
#     price = list(map(int,input().split()))
#     maxPrice = max(price)
#     maxPriceIndex = 0

#     for j in range(days):
#         if price[j] == maxPrice:
#             maxPriceIndex = j
#             break

#     if maxPriceIndex ==0:
#         continue

#     minPrice = min(price[0:maxPriceIndex])

#     ans += (maxPrice - minPrice)*items[i]

# print(ans)

def solve():
    n = int(input())        # 商品种类数量n
    m = int(input())        # 售货天数m
    num = list(map(int, input().split()))  # 输入每种商品的最大持有数量
    ans = 0  # 初始化总利润变量为0
    for i in range(n):  # 遍历每种商品
        price = list(map(int, input().split()))  # 输入每种商品在每一天的价格
        res = 0  # 初始化临时利润变量res
        for j in range(m - 1):  # 遍历每一天的价格（不包括最后一天）
            if price[j + 1] > price[j]:  # 如果第二天的价格高于当天价格
                res += price[j + 1] - price[j]  # 计算当天买入第二天卖出的利润并累计到res 这个res 是累加的。 
        ans += res * num[i]  # 计算该商品在所有天内可能获得的最大利润，并累加到总利润ans中
    print(ans)  # 输出商人在给定天数内可能获得的最大总利润
 
if __name__ == "__main__":
    solve()

