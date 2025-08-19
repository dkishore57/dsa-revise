def lower_bound(self, arr, target):
    low = 0
    high = len(arr) - 1
    ans = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def rowWithMax1s(self, arr):
    max_ones = 0
    ind = -1
    cols = len(arr[0])
    for i in range(len(arr)):
        ones = cols - self.lower_bound(arr[i], 1)

        if ones > max_ones:
            max_ones = ones
            ind = i
    return ind