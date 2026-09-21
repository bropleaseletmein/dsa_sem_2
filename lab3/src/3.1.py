n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
   a, b = map(int, input().split())
   g[a].append(b)
   g[b].append(a)

u, v = map(int, input().split())

visited = [False] * (n + 1)
visited[u] = True
stack = [u]

while stack:
   x = stack.pop()
   for y in g[x]:
       if not visited[y]:
           visited[y] = True
           stack.append(y)

print(1 if visited[v] else 0)
