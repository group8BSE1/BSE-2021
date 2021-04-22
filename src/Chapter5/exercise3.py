#Global variables of stock coins
nickels = 25
dimes = 25
quarters = 25
one_dollar = 0
five_dollar = 0
#Global variables of stock coins

#Function to print the Menu
def menu_message():
    print('MENU FOR DEPOSITS')
    print('n -- deposit a nickel')
    print('d -- deposit a dime')
    print('q -- deposit a quarter')
    print('o -- deposit a one dollar bill')
    print('f -- deposit a five dollar bill')
    print('c -- caancel the deposit')

#Function prints the current stock value
def stock_contains(n_value, d_value, q_value, o_value, f_value):
    print(f'{n_value} -- nickels')
    print(f'{d_value} -- dimes')
    print(f'{q_value} -- quarter')
    print(f'{o_value} -- one dollar bill')
    print(f'{f_value} -- five dollar bill')


print('WELCOME TO THE VENDING CHANGE MACHINE!\n')
print('CURRENT STOCK CONTAINS>\n')
stock_contains(nickels, dimes, quarters, one_dollar, five_dollar)