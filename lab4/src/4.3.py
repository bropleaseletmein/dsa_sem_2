import sys

data = sys.stdin.read().split()
p = data[0]
t = data[1]
np = len(p)
nt = len(t)

res = []
if np <= nt:
   m = 10 ** 9 + 7
   x = 263
   hp = 0
   for c in p:
       hp = (hp * x + ord(c)) % m
   xl = pow(x, np, m)
   h = 0
   for i in range(np):
       h = (h * x + ord(t[i])) % m
   if h == hp and t[:np] == p:
       res.append(1)
   for i in range(np, nt):
       h = (h * x + ord(t[i]) - xl * ord(t[i - np])) % m
       if h == hp and t[i - np + 1:i + 1] == p:
           res.append(i - np + 2)

print(len(res))
print(*res)
