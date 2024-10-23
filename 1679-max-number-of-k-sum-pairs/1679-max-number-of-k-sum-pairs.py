class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        index_store = {}
        num_pairs = 0
        for num in nums:
            complement = (k - num)
            if complement in nums and (num not in index_store and complement not in index_store):
                num_pairs += 1
                index_store[num] = complement

        return num_pairs