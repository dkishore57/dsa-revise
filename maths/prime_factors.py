def prime_factors(n):
    factors=[]
    for i in range(2, int(n**0.5) + 1):
        print(i,n)
        if n%i==0:
            factors.append(i)
            while n%i==0:
                n//=i
    if n!=1:
        factors.append(n)
    return factors
print(prime_factors(16))  