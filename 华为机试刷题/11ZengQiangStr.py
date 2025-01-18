def solve():
    s = input()  # 输入源字符串
    t = input()  # 输入目标字符串
 
    v = []  # 用于存储目标字符串的匹配模式，使用字符集的列表表示
    st = set()  # 临时字符集，用于存储方括号内的字符
    f1 = False  # 标记当前是否在处理方括号内的字符
    # abc[de]fg
    # 遍历目标字符串t，构建匹配模式

    for c in t:
        if c == '[':  # 遇到'['，进入方括号模式
            f1 = True
        elif c == ']':  # 遇到']'，退出方括号模式
            f1 = False
            v.append(st.copy())  # 将当前方括号内的字符集加入模式列表
            st.clear()  # 清空字符集，为下一次使用做准备
        else:
            st.add(c)  # 将字符加入当前字符集
            if not f1:  # 如果不在方括号内，说明是普通字符
                v.append(st.copy())  # 直接将当前字符（作为单字符集）加入模式列表
                st.clear()  # 清空字符集
    
    n = len(s)  # 获取源字符串的长度
    m = len(v)  # 获取匹配模式的长度
    ans = -1  # 初始化结果为-1，表示未找到匹配
 
    # 遍历源字符串，尝试匹配目标字符串的模式
    for i in range(n - m + 1):  # 从源字符串的每一个可能起始位置开始匹配
        f2 = True  # 标记当前尝试是否匹配成功
 
        # 检查当前子串是否匹配模式
        for j in range(m):
            if s[i + j] not in v[j]:  # 如果当前字符不在相应位置的字符集中，匹配失败
                f2 = False
                break  # 匹配失败，停止当前尝试
 
        if f2:  # 如果成功匹配，记录偏移量并结束搜索
            ans = i
            break
 
    print(ans)  # 输出最终的匹配偏移量
 
if __name__ == "__main__":
    solve()