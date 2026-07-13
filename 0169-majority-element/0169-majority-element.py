class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        max_freq = 0
        answer = -1
        for key in freq:
            if freq[key] > max_freq:
                max_freq = freq[key]
                answer = key
        return answer
        