'''
PROBLEM 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''

def run():
	maximum = 1000
	sum = 0
	for x in range(maximum):
		if x % 3 == 0:
			sum += x
		elif x % 5 == 0:
			sum += x
	print("The Sum is {}".format(sum))


if __name__ == "__main__":
	run()