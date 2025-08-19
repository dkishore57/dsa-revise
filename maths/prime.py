def is_prime(n):
    if n <= 1:
        return False
    x=int(n**0.5) + 1
    for i in range(2,x):
        if n % i == 0:
            return False
    return True
print(is_prime(2))