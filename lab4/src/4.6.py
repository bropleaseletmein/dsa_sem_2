import sys

s = sys.stdin.readline().strip()
n = len(s)
z = [0] * n
l = 0
r = 0

for i in range(1, n):
   if i < r:
       z[i] = min(r - i, z[i - l])
   while i + z[i] < n and s[z[i]] == s[i + z[i]]:
       z[i] += 1
   if i + z[i] > r:
       l = i
       r = i + z[i]

sys.stdout.write(' '.join(map(str, z[1:])))
