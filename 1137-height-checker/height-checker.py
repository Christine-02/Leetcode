class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        corheights = sorted(heights)
        count = 0

        for i in range(len(heights)):
            if heights[i] != corheights[i]:
                count += 1

        return count