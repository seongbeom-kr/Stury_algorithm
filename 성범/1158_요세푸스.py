from collections import deque

n, k = map(int, input().split())

p =deque()
for i in range(1, n+1): p.append(i)

result = []
    
while p:
    for _ in range(k-1):
        p.append(p.popleft())
    result.append(p.popleft())
print(str(result).replace('[', '<').replace(']', '>'))