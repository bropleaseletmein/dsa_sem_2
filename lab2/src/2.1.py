def in_order(key, left, right):
   result, stack = [], []
   v = 0
   while stack or v != -1:
       while v != -1:
           stack.append(v)
           v = left[v]
       v = stack.pop()
       result.append(key[v])
       v = right[v]
   return result

def pre_order(key, left, right):
   result, stack = [], [0]
   while stack:
       v = stack.pop()
       result.append(key[v])
       if right[v] != -1:
           stack.append(right[v])
       if left[v] != -1:
           stack.append(left[v])
   return result

def post_order(key, left, right):
   result, stack = [], [0]
   while stack:
       v = stack.pop()
       result.append(key[v])
       if left[v] != -1:
           stack.append(left[v])
       if right[v] != -1:
           stack.append(right[v])
   result.reverse()
   return result

n = int(input())
key, left, right = [], [], []
for _ in range(n):
   k, l, r = map(int, input().split())
   key.append(k)
   left.append(l)
   right.append(r)

print(*in_order(key, left, right))
print(*pre_order(key, left, right))
print(*post_order(key, left, right))
