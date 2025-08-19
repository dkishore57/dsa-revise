#upper bound means the smallest index greter than the target value
def upper_bound(arr, target):
    low=0
    high=len(arr)-1
    ans=len(arr)
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>target):
            high=mid-1
            ans=mid
        else:
            low=mid+1
    return ans
arr=[0,0,1,1]
print(upper_bound(arr,0))