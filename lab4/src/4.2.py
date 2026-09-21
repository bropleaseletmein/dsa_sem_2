s = input().replace(' ', '')

pos = {}
for i, c in enumerate(s):
   pos.setdefault(c, []).append(i)

total = 0
for lst in pos.values():
   pref = 0
   for k, q in enumerate(lst):
       total += k * q - pref - k
       pref += q

print(total)
