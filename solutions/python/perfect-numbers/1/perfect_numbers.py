import math 

def classify(n):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if n > 0 : 
        factors = set ()
        for i in range  (1, math.isqrt(n) + 1) : 
            if n % i == 0 : 
                factors.add (i) 
                factors.add(n // i)
        factors = sorted(list(factors))
        
        sum = 0
        for item in factors : 
            sum = sum + item 
        sum = sum - factors[-1]
        
        if sum == n : 
            return "perfect"
        elif sum > n : 
            return "abundant"
        elif sum < n : 
            return "deficient"
    raise ValueError ("Classification is only possible for positive integers.")
    