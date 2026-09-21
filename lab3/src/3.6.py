from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
   a, b = map(int, input().split())
   g[a].append(b)
   g[b].append(a)

u, v = map(int, input().split())

dist = [-1] * (n + 1)
dist[u] = 0
q = deque([u])

while q:
   x = q.popleft()
   for y in g[x]:
       if dist[y] == -1:
           dist[y] = dist[x] + 1
           q.append(y)

print(dist[v])
