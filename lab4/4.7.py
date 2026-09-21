import sys

M1 = 10 ** 9 + 7
M2 = 10 ** 9 + 9
X = 263

def build(s, m):
   n = len(s)
   h = [0] * (n + 1)
   p = [1] * (n + 1)
   for i in range(1, n + 1):
       h[i] = (h[i - 1] * X + ord(s[i - 1])) % m
       p[i] = p[i - 1] * X % m
   return h, p

out = []
for line in sys.stdin:
   parts = line.split()
   if len(parts) < 2:
       continue
   s, t = parts[0], parts[1]
   hs1, p1 = build(s, M1)
   hs2, p2 = build(s, M2)
   ht1, q1 = build(t, M1)
   ht2, q2 = build(t, M2)

   ans = (0, 0, 0)
   lo = 1
   hi = min(len(s), len(t))
   while lo <= hi:
       k = (lo + hi) // 2
       table = {}
       for i in range(len(s) - k + 1):
           a = (hs1[i + k] - hs1[i] * p1[k]) % M1
           b = (hs2[i + k] - hs2[i] * p2[k]) % M2
           if (a, b) not in table:
               table[(a, b)] = i
       found = None
       for j in range(len(t) - k + 1):
           a = (ht1[j + k] - ht1[j] * q1[k]) % M1
           b = (ht2[j + k] - ht2[j] * q2[k]) % M2
           i = table.get((a, b))
           if i is not None:
               found = (i, j, k)
               break

       if found:
           ans = found
           lo = k + 1
       else:
           hi = k - 1
   out.append('%d %d %d' % ans)

print('\n'.join(out))
