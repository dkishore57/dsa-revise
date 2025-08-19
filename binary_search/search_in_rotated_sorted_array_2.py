def search(arr,target):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==target):
            return mid
        if(arr[low]==arr[mid] and arr[mid]==arr[high]):
            low += 1
            high -= 1
            continue
      
        if(arr[low]<=arr[mid]):
            if(arr[low]<=target and arr[mid]>=target):
                high=mid-1
            else:
                low=mid+1
        else:
            if(arr[mid]<=target and target<=arr[high]):
                low=mid+1
            else:
                high=mid-1
    return -1
arr=[4,4,4,4,4,5,6,7,0,0,0,1,2]
print(search(arr,2))
