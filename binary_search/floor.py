def floor(arr,target):
    low=0
    high=len(arr)-1
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]<=target:
            ans=arr[mid]
            low=mid+1
        else:
            high=mid-1
    return ans
arr=[1,4,67,100,999,1000,10023,2025,7890]
print(floor(arr,90))
    