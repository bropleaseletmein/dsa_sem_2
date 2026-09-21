n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

dist = [0] * (n + 1)
found = 0

for i in range(n):
   changed = False
   for u, v, w in edges:
       if dist[u] + w < dist[v]:
           dist[v] = dist[u] + w
           changed = True
   if not changed:
       break
   if i == n - 1:
       found = 1

print(found)
