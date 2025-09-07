def subsequence(ind,ds,ans,arr):
    if ind>=n:
        ans.append(ds[:])
        return
    ds.append(arr[ind])
    subsequence(ind+1,ds,ans,arr)
    ds.pop()
    subsequence(ind+1,ds,ans,arr)
n = 3
arr = [1, 2, 3] 
ans = []
subsequence(0, [], ans, arr)
ans.sort()
print(ans)