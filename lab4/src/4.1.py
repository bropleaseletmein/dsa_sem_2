p = input()
t = input()

res = []
for i in range(len(t) - len(p) + 1):
   equal = True
   for j in range(len(p)):
       if t[i + j] != p[j]:
           equal = False
           break
   if equal:
       res.append(i + 1)

print(len(res))
print(*res)
