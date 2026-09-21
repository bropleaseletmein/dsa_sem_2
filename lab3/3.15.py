from collections import deque

n, m = map(int, input().split())
grid = [input() for _ in range(n)]
qx, qy, l = map(int, input().split())

dist = [[-1] * m for _ in range(n)]
dist[qx - 1][qy - 1] = 0
q = deque([(qx - 1, qy - 1)])

while q:
   x, y = q.popleft()
   for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
       a, b = x + dx, y + dy
       if 0 <= a < n and 0 <= b < m and grid[a][b] == '0' and dist[a][b] == -1:
           dist[a][b] = dist[x][y] + 1
           q.append((a, b))

total = 0
for _ in range(4):
   ax, ay, p = map(int, input().split())
   if dist[ax - 1][ay - 1] != -1 and dist[ax - 1][ay - 1] <= l:
       total += p

print(total)
