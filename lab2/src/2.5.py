class Node:
   def __init__(self, key):
       self.key = key
       self.left = None
       self.right = None

def insert(node, x):
   if node is None:
       return Node(x)
   if x < node.key:
       node.left = insert(node.left, x)
   elif x > node.key:
       node.right = insert(node.right, x)
   return node

def delete(node, x):
   if node is None:
       return None
   if x < node.key:
       node.left = delete(node.left, x)
   elif x > node.key:
       node.right = delete(node.right, x)
   else:
       if node.left is None:
           return node.right
       if node.right is None:
           return node.left
       m = node.right
       while m.left is not None:
           m = m.left
       node.key = m.key
       node.right = delete(node.right, m.key)
   return node

def exists(node, x):
   while node is not None:
       if x == node.key:
           return True
       node = node.left if x < node.key else node.right
   return False

def next_key(node, x):
   res = None
   while node is not None:
       if node.key > x:
           res = node.key
           node = node.left
       else:
           node = node.right
   return res

def prev_key(node, x):
   res = None
   while node is not None:
       if node.key < x:
           res = node.key
           node = node.right
       else:
           node = node.left
   return res

import sys

root = None

for line in sys.stdin:
   parts = line.split()
   if not parts:
       continue
   op, x = parts[0], int(parts[1])
   if op == "insert":
       root = insert(root, x)
   elif op == "delete":
       root = delete(root, x)
   elif op == "exists":
       print("true" if exists(root, x) else "false")
   elif op == "next":
       r = next_key(root, x)
       print(r if r is not None else "none")
   elif op == "prev":
       r = prev_key(root, x)
       print(r if r is not None else "none")
