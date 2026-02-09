def smallest_subarray(arr,x):
    n=len(arr)
    current_num=0
    left=0
    num_lenght=n+1
    for right in range(n):
       current_num +=arr[right]
    while current_num>x:
       minimum_len=min(num_lenght,right-left+1)
       current_num -=arr[left]
       left +=1
    return minimum_len if minimum_len != n+1 else -1    #! use for not equal to n+1
arr=[1,10,5]
x=11
result=smallest_subarray(arr,x)
print("smallest subarray length is:",result)  


#no of choclate in packets each no of choclate  there are m student tast is to destribute among student such that 1 each student get one packet and 2 the diff between max and min no of choclate is minumum and return that min possible diff
def choclate_packet(arr,m):
    n=len(arr)
    if m==0 or n==0:
        return 0
    arr.sort()
    if n<m:
        return -1
    min_diff=float('inf')
    for i in range(n-m+1):
        diff=arr[i+m-1]-arr[i]
        min_diff=min(min_diff,diff)
    return min_diff
arr=[3,4,1,9,56,7,9,12]
m=5
result=choclate_packet(arr,m)
print("minimum difference is:",result)

