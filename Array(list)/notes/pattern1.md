# PATTERN 1  - Array Traversal & Simulation

# concepts

Single traversal 
Nested traversal 
In-place modification 
Simulation


# single traversal

to visit every element exactly once

nums = [4,7,2,9,5]

for i in nums:
    print(i)

output
4
7
2
9
5

# time Complexity - O(n)

When to use:

Count
Find maximum
Find minimum
Sum elements
Check a condition
Update values

# eg
find max
nums = [5,8,2,9,4]

maximum = nums[0]

for num in nums:
    if num > maximum:
        maximum = num

print(maximum)



# NESTED TRAVERSAL

Now instead of one loop,

we have a loop inside another loop.

for i in range(n):

    for j in range(n):



First element

↓

check everything

Second element

↓

check everything

Third element

↓

check everything    

# EG
nums = [2,4,6]

Pairs

2 4

2 6

4 6

Code

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        print(nums[i], nums[j])

Output

2 4

2 6

4 6


# TIME COMPLEXITY - O(n^2)



# In-Place Modification

Instead of creating another array,
modify the original one

Original

[1,2,3]

Multiply every element by 2.

Instead of

new = []

for num in nums:
    new.append(num*2)

Do

for i in range(len(nums)):
    nums[i] *= 2

Creating another array
Extra memory
O(n)

Modifying original
Extra memory
O(1)    


