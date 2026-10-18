class Solution:
    from math import comb
    from typing import List
    def numOfWays(self, nums: list[int]) -> int:
        def f(nums):
            if len(nums) <= 2:
                return 1

            left = [i for i in nums if i < nums[0]]
            right = [i for i in nums if i > nums[0]]

            return comb(len(left) + len(right) , len(right)) * f(left) * f(right)
        return (f(nums) - 1) % (10**9 + 7)


        