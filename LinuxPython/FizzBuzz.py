def FizzBuzz(num):


		if num % 3 == 0 and num % 5 == 0:
			return 'FizzBuzz'
		elif num % 3 == 0:
			return 'Fizz'
		elif num % 5 == 0:
			return 'Buzz'
		else:
			return str(num)

#for n in range (101):
#	print(FizzBuzz(n))
print('\n'.join(FizzBuzz(num) for num in range(0, 101) ))
