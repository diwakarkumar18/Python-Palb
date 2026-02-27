#find the number of each element from array and display the result in dictionary format
arr = ['x','x','x','a','a','b']
result = {}
for item in arr:
    result[item] = result.get(item, 0) + 1
print(result)

#with max frequency element
arr=['aman','akash','akash','ansh','ansh','ansh','akash']
result={}
for item in arr:
    result[item] = result.get(item, 0) + 1
print(result)
max_freq = max(result.values())
max_elements = [key for key, value in result.items() if value == max_freq]
print("Elements with maximum frequency:", max_elements)