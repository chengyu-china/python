from collections import defaultdict
from collections import deque

# 这个作用使用list 来存储 values。 一个key 可以有多个 values， 把他们都放在一个list中。
# 很适合作为存储邻接表，存储有向图。
g = defaultdict(list)


def solve():

    global g
    m = int(input())
    N = int(1e6+5)
    n = 0
    du = [0] * N
    val = [0] * N

    while m:
        m -= 1
        u, v, w = map(int, input().split())
        n = max(n, max(u, v))       # 手动计算 n 值, 这个就是节点的个数
        g[u].append(v)              # 建图
        du[v] += 1                  # 记录每个点的入度
        val[u] += w                 # 记录收入


    q = deque()

    # 将入度为 0 的点入队
    for i in range(n+1):
        if du[i] == 0:
            q.append(i)
    # 拓扑遍历
    while q:
        u = q.popleft()
        for v in g[u]:
            du[v] -= 1              # 入度-1
            val[v] += val[u] // 100 * 15        # 计算收入
            if du[v] == 0:          # 入度为 0 的点入队
                q.append(v)
        # 最后剩下的点一定是 boss
        if len(q) == 0:     
            print(u, val[u])
 
 
if __name__ == '__main__':
    solve()