yearInput=input('Please enter a year: ')
listOutput = []
year=input('Enter year:')
l = []


try:
    with open('measles.txt', 'r') as fileRead:
        for lines in fileRead:
         with open('measles.txt', 'r') as f:
            for lines in f:
             line = lines.split()
            if line:
                if yearInput in ["ALL", 'all', '']: #If User asks for all the years
                    listOutput.append(lines)
                elif line[4].startswith(yearInput): #If the user enters a specific year
                    listOutput.append(lines)
                if year in ["ALL", 'all', '']:
                    l.append(lines)
                elif line[4].startswith(year):
                    l.append(lines)

except IOError:
     print('Could not read file, File doesnt exist!!')

if listOutput:
    file = input("Enter name of file in which data will be written: ")
    with open(file,'w') as fileRead:
        for lines in listOutput:
            fileRead.write(lines)
    print('Could not read file')
if l:
    file=input("Enter name of file in which data will be written: ")
    with open(file,'w') as f:
        for lines in l:
            f.write(lines)
else:
    print('No data to write')
