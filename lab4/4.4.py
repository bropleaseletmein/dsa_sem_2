import sys

data = sys.stdin.read().split()
s = data[0]
q = int(data[1])
n = len(s)

m1 = 10 ** 9 + 7
m2 = 10 ** 9 + 9
x = 263

h1 = [0] * (n + 1)
h2 = [0] * (n + 1)
p1 = [1] * (n + 1)
p2 = [1] * (n + 1)

for i in range(1, n + 1):
   c = ord(s[i - 1])
   h1[i] = (h1[i - 1] * x + c) % m1
   h2[i] = (h2[i - 1] * x + c) % m2
   p1[i] = p1[i - 1] * x % m1
   p2[i] = p2[i - 1] * x % m2

out = []
k = 2
for _ in range(q):
   a = int(data[k])
   b = int(data[k + 1])
   l = int(data[k + 2])
   k += 3
   f1 = (h1[a + l] - h1[a] * p1[l]) % m1
   g1 = (h1[b + l] - h1[b] * p1[l]) % m1
   f2 = (h2[a + l] - h2[a] * p2[l]) % m2
   g2 = (h2[b + l] - h2[b] * p2[l]) % m2
   out.append("Yes" if f1 == g1 and f2 == g2 else "No")

print("\n".join(out))
