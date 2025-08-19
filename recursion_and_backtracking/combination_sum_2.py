def combinationSum2(candidates, target):
        candidates.sort()
        def cs1(ind,arr,target,ds,ans):
            if target==0:
                ans.append(ds[:])
                return
            for i in range(ind,len(arr)):
                if i>ind and arr[i]==arr[i-1]:
                    continue
                if arr[i]>target:
                    break
                ds.append(arr[i])
                cs1(i+1,arr,target-arr[i],ds,ans)
                ds.pop()       
        ans=[]
        cs1(0,candidates,target,[],ans)
        return ans
print(combinationSum2([10,1,2,7,6,1,5], 8))  # Example usage

