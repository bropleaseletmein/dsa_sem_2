n = int(input())
key = [0] * (n + 1)
left = [0] * (n + 1)
right = [0] * (n + 1)

for i in range(1, n + 1):
   k, l, r = map(int, input().split())
   key[i] = k
   left[i] = l
   right[i] = r

height = [0] * (n + 1)

for i in range(n, 0, -1):
   height[i] = 1 + max(height[left[i]], height[right[i]])

for i in range(1, n + 1):
   print(height[right[i]] - height[left[i]])
