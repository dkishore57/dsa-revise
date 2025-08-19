def subsets(nums):
        def subset_sum(ind,scum,nums,ans,ds):
            if ind>=len(nums):
                ans.append(ds[:])
                return
            ds.append(nums[ind])
            subset_sum(ind+1,scum+nums[ind],nums,ans,ds)
            ds.pop()
            subset_sum(ind+1,scum,nums,ans,ds)
        ans=[]
        subset_sum(0,0,nums,ans,[])
        ans.sort()
        return ans
arr=[1, 2, 3]
print(subsets(arr))  # Example usage
