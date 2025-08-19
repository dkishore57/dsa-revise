def searchMatrix(matrix, target):
    low=0;high=(len(matrix)*len(matrix[0]) - 1)
    while(low<=high):
        mid=(low+high)//2
        row=mid//len(matrix[0])
        col=mid%len(matrix[0])
        if(matrix[row][col]==target):
            return True
        elif(matrix[row][col]<target):
            low=mid+1
        else:
            high=mid-1
    return False
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 0
print(searchMatrix(matrix, target))  # Output: True

        