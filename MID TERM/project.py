
#calculation for the differance
def diff_check(begin, end):
    if end >= begin:
        units = end - begin
    else:
        units = (1000000000 - begin) + end
    return units

#calculation for residential customer
def residential(galon_units):
    galon_units = galon_units / 10
    total = 5.00 + (0.0005 * galon_units)
    return total

#calculation for commercial customer
def commercial(galon_units):
    galon_units = galon_units / 10
    if galon_units <= 4000000:
        total = 1000.00
    else:
        total = 1000 + (0.00025 * galon_units)    
    return total        

#calculation for industrial customer
def industrial(galon_units):
    galon_units = galon_units / 10
    if galon_units <= 4000000:
        total = 1000.00
    elif galon_units > 4000000 and galon_units <= 10000000: 
        total = 2000.00    
    else:
        total = 2000.00 + (0.000025 * galon_units)
    
    return total    


def main():
    while True:
        user_code = input("ENTER CUSTOMER CODE: ").lower()
        if user_code in ['r', 'c', 'i']:
            start_units = int(input("ENTER BEGINNING METRE READING: "))
            end_units = int(input("ENTER ENDING METRE READING: "))
            diff_units = diff_check(start_units, end_units) #calculates difference of the units
            if user_code == 'r':
                cost_of_Units = residential(diff_units)
            elif user_code == 'c':
                cost_of_Units = commercial(diff_units)
            elif user_code == 'i':
                cost_of_Units = industrial(diff_units) 
        else:
            break
        
        
        print('\n\n')
        print(f'Customer code: {user_code}')
        print(f'Beginning metre reading: {start_units}')
        print(f'Ending metre reading: {end_units}')
        print(f'Galons of water used: {diff_units/10}')
        print(f'Amount billed: ${cost_of_Units:.2f}')


main()
