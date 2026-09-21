n = int(input())
key = [0] * n
left = [0] * n
right = [0] * n

for i in range(n):
   k, l, r = map(int, input().split())
   key[i] = k
   left[i] = l
   right[i] = r

inf = float('inf')
ok = True
stack = [(0, -inf, inf)] if n > 0 else []

while stack:
   v, lo, hi = stack.pop()
   if not lo < key[v] < hi:
       ok = False
       break
   if left[v] != -1:
       stack.append((left[v], lo, key[v]))
   if right[v] != -1:
       stack.append((right[v], key[v], hi))

if ok:
   print("CORRECT")
else:
   print("INCORRECT")
