def square_root(n):
    if n<2:
        return n
    low=1
    high=n
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if mid*mid==n:
            return mid
        elif mid*mid<n:
            low=mid+1
            ans=mid
        else:
            high=mid-1
    return ans
print(square_root(15))