class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cyclic_index: int = -1
        if sum(gas) < sum(cost):
            return cyclic_index

        starting_station: int = 0
        num_stations:int = len(gas)
        net_fuel: int = 0
        gas_in_tank: int = 0

        for i in range(0, num_stations):
            net_fuel += gas[i] - cost[i]
            gas_in_tank += gas[i] - cost[i]
            if gas_in_tank < 0:
                gas_in_tank = 0
                starting_station = i + 1

        cyclic_index = starting_station if net_fuel >= 0 else -1
        return cyclic_index