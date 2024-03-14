# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2

def solution(nums):
    max_ones = 0
    index = 0
    while index < len(nums):
        if nums[index] == 1:
            consec_ones = 1
            index += 1
            while index < len(nums) and nums[index] == 1:
                consec_ones += 1
                index += 1
            if consec_ones > max_ones:
                max_ones = consec_ones
        index += 1
    return max_ones

def solution(nums):
    str_nums = ''.join([str(num) for num in nums])
    ones_groups = str_nums.split('0')
    consecutives = [len(ones) for ones in ones_groups]
    max_consec = max(consecutives)
    return max_consec

def solution(nums):
    return max([len(ones) for ones in ''.join([str(num) for num in nums]).split('0')])

