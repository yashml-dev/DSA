class Solution(object):
    @staticmethod
    def differenceOfSums(n, m):
        total_sum = n * (n + 1) // 2
        k = n // m
        sum_divisible_by_m = m * k * (k + 1) // 2
        return total_sum - 2 * sum_divisible_by_m

# Correct call using the class
print(Solution.differenceOfSums(10, 3))  # Output: 19

    
        

        