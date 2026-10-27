class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        setn1 = set(nums1)
        setn2 = set(nums2)


        diff = setn1 ^ setn2

        diff1 = []
        diff2 = []
        for i in diff:
            if i in setn1:
                diff1.append(i)
            else:
                diff2.append(i)

        return [diff1, diff2]
