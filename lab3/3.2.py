n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
   a, b = map(int, input().split())
   g[a].append(b)
   g[b].append(a)

visited = [False] * (n + 1)
count = 0

for s in range(1, n + 1):
   if visited[s]:
       continue
   count += 1
   visited[s] = True
   stack = [s]
   while stack:
       x = stack.pop()
       for y in g[x]:
           if not visited[y]:
               visited[y] = True
               stack.append(y)

print(count)
