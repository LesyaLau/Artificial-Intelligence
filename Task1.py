def salary_calc():
    hours = float(input("количество отработанных часов : "))
    wage = float(input("сумма оплаты труда за 1 час : "))
    bonus = float(input("размер премии - "))
    salary = hours*wage+bonus
    return salary
print(f"Размер заработной платы составил: {salary_calc() }")