

##A happy number is a number defined by the following process:
#
#- Starting with any positive integer, replace the number by the sum of the squares of its digits.
#- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 
#- Those numbers for which this process ends in are happy.
#Return TRUE if is a happy number, and FALSE if not.


def isHappyNumber(n):

    def sumDigits(number):
        totalSum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            totalSum += digit ** 2
        return totalSum

    slow = n
    fast = sumDigits(n)
    while fast != 1 and slow != fast:

        slow = sumDigits(slow)
        fast = sumDigits(sumDigits(fast))

    if fast == 1:
        return True
    return False


print(isHappyNumber(232421123))
    

    
