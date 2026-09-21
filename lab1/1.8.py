n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]

lectures.sort(key=lambda x: x[1])

count = 0
last = 0

for s, f in lectures:
   if s >= last:
       count += 1
       last = f

print(count)
