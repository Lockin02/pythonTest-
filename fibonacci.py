def fib(max):
	n,a,b = 0,1,1
	while n<max:
		print(b)
		a,b = b,a+b
		n = n+1
	return 'Done'

fib(6)