def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]<target):
            low=mid+1
        elif(arr[mid]>target):
            high=mid-1
        else:
            return mid
arr=[1,4,67,100,999,1000,10023,2025,7890]
print(binary_search(arr,100))


''' Search insert position is same as lower bound
    ceil of the array is same as lower bound
    first occurence is same as lower bound
    last occurence is same as upper bound-1
    count occurence is first occurence - last occurence + 1
'''
