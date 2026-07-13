class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        last_seen = {}
        for i, num in enumerate(nums):
            if num in last_seen:
                distance = i - last_seen[num]
                if distance <= k:
                    return True
            last_seen[num] = i
        return False
        