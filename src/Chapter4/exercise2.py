def investment(c, r, n, t):
    val_of_investment = c * (1 + ((r / 100) / n)) ** t
    return val_of_investment


money = float(input('Enter your initial investment: '))
rate = float(input('Enter the rate per year in %: '))
time = int(input('Enter the years of the investment: '))
times_per_year = int(input('Enter the times interest is compounded in a year: '))

amount = investment(money, rate, times_per_year, time)
print(f'Final Value of Investments is: {amount:.2f}.')
