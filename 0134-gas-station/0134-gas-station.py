class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cyclic_index: int = -1
        if sum(gas) < sum(cost):
            return cyclic_index

        starting_station: int = 0
        num_stations: int = len(gas)
        gas_in_tank: int = 0

        for i in range(0, num_stations):
            gas_in_tank += gas[i] - cost[i]
            if gas_in_tank < 0:
                gas_in_tank = 0
                starting_station = i + 1
        return starting_station