# find the midian of an given array
def find_median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        median = (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        median = arr[n//2]
    return median 
arr = [3, 1, 4, 2, 5]
median = find_median(arr)
print(median)

#store matrix element in an array 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
array = []
top = 0
bottom = len(matrix) - 1
left = 0
right = len(matrix[0]) - 1
while top <= bottom and left <= right:
    for i in range(left,right+1):
        array.append(matrix[top][i])
    top +=1
    for j in range(top,bottom+1):
        array.append(matrix[j][right])
    right -=1
    for i in range(right,left-1,-1):
        array.append(matrix[bottom][i])
    bottom -=1
    for j in range(bottom,top-1,-1):
        array.append(matrix[j][left])
    left +=1
print(array)
