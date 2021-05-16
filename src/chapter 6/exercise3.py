def counter(s, l):
  string = str(s)
  letter = str(l)
  count = 0
  for thing in string: 
    if thing == letter :
      count = count + 1
  print(count)


counter ('banana', 'a')

counter ('payal', 'p')
