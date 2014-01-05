def fib(n):
  
	if n == 0 : print 'The fibanocci number is : 0'
	else:
		x, y = 0, 1
		i = 0
		while( i < n ):
			x, y = y, x + y
			 
			i = i + 1		
		print ' The fibanocci number is :', x 
	


fib(3)