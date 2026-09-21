import sys

s = sys.stdin.readline().strip()
n = len(s)
p = [0] * n
k = 0

for i in range(1, n):
   c = s[i]
   while k and c != s[k]:
       k = p[k - 1]
   if c == s[k]:
       k += 1
   p[i] = k

sys.stdout.write(' '.join(map(str, p)))
