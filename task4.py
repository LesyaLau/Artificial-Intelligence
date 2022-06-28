from random import random
list_a = []
for j in range(12):
  list_a.append(int(random()*10))
print(f"initial random list: {list_a}")
new_list_a = []
for k in list_a:
  if list_a.count(k) == 1:
    new_list_a.append(k)
print(f"list without dublicates: {new_list_a}")
