n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
gt = [[] for _ in range(n + 1)]

for _ in range(m):
   u, v = map(int, input().split())
   g[u].append(v)
   gt[v].append(u)

visited = [False] * (n + 1)
order = []

for s in range(1, n + 1):
   if visited[s]:
       continue
   stack = [(s, False)]
   while stack:
       v, done = stack.pop()
       if done:
           order.append(v)
           continue
       if visited[v]:
           continue
       visited[v] = True
       stack.append((v, True))
       for u in gt[v]:
           if not visited[u]:
               stack.append((u, False))

visited = [False] * (n + 1)
count = 0

for v in reversed(order):
   if visited[v]:
       continue
   count += 1
   visited[v] = True
   stack = [v]
   while stack:
       x = stack.pop()
       for u in g[x]:
           if not visited[u]:
               visited[u] = True
               stack.append(u)

print(count)
