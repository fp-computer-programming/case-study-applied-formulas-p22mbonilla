# Author MB 10/12/2021

first_investment = int(input("principal investment: "))
annual_rate = int(input("annual interest rate: "))
n = 12
time = int(input("amount of time the money is invested: "))

future_value = first_investment * (1 + (annual_rate / n) ** n * time)

future_value = float(future_value)

print(future_value)
