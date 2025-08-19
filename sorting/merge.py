def merge_sort(low,high,arr):
    mid=(low+high)//2
    if(low>=high):
        return
    merge_sort(0,mid,arr)
    merge_sort(mid+1,high,arr)
    merge(low,mid,high,arr)


def merge(low,mid,high,arr):
    left=low
    right=mid+1
    temp=[]
    while(left<=mid and right<=high):
        if(arr[left]<arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while(left<=mid):
        temp.append(arr[left])
        left+=1
    while(right<=high):
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]

arr=[1,23,90,0,7,6,34,19]
merge_sort(0,len(arr)-1,arr)
print(arr)





    

