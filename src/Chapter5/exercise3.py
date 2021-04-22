#Global variables of stock coins
nickels = 25
dimes = 25
quarters = 25
one_dollar = 0
five_dollar = 0
#Global variables of stock coins

g_money_toPay = 0
g_cents_toPayConverted = 0

#denminations counter global
g_nickles_count = 0
g_dimes_count = 0
g_quarters_count = 0
g_ones_count = 0
g_five_count = 0 
#denminations counter global

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

#function to update the stock of coins 
def updateStock(upDate_nickles, upDate_dimes, upDate_quarters, upDate_oneDollar, upDate_fiveDollar):
    #using global keyword to change a global variable
    global nickels
    global dimes
    global quarters
    global one_dollar
    global five_dollar

    #assigning the stock new values
    nickels = nickels + upDate_nickles
    dimes = dimes + upDate_dimes
    quarters = quarters + upDate_quarters
    one_dollar = one_dollar + upDate_oneDollar
    five_dollar = five_dollar + upDate_fiveDollar


print('WELCOME TO THE VENDING CHANGE MACHINE!\n')
print('CURRENT STOCK CONTAINS>\n')
stock_contains(nickels, dimes, quarters, one_dollar, five_dollar)