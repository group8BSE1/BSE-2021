count = 0
sum = 0
user = input('Please enter a file name')
try: 
    fhand = open(user)
except:
    print("Not a valid file")
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
         print(lines)
         count += 1
         colon_position = int(line.find(":"))
         extract = line[colon_position+1:]
         number_extract = float(extract)
         sum += number_extract
print("Extracted lines", count)
print("Sum of confidence values", sum)
print("Average of confidence values", sum/count