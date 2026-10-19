class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        
        if not target:
            return []
        nums.sort()
        return [i for i in range(len(nums)) if nums[i] == target]