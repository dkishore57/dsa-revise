def findKthPositive(arr, k):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        miss=arr[mid]-(mid+1)
        if miss<k:
            low=mid+1
        else:
            high=mid-1
    return low+k
# Example usage
arr = [2, 3, 4, 7, 11]  
k = 5
print(findKthPositive(arr, k))  # Output: 9
