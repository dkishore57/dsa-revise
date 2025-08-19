def peak_element(arr):
    low = 0
    high = len(arr) - 1
    if len(arr)==1:
        return arr[0]
    if arr[0]>arr[1]:
        return arr[0]
    if arr[len(arr)-1]>arr[len(arr)-2]:
        return arr[len(arr)-1]
    low=1
    high=len(arr)-2
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]):
            return arr[mid]
        elif arr[mid]>arr[mid+1]:
            high=mid-1
        else:
            low=mid+1
    return -1
arr=[1,2,3,4,9,5,6,7,8,9,0,10,2]
print(peak_element(arr))