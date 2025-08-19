def how_many_times_rotated(arr):
    low=0
    high=len(arr) - 1
    ans=float('inf')
    ind=-1
    while low <= high:
        mid=(low + high) // 2
        if arr[low]<=arr[mid]:
            if ans > arr[low]:
                ans = arr[low]
                ind = low
            low=mid + 1
        else:   
            if ans > arr[mid]:
                ans = arr[mid]
                ind = mid
            high=mid - 1
    return ind
arr=[4,5,6,7,8,0,1,2]
print(how_many_times_rotated(arr))