from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
   a, b = map(int, input().split())
   g[a].append(b)
   g[b].append(a)

color = [-1] * (n + 1)
ok = True

for s in range(1, n + 1):
   if color[s] != -1:
       continue
   color[s] = 0
   q = deque([s])
   while q:
       x = q.popleft()
       for y in g[x]:
           if color[y] == -1:
               color[y] = 1 - color[x]
               q.append(y)
           elif color[y] == color[x]:
               ok = False

if ok:
   print(1)
else:
   print(0)
