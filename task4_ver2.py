from random import random
list_a = []
for j in range(12):
  list_a.append(int(random()*10))
print(f"initial random list: {list_a}")
new_list_a = [el for el in list_a if list_a.count(el) == 1]
print(f"list without dublicates: {new_list_a}")