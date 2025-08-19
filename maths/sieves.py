def sieve(n):
    primes=[]
    is_prime=[1]*(n+1)
    is_prime[0]=is_prime[1]=0
    for i in range(2,int(n**0.5) + 1):
        if is_prime[i]==1:
            for j in range(i*i, n+1, i):
                is_prime[j]=0
    for i in range(n+1):
        if is_prime[i]==1:
            primes.append(i)
    return primes
print(sieve(1000))

