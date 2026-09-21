s = input()
n = len(s)
inf = 10 ** 9

dp = [inf] * (n + 1)
frm = [0] * (n + 1)
per = [0] * (n + 1)
dp[0] = 0

best = inf
best_j = 0

for i in range(n + 1):
   if i > 0 and best + i < dp[i]:
       dp[i] = best + i
       frm[i] = best_j
       per[i] = i - best_j
   v = dp[i] + (1 if i > 0 else 0) - i
   if v < best:
       best = v
       best_j = i
   if i == n:
       break
   t = s[i:]
   m = n - i
   pi = [0] * m
   k = 0
   base = dp[i] + (1 if i > 0 else 0)
   for q in range(1, m):
       c = t[q]
       while k and c != t[k]:
           k = pi[k - 1]
       if c == t[k]:
           k += 1
       pi[q] = k
       L = q + 1
       p = L - k
       if k and L % p == 0:
           cost = base + p + 1 + len(str(L // p))
           if cost < dp[i + L]:
               dp[i + L] = cost
               frm[i + L] = i
               per[i + L] = p



parts = []
i = n
while i > 0:
   j = frm[i]
   p = per[i]
   a = (i - j) // p
   parts.append(s[j:j + p] if a == 1 else s[j:j + p] + '*' + str(a))
   i = j

print('+'.join(reversed(parts)))
