import time
def is_prime(num):

	for i in range(2, num):
		if num % i == 0:
			return  False
	else:
		return True

def get_prime(num):
	cont = 0
	for j in range(2,num):
		if is_prime(j):
			cont += 1
			#print(j)
		if cont == 10001:
			break
	return j
t0 = time.time()
print(get_prime(20))
print(time.time() - t0)
