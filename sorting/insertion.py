arr=[1,23,90,0,7,6,34,19]
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        temp=arr[i]
        while(j>=0 and temp<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
    return arr
print(insertion_sort(arr))

