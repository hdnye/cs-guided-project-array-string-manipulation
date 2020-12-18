"""
You are given a non-empty array that represents the digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""
def plus_one(digits):
    # Your code here    
    # convert to string 
    j = [str(i) for i in digits]
    # join stmt to remove commas & brackets, turn into integer
    result = int(''.join(j))
    # increment the int by 1
    sum_one = result + 1    
    # convert back to list
    new_digit = [int(i) for i in str(sum_one)]
    return new_digit
     

digits = [1, 3, 2]
digits = [9, 9, 9]
print(plus_one([1, 3, 2]))
print(plus_one([9, 9, 9]))
