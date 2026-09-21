RANKS = '6789TJQKA'

data = input().split()
n, m, trump = int(data[0]), int(data[1]), data[2]
hand = input().split()
attack = input().split()

used = [False] * n


def beats(c, x):
   if x[1] == trump:
       return c[1] == trump and RANKS.index(c[0]) > RANKS.index(x[0])
   if c[1] == x[1]:
       return RANKS.index(c[0]) > RANKS.index(x[0])
   return c[1] == trump


def solve(i):
   if i == m:
       return True
   for j in range(n):
       if not used[j] and beats(hand[j], attack[i]):
           used[j] = True
           if solve(i + 1):
               return True
           used[j] = False
   return False


if solve(0):
   print("YES")
else:
   print("NO")
