num_list = []

num = input('Please enter a number: ')

while num != 'done' and num != 'DONE':
    try:
        num_list.append(int(num))
        num = input('Please enter a number: ')
    except:
        num = input("Not a number. Please enter a number Or 'done' to finish: ")

try:
    print('Maximum number: ', max(num_list))        
    print('Minimum number: ', min(num_list))
except:
    print('NO INPUT!')
    