def isPrime(n):
    if n<2:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        else:
            return True

print isPrime(9)
