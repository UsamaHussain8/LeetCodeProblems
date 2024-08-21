class Solution:
    def hIndex(self, citations: List[int]) -> int:
        num_papers = len(citations)
        citations.sort()
        for idx, val in enumerate(citations):
            if val >= num_papers - idx:
                return num_papers - idx
        return 0    