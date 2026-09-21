n, m = map(int, input().split())
edges = []
g = [[] for _ in range(n + 1)]

for _ in range(m):
   u, v, w = map(int, input().split())
   edges.append((u, v, w))
   g[u].append(v)

s = int(input())

inf = float('inf')
dist = [inf] * (n + 1)
dist[s] = 0

for _ in range(n - 1):
   changed = False
   for u, v, w in edges:
       if dist[u] != inf and dist[u] + w < dist[v]:
           dist[v] = dist[u] + w
           changed = True
   if not changed:
       break

neg = [False] * (n + 1)
stack = []

for u, v, w in edges:
   if dist[u] != inf and dist[u] + w < dist[v] and not neg[v]:
       neg[v] = True
       stack.append(v)

while stack:
   x = stack.pop()
   for u in g[x]:
       if not neg[u]:
           neg[u] = True
           stack.append(u)

for i in range(1, n + 1):
   if dist[i] == inf:
       print("*")
   elif neg[i]:
       print("-")
   else:
       print(dist[i])
