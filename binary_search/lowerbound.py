#lower bound means the smallest index greter than or equal to the target value
def lower_bound(arr, target):
    low=0
    high=len(arr)-1
    ans=len(arr)
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>=target):
            high=mid-1
            ans=mid
        else:
            low=mid+1
    return ans
#arr=[1,4,67,100,999,1000,10023,2025,7890]
arr=[0,1,1,1]

print(lower_bound(arr,1))