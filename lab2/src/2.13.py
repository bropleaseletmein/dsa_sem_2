n = int(input())
key, left, right = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
for i in range(1, n + 1):
   k, l, r = map(int, input().split())
   key[i] = k
   left[i] = l
   right[i] = r

height = [0] * (n + 1)
for i in range(n, 0, -1):
   height[i] = 1 + max(height[left[i]], height[right[i]])

a = 1
b = right[a]
if height[right[b]] - height[left[b]] == -1:
   c = left[b]
   right[a] = left[c]
   left[b] = right[c]
   left[c] = a
   right[c] = b
   root = c
else:
   right[a] = left[b]
   left[b] = a
   root = b

new = [0] * (n + 1)
order = [root]
new[root] = 1
cnt = 1
i = 0
while i < len(order):
   v = order[i]
   i += 1
   if left[v] != 0:
       cnt += 1
       new[left[v]] = cnt
       order.append(left[v])
   if right[v] != 0:
       cnt += 1
       new[right[v]] = cnt
       order.append(right[v])

print(n)
for v in order:
   print(key[v], new[left[v]], new[right[v]])
