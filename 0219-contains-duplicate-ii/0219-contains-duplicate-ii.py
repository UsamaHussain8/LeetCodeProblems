class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq_counter = {}

        for idx, val in enumerate(nums):
            if val in freq_counter:
                if idx - freq_counter[val] <= k:
                    return True
            freq_counter[val] = idx

        return False