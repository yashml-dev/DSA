class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total_sum = sum(nums)
        cur_max = nums[0]
        max_sum = nums[0]

        cur_min = nums[0]
        min_sum = nums[0]

        for i in range(1, len(nums)):
            cur_max = max(nums[i], cur_max + nums[i])
            max_sum = max(max_sum, cur_max)

            cur_min = min(nums[i], cur_min + nums[i])
            min_sum = min(min_sum, cur_min)

        if max_sum < 0:
            return max_sum

        circular_sum = total_sum - min_sum
        return max( max_sum, circular_sum)

        