class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        trail_length = len(gain)
        altitudes: int = [0] * (trail_length + 1)
        altitudes[0] = 0

        for i in range(0, trail_length):
            altitudes[i + 1] = altitudes[i] + gain[i]

        return max(altitudes)