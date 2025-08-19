def subsequence_sum(arr,ind,ds,scum,ans,target):
    if ind>=len(arr):
        if scum==target:
            ans.append(ds[:])
            return True
        return False
    ds.append(arr[ind])
    scum+= arr[ind]
    if subsequence_sum(arr, ind+1, ds, scum, ans, target):
        return True
    ds.pop()    
    scum-= arr[ind]
    if subsequence_sum(arr, ind+1, ds, scum, ans, target):
        return True
    return False
ans=[]
n = 3
arr = [1, 2, 3] 
target = 3
subsequence_sum(arr, 0, [], 0, ans, target)
print(ans)