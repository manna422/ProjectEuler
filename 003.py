'''
finding the largest prime number

stategy, continually divide by the smallest possible number.
if the number we are dividing by is larger that the square root of the n,
we have already exhausted the list of possible factors
'''

tests = input()
for i in xrange(tests):
    n = input()
    j = 2
    result = n
    while j**2 <= n:
        while n % j == 0:
            n = n / j
            result = max(n, j)
        j += 1
    print result
