class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for operation in operations:
            if operation == 'C':
                record.pop()
            elif operation == 'D':
                record.append(record[-1] * 2)
            elif operation == '+':
                record.append(record[-1] + record[-2])
            else:
                record.append(int(operation))
                
        return sum(record) if len(record) > 0 else 0

        return sum(record) if len(record) > 0 else 0