#store the element in stack and traverse the array
stack = []
array = [1, 2, 3, 4, 5]

for element in array:
    stack.append(element)

while stack:
    print(stack.pop())

#find 123 pattern in an array
    def find132pattern(nums):
     third = float('-inf')
     stack = []
     for i in range(len(nums) - 1, -1, -1):
        if nums[i] < third:
           return True
        while stack and nums[i] > stack[-1]:
            third = stack.pop()
        stack.append(nums[i])
        
     return False
arr1 = [4, 7, 11, 5, 13, 2]
print(f"Input: {arr1} | Result: {find132pattern(arr1)}")