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




