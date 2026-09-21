class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def quick_sort(nums):
            if len(nums) <= 1:
                return nums

            pivot = nums[-1]

            left = []
            right = []

            for n in nums[:-1]:
                if n < pivot:
                    left.append(n)
                else:
                    right.append(n)

            return quick_sort(left) + [pivot] + quick_sort(right)

        nums[:] = quick_sort(nums)
