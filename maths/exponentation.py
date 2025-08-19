def exp(n,x):
    ans=1
    if x==0:
        return 1
    while(x>0):
        if x%2==1:
            ans=ans*n
            x-=1
        else:
            x=x//2
            n=n*n
    return ans
print(exp(201,42))  
