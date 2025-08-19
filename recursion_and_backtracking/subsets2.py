def sub2(ind,nums,ans,ds):
        ans.append(ds[:])
        for i in range(ind,len(nums)):
            if i>ind and nums[i]==nums[i-1]:
                continue
            ds.append(nums[i])
            sub2(i+1,nums,ans,ds)
            ds.pop()
def subsetsWithDup(nums):
    nums.sort()
    ans=[]
    ds=[]
    sub2(0,nums,ans,ds)
    return ans
print(subsetsWithDup([1, 2, 2]))  # Example usage
