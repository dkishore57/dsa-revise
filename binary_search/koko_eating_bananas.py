import math
def hrs(x,piles):
    req=0
    for i in range(len(piles)):
        req+=math.ceil(piles[i]/x)
    return req
def minEatingSpeed(piles, h) :
    low=1
    high=max(piles)
    ans=0
    while(low<=high):
        mid=(low+high)//2
        if(hrs(mid,piles)<=h):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))