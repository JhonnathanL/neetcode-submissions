class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = (nums1 + nums2)
        array.sort()

        if len(array) % 2 == 1:
            return array[len(array)//2]
        else:
            return (array[(len(array)//2)] + array[(len(array)//2) - 1]) / 2