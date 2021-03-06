'''
PROBLEM 20:

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

'''


def run():
    large_number = 1
    sum = 0
    for i in range(100):
        large_number *= (i+1)
    str_num = str(large_number)
    for x in str_num:
        sum += int(x)
    print("The sum of the digits is: {}".format(sum))


if __name__ == '__main__':
    run()
