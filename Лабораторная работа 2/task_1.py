money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
increases = 1.05
money_have = True
month = 0
while money_have == True:
  if spend >= (money_capital + salary):
    money_have = False
  else:
    money_capital = money_capital + salary - spend
    month += 1
    spend *= increases

print("Количество месяцев, которое можно протянуть без долгов:", month)
