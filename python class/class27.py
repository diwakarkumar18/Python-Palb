def twosum(nums,target):
    n= len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]== target:
                 return[i,j]
    return[]
print(f"result:{twosum([3,2,4,],6)}") 


arr=[1,3,5,6,8,2,6,7,6,8,9]
n=len(arr)
max_reach =arr[0]
jumps=1
for i in range(1,n-1):
    max_reach=max(max_reach,i+arr[i])
    steps_left=1
    if steps_left==0:
        jumps+=1
        steps_left=max_reach-i
print("maximum jumps:",jumps)