def combination_sum(ind,arr,ds,ans,target):
    if ind>=len(arr):
        if target==0:
            ans.append(ds[:])
        return
    if arr[ind]<=target:
        ds.append(arr[ind])
        combination_sum(ind, arr, ds, ans, target - arr[ind])
        ds.pop()
    combination_sum(ind+1, arr, ds, ans, target)
ans=[]
n=3     
arr=[1, 2, 3]
target= 3  
combination_sum(0, arr, [], ans, target)
print(ans)