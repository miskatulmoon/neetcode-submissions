"""
brute force solution o(n^2):
for each position in the array, count how many consecutive ones start from that pos.
then scan forward until we hit a 0 or the end of the array
then track the max count seen.

1. initialize maxCount to zero
2. for each starting index i:
    - initialize cunter count to zero
    - scan forward from i while the current elm is 1, increment the counter
    - stop when encountering a 0 or reaching the end
    - update maxCount with the max(maxCount, count)
    - return maxCount
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0

        for i in range(len(nums)):
            count = 0
            for j in range(i,len(nums)):
                if nums[j] == 0:
                    break
                count += 1
            maxCount = max(maxCount, count)

        return maxCount
