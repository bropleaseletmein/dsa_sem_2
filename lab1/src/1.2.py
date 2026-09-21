d = int(input())
m = int(input())
n = int(input())
stops = list(map(int, input().split()))

stops = [0] + stops + [d]
refills = 0
pos = 0
i = 0

while pos < d:
   last = pos
   while i + 1 < len(stops) and stops[i + 1] - last <= m:
       i += 1
   if stops[i] == pos:
       refills = -1
       break
   pos = stops[i]
   if pos < d:
       refills += 1

print(refills)
