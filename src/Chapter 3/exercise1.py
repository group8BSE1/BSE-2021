#the hourly rate for hours worked above 40 hours.
hours = float(input('Enter Hours:'))
rate = float(input('Enter Rate:'))

if hours <= 40:
  pay = hours * rate
else:
  pay = ((hours - 40) * (1.5 * rate)) + (40 * rate)

print ('Pay =', pay)
