class Solution:
    def nextGreaterElements(self, nums):

        n = len(nums)

        stack = []

        answer = [-1] * n

        # Traverse twice from right to left
        for i in range(2 * n - 1, -1, -1):

            current = nums[i % n]

            # Remove useless elements
            while stack and current >= stack[-1]:
                stack.pop()

            # Store answer only during the second pass
            if i < n:
                if stack:
                    answer[i] = stack[-1]

            # Push current element
            stack.append(current)

        return answer
        