M = 10 ** 9

moves = {
   0: [4, 6],
   1: [6, 8],
   2: [7, 9],
   3: [4, 8],
   4: [0, 3, 9],
   5: [],
   6: [0, 1, 7],
   7: [2, 6],
   8: [1, 3],
   9: [2, 4]
}

n = int(input())

dp = [0] * 10
for d in range(10):
   if d != 0 and d != 8:
       dp[d] = 1

for _ in range(n - 1):
   new_dp = [0] * 10
   for d in range(10):
       for x in moves[d]:
           new_dp[x] = (new_dp[x] + dp[d]) % M
   dp = new_dp

print(sum(dp) % M)
