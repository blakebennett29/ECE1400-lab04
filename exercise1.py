"""
Exercise 1
Blake Bennett
"""

def prime_numbers(n):
    """Returns a set of prime numbers below n."""
    primes = set()
    for num in range(2, n):
        is_prime = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(num)
    return primes

def Fibonacci_sequence(n):
    """Returns a set of Fibonacci integers below n."""
    fibs = set()
    a, b = 0, 1
    while a < n:
        fibs.add(a)
        a, b = b, a + b
    return fibs

def Print_intersection(n):
    """Prints the intersection of prime numbers and Fibonacci integers below n."""
    primes = prime_numbers(n)
    fibs = Fibonacci_sequence(n)
    intersection = primes.intersection(fibs)
    print(intersection)
    
if __name__ == "__main__":
    n = 100
    Print_intersection(n)