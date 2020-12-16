"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
# def pivot_index(nums):
#     # Your code here
#     # iterate through array
#     for i in range(len(nums)):
#         # check if current index is the pivot        
#         left_sub = nums[:i]        
#         right_sub = nums[i+1:]
#         # get sum of both subarrays & compare
#         left_sum = sum(left_sub)
#         right_sum = sum(right_sub)        
#         # if equal return i
#         if left_sum == right_sum:
#             return i
# # ^^ O(n^2)
# # more optimal solution O(n)

# def pivot_index(nums):
#     l_sum = 0
#     r_sum = sum(nums[1:])

#     # iterate array & check if i is pivot
#     for i in range(len(nums)):
#         if l_sum == r_sum:
#             return i
#         # add # at cur index to l_sum 
#         l_sum += nums[i]
#         # check we're not at last index
#         if (i+1 == len(nums)):
#             r_sum = 0
#         # remove left sum from right sum. this avoids running the sum loop from above repeatedly
#         else:
#             r_sum -= nums[i+1]

#     return -1

# Optimal solution
def pivot_index(nums):
    total_sum = sum(nums)
    l_sum = 0

    for i in range(len(nums)):
        r_sum = total_sum - l_sum - nums[i]
        if l_sum == r_sum:
            return i
        l_sum += nums[i]
    return -1



print(pivot_index([1,7,3,6,5,6]))
print(pivot_index([1,7,3]))
    
'''
    input = array of ints
    output = return a number (an index)
    Plan: search through arary find the pivot index
    is I a pivot index/ 
    get sum of left subarray
    get sum of right subarray
    compare
    pseudo:
    if true
        - return index(i)
    if false
        - keep looping
'''
