class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        the problem doesn't require shrinking the list
        using a 2 pointer approach
        k = 0, iterate thru nums with i

        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

