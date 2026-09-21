RANKS = '6789TJQKA'

data = input().split()
n, m, trump = int(data[0]), int(data[1]), data[2]
hand = input().split()
attack = input().split()

def beats(c, x):
   if x[1] == trump:
       return c[1] == trump and RANKS.index(c[0]) > RANKS.index(x[0])
   if c[1] == x[1]:
       return RANKS.index(c[0]) > RANKS.index(x[0])
   return c[1] == trump

start = tuple([False] * m)
goal = tuple([True] * m)
states = {start}

for card in hand:
   new_states = set(states)
   for st in states:
       for i in range(m):
           if not st[i] and beats(card, attack[i]):
               nxt = list(st)
               nxt[i] = True
               new_states.add(tuple(nxt))
   states = new_states

if goal in states:
   print("YES")
else:
   print("NO")
