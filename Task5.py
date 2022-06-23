my_list = input('введите числа через пробел ').split()
list1 = list(map(float, my_list))
def sum_list(list1):
  return(sum(list1))
print(sum_list(list1))