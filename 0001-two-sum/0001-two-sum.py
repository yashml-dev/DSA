class Solution(object):
    def twoSum(self, nums, target):
        hashmap= {}
        for i, num in enumerate(nums):
            need = target - num
            if need in hashmap:
                return[hashmap[need], i]
            hashmap[num] = i
        
        