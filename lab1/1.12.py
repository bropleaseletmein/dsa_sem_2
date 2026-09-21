n = int(input())
a = list(map(int, input().split()))
s = sum(a)

if s % 2 == 1:
   print(-1)
else:
   target = s // 2
   res = []
   for i in range(n - 1, -1, -1):
       if a[i] <= target:
           target -= a[i]
           res.append(i + 1)
   res.reverse()
   print(len(res))
   print(*res)
