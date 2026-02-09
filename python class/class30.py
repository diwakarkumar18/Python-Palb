arr=[16,17,3,4,5,2]
def find_leaders(arr):
    n=len(arr)
    leaders=[]
    max_from_right=arr[n-1]
    leaders.append(max_from_right)
    for i in range(n-2,-1,-1):
        if arr[i]>max_from_right:
            max_from_right=arr[i]
            leaders.append(arr[i])
    leaders.reverse()
    return leaders
result=find_leaders(arr)
print("leaders=",result)   


#write a factirial of given number
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
print("enter a number to find factorial:")
number=int(input())
fact=factorial(number)
print("factorial of",number,"is",fact)
fact_digits = [int(digit) for digit in str(fact)]
print("digits of factorial:",fact_digits)

display_arr_element=[fact]
print("display array:",display_arr_element)
