def smallest_prime_factor(n):
    spf = [i for i in range(10**5 + 1)]
    for i in range(2, int((10**5)**0.5) + 1):
        if spf[i] == i:
            for j in range(i*i, 10**5 + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf[n]
print(smallest_prime_factor(91))