def subsequence_sum(arr,ind,scum,target):
    if ind>=len(arr):
        if scum==target:
            return 1
        return 0
    scum+= arr[ind]
    left=subsequence_sum(arr, ind+1,  scum, target)
    scum-= arr[ind]
    right=subsequence_sum(arr, ind+1, scum, target)
    return left + right
ans=[]
n = 3
arr = [1, 2, 3 , 1] 
target = 3
print(subsequence_sum(arr, 0, 0, target))

