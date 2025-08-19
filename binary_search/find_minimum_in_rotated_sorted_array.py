def find_min(arr):
    low=1
    high=len(arr) - 1
    ans=arr[0]  
    while low <= high:
        mid=(low + high) // 2
        if arr[low]<=arr[mid]:
            ans=min(ans, arr[low])
            low=mid + 1
        else:
            ans=min(ans, arr[mid])
            high=mid - 1
    return ans
arr=[4,5,6,7,-1,0,1,2]
print(find_min(arr))