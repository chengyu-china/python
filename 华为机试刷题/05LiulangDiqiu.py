import sys 
import heapq

data = sys.stdin.read().splitlines()

N, E = map(int,data[0].split())

activation_time = [-1]*N

visited = [False]*N

pq = [] 

for i in range(1,E + 1):
    T, P = map(int, data[i].split())
    if activation_time[P] == -1:
        activation_time[P] = T 
        heapq.heappush(pq,(T,P))

while pq:
    time, pos = heapq.heappop(pq)

    if visited[pos]:
        continue

    visited[pos] = True

    next_time = time + 1

    neighbors = [(pos - 1 + N) % N,(pos+1)% N]

    for neighbor in neighbors:
        if activation_time[neighbor] == -1 or activation_time[neighbor] > next_time:
            activation_time[neighbor] = next_time

            if not visited[neighbor]:
                heapq.heappush(pq,(next_time,neighbor))
    
Max_time = max(activation_time)

latest_engines = [i for i in range(N) if activation_time[i] == Max_time]

print(len(latest_engines))
latest_engines.sort()
print(" ".join(map(str,latest_engines)))






