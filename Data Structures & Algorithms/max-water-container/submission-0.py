class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0

        l,r = 0, (len(heights)-1)

        while(l<r):
            hl = heights[l]
            hr = heights[r]
            cur = min(hl, hr) * (r-l)
            maxA = max(cur, maxA)

            # print(f"l: {l}, {hl} - r: {r}, {hr} -- w: {r-l+1}")
            if hr > hl:
                l += 1
            else:
                r -= 1

        return maxA