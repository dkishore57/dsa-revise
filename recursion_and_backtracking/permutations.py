def permutations(ind,nums,ds,ans,freq):
    if ind==len(nums):
        ans.append(ds[:])
        return
    for i in range(len(nums)):
        if not freq[i]:
            ds.append(nums[i])
            freq[i] = True
            permutations(ind+1,nums,ds,ans,freq)
            ds.pop()
            freq[i] = False
def permute(nums):
    ans = []
    ds = []
    freq = [False] * len(nums)
    permutations(0,nums,ds,ans,freq)
    return ans
print(permute([1, 2, 3]))