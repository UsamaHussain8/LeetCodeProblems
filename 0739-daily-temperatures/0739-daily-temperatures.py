class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waiting_days = [0] * len(temperatures)
        temp_stack = []

        for day, temperature in enumerate(temperatures):
            while temp_stack and temperature > temp_stack[-1][1]:
                prev_day, prev_temp = temp_stack.pop()
                waiting_days[prev_day] = day - prev_day
            temp_stack.append([day, temperature])
           
        return waiting_days

