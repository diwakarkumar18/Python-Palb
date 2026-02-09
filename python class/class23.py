#arr=[3,5,6,8,9]
#k = arr.pop()
#arr.insert(0,k)
#print(arr)

#given arr=(2,3,-8,7,-1,2,3)
#currunt sum index 0 first el=2 next ele 3 

def max_subarr_sum(arr):

 currunt_max=arr[0]
 maxsum=arr[0]
 for i in range (1,len(arr)):
    currunt_max=max(arr[i],currunt_max + arr[i])
    maxsum= max  (maxsum,currunt_max)
 return maxsum
arr=[2,3,-8,7,-1,2,3]
result=max_subarr_sum(arr)
print("array: {arr}")
print(result)
