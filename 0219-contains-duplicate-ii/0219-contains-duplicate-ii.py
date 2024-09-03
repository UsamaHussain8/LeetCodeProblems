class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        elem_freq_counter = {}

        for idx, num in enumerate(nums):
            if num not in elem_freq_counter:
                elem_freq_counter[num] = []
            elem_freq_counter[num].append(idx)

        for key in elem_freq_counter.keys():
            indices = elem_freq_counter[key]
            if len(indices) > 1:
                for i in range(0, len(indices) - 1):
                    if indices[i + 1] - indices[i] <= k:
                        return True

        return False

