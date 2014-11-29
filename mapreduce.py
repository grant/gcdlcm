from fractions import gcd
from itertools import combinations
import ast

def lcm(*values):
  if len(values) == 1:
    values = values[0]
  values = set([abs(int(v)) for v in values])
  if values and 0 not in values:
    n = n0 = max(values)
    values.remove(n)
    while any( n % m for m in values ):
      n += n0
    return n
  return 0

def mgcd(*args):
  if len(args) == 1:
    args = args[0]
  if len(args) == 2:
    return gcd(args[0], args[1])
  else:
    return gcd(args[0], mgcd(args[1:]))

with open ("data.txt", "r") as myfile:
    data = myfile.read().replace('\n', '')

data = ast.literal_eval(data)

total = len(data)
gs = []
for t in data:
  gs.append(mgcd(t))
  print str(len(gs)) + "/" + str(total)

best = lcm(gs[0], gs[1])
for t in gs:
  best = lcm(best, t)
  print best