n, s = map(int, input().split())
apples = [tuple(map(int, input().split())) for _ in range(n)]

order = sorted(range(n), key=lambda i: -apples[i][0])

for i in order:
   a, b = apples[i]
   if s - a <= 0:
       print(-1)
       break
   s = s - a + b
else:
   print(*[i + 1 for i in order])
