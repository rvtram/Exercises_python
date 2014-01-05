a = list(raw_input('Enter list of numbers: '))
print 'So the given list is :', a
n = len(a)

i = 0
y = 0

while (i < n):
  sum_x = y + int(a[i])
  y = sum_x  
  i = i + 1

print 'Sum of numbers in the given list is:', sum_x
