def jump(nums):
    jumps=0
    l=0
    r=0
    while(r<len(nums)-1):
        farthest=0
        for i in range(l,r+1):
            farthest=max(farthest,i+nums[i])
        l=r+1
        r=farthest
        jumps+=1
    return jumps
print(jump([1,2,0,2,3,1,6]))

        