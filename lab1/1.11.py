W, n = map(int, input().split())
w = list(map(int, input().split()))

dp = [0] * (W + 1)

for x in w:
   for j in range(W, x - 1, -1):
       if dp[j - x] + x > dp[j]:
           dp[j] = dp[j - x] + x

print(dp[W])
