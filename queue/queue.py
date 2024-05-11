from collections import deque

data = deque()
data.append(1)
data.append(2)
data.append(3)
print(data)
data.popleft()
print(data) 