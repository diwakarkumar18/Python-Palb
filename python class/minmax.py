arr=[1,3,4,5,7,3,]
max=max(arr)

min=min(arr)
for i in range (1,len(arr)):
    if arr[i]>max:
        max=arr[i]
    if arr[i]<min:
        min=arr[i]
print(max)
print(min)

