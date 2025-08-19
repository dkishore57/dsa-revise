def jumpgame3(arr,start):
    zero=False
    seen=set()
    def helper(start):
        if start<0 or start>=len(arr) or start in seen:
            return False
        if arr[start]==0:
            return True
        seen.add(start)
        return helper(start+arr[start]) or helper(start-arr[start])
