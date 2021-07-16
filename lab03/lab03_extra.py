""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    "give a positive integer n and m,count from 1 to m ,the number can be divided by n"
    def countzero(n,m):
        assert n >0 and m> 0 ,"n,m are positive"
        inc=0
        if m==1:
            return 1
        if n%m==0:
            inc=1
        return inc+countzero(n,m-1)
    if countzero(n,n) ==2:
        return True
    return  False

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if max(a,b)%min(a,b)==0:
        return  min(a,b)
    return gcd(min(a,b),max(a,b)%min(a,b))

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def countdigits(n,x):
        assert x <10 ,"x < 10"
        if n<10:
            if n == x:
                return 1
            return 0
        if n%10 == x:
            return 1+countdigits(n//10,x)
        return countdigits(n//10,x)

    if n<=10:
        return 0
    elif n<100:
        if n%10 + n//10 == 10:
            return 1
    if n%10 == 0:
        return ten_pairs(n//10)
    return ten_pairs(n//10)+countdigits(n//10,10-n%10)