from datetime import datetime
 
class App:
    """表示一个App的类，包含名称、优先级、开始时间和结束时间"""
    def __init__(self, name, priority, start_time, end_time):
        self.name = name
        self.priority = priority
        self.start_time = start_time
        self.end_time = end_time
 
def time_to_minutes(time_str):
    """将时间字符串（格式HH:MM）转换为一天中从00:00开始的分钟数"""
    return int(time_str[:2]) * 60 + int(time_str[3:5])
 
def main():
    N = int(input())  # 读入要注册的App数量
    registered_apps = []  # 存储所有注册成功的App
 
    for _ in range(N):
        line = input()  # 读取一行App注册信息
        name, priority, start, end = line.split()
        priority = int(priority)
        start_time = time_to_minutes(start)
        end_time = time_to_minutes(end) - 1
        if start_time > end_time:
            continue  # 如果开始时间大于结束时间，则跳过此次注册
 
 
        # 检查冲突并确定是否能注册
        can_register = True
        for app in registered_apps:
            if (start_time <= app.end_time and end_time >= app.start_time):
                if priority <= app.priority:
                    can_register = False
                    break
 
        if can_register:
            # 剔除所有时间上冲突的App
            new_registered = [app for app in registered_apps if not (start_time <= app.end_time and end_time >= app.start_time)]
            new_registered.append(App(name, priority, start_time, end_time))
            registered_apps = new_registered
 
    query_time = input()  # 读取查询时间
    query_minute = time_to_minutes(query_time)
 
    # 查询特定时间点的App
    for app in registered_apps:
        if app.start_time <= query_minute <= app.end_time:
            print(app.name)
            return
 
    print("NA")
 
if __name__ == "__main__":
    main()