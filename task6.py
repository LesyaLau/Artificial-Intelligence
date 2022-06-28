from itertools import count

e = int(input("введите целое начальное число списка: "))
r = int(input("введите целое конечное число списка: "))

for el in count(e):
  if el > r:
    break
  else:
    print(el)

from itertools import cycle

t = 0

for el in cycle("lmn"):
  if t > 9:
    break
  print(el)
  t += 1
