name = input("имя ")
surname = input("фамилия ")
birthyear = input("год рождения ")
city = input("город проживания ")
email = input("email ")
phone = input("телефон19 ")

def personal_data(**kwargs):
  return kwargs
print(personal_data(имя=name, фамилия=surname, год_рождения=birthyear, город_проживания=city, email=email, телефон=phone))