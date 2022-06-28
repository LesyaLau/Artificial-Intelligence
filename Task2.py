initial_list = [45, 87, 12, 65, 43, 9, 12, 10, 33]
print(f"initial list {initial_list}")
new_list = []
for i in range (1, len(initial_list)):
  if initial_list[i] > initial_list[i-1]:
    new_list.append(initial_list[i])
print(f"new list {new_list}")