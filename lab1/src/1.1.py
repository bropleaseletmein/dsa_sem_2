n, W = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[0] / x[1], reverse=True)
result = 0

for item in arr:
   if W <= 0:
       break
   result += (item[0] / item[1]) * min(item[1], W)
   W -= item[1]

print(f"{result:.4f}")
