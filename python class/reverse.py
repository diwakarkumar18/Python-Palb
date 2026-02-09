def reverse_array(arr):
   
    start = 0
    end = len(arr) - 1
   
    while start<end:
       
       arr[start], arr[end] = arr[end], arr[start]
       start += 1
       end -= 1
    return arr
#example usage
arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)








#find the kth smallest element in an array
#union of two arrays
#largest element of array return it