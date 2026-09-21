n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

inf = float('inf')
visited = [False] * n
memo = {}
choice = {}
#пришлось пожертвовать оформлением кода тк код не влезал на страницу
def solve(v, cnt):
   if cnt == n: return 0
   key = (tuple(visited), v)
   if key in memo: return memo[key]
   best = inf
   best_u = -1
   for u in range(n):
       if not visited[u]:
           visited[u] = True
           cost = a[v][u] + solve(u, cnt + 1)
           visited[u] = False
           if cost < best:
               best = cost
               best_u = u
   memo[key] = best
   choice[key] = best_u
   return best

answer = inf
start = 0
for v in range(n):
   visited[v] = True
   cost = solve(v, 1)
   visited[v] = False
   if cost < answer:
       answer = cost
       start = v

path = [start + 1]
visited[start] = True
v = start
for _ in range(n - 1):
   u = choice[(tuple(visited), v)]
   visited[u] = True
   path.append(u + 1)
   v = u
print(answer)
print(*path)
