n = int(input())
key = [0] * (n + 1)
left = [0] * (n + 1)
right = [0] * (n + 1)

for i in range(1, n + 1):
   k, l, r = map(int, input().split())
   key[i] = k
   left[i] = l
   right[i] = r

inf = float('inf')
ok = True
stack = [(1, -inf, inf)] if n > 0 else []

while stack:
   v, lo, hi = stack.pop()
   if not lo < key[v] < hi:
       ok = False
       break
   if left[v] != 0:
       stack.append((left[v], lo, key[v]))
   if right[v] != 0:
       stack.append((right[v], key[v], hi))

if ok:
   print("YES")
else:
   print("NO")
