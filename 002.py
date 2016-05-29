'''
It's unavoidable to solve this without computing most of the fibonacci sequence.
To reduce the amount of brute-forcing used we can take advantage of the fact that
the fibonacci series follows a pattern of odd then odd then even and so on.
'''

tests = input()
for i in xrange(tests):
    n = input()
    result = 0
    x = 2
    y = 3
    while x < n:
        result += x
        x, y = x+(2*y), (2*x)+(3*y)
    print result
