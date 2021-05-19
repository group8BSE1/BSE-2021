def chop(list):
  del list[0]
  del list[len(list) -1]
  return None

print('Your inputs will be turned into a list. Type \'done\' when you are finished with your inputs')
list = []
cond = True
while cond == True:
  element = input('Please input whatever you want:')
  if element.lower() == 'done':
    break
  else:
    list.append(element)
chop(list)
print(list)