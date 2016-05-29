'''
Taking advantage of the fact that multiples of 3 and 5 are 2 artihmetic progressions.
Giving a runtime of O(1)
'''


for i in range(input()):
    num = input()

    result = 0

    # formula for determining sum of multiples is derived
    # from the sum of an arithmetic progression

    # add sum of multiples of 3
    result += ((num - 1)/3 + 1) * ((num - 1) / 3 * 3) / 2
    # add sum of multiples of 5
    result += ((num - 1)/5 + 1) * ((num - 1) / 5 * 5) / 2
    # multiples of 15 are included twice and therefore need to removed once
    result -= ((num - 1)/15 + 1) * ((num - 1) / 15 * 15) / 2

    print result
