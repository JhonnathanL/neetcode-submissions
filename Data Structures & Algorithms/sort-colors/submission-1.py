class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zeros = nums.count(0)
        ones = nums.count(1)
        twos = nums.count(2)

        nums[:] = [0] * zeros + [1] * ones + [2] * twos
