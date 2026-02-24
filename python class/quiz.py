#question 1
print(sum(range(1,6)))

#question 2-1

N = -1
S = 0

while N < 99:
    N = N + 2
    S = S + N

print(S)


#question 2-2

print("Enter an integer: ")
n = int(input())

if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")


#question 3-1

print("*" * 30)
print("# " * 15)    

#question 4=1

name="David Don"
address="1600 Wilshire Blvd #205, Los Angeles CA 90017"
print(name)
print(address)

#question 5-1

x=1
y=0
print(x and y)
print(x or y)
print(not x)
print(not y)

#question 6-1 

 # Take two integers as input
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

# Compare and print from smallest to largest
if num1 < num2:
    print(num1, num2)
else:
    print(num2, num1)

#question 7-1
 
  # Take inputs
adult = int(input("Are you an adult? (1 if you are an adult, 0 if you are minor): "))
married = int(input("Are you married? (1 if you are married, 0 if you are single): "))

# Compound condition
if adult == 1 and married == 1:
    print("You are an adult who is married.")
elif adult == 1 and married == 0:
    print("You are an adult who is single.")
elif adult == 0 and married == 1:
    print("You are a minor who is married.")
else:
    print("You are a minor who is single.")


#question 8-1
for num in range(2, 13):  # Numbers from 2 to 12
    is_prime = True
    
    for i in range(2, num):  # Inner loop to check divisibility
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, ": Prime number")
    else:
        print(num, ": Composite number")    


#question 9-1

print("Three-digit Armstrong numbers:", end=" ")

for num in range(100, 1000):
    # Extract digits
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10
    
    # Check Armstrong condition
    if num == hundreds**3 + tens**3 + ones**3:
        print(num, end=" ")        

#question 10-1

l1 = ['I like', 'I love']
l2 = ['pancake.', 'kiwi juice.', 'espresso.']

for first in l1:
    for second in l2:
        print(first, second)

#question 11-1

person ={'Name': 'David Doe', 'Age': 26, 'Weight': 82, 'Job': 'Data scientist', 'Father': 'John Doe'}
print (person)


#question 12-1

lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]

# Find index of largest value
max_index = 0
for i in range(len(lst)):
    if lst[i] > lst[max_index]:
        max_index = i

# Swap largest value with last element (tuple swapping)
lst[max_index], lst[-1] = lst[-1], lst[max_index]

print(lst)


#question 13-1

a = [[1, 2], [3, 4], [5, 6]]

# New one-dimensional list
new_list = []

# Using nested for loop
for row in a:
    for element in row:
        new_list.append(element)

print(new_list)



#question 14-1


maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

# Calculate average
average = sum(maria.values()) / len(maria)

print(average)


#question 15-1

import copy

school = {
    'kim': {'age': 16, 'hei': 170, 'grade': 3},
    'lee': {'age': 15, 'hei': 168, 'grade': 2},
    'choi': {'age': 14, 'hei': 173, 'grade': 1}
}

# Deep copy
school2 = copy.deepcopy(school)

# Check if they are the same object
print(school is school2)


#question 16-1

scores = (('Hyun', 88, 95, 90),
          ('Kang', 85, 90, 95),
          ('Park', 70, 90, 80),
          ('Hong', 90, 90, 95))

# Unpack using zip
names, english, math, science = zip(*scores)

# Calculate average of math scores
average_math = sum(math) / len(math)

print(average_math)