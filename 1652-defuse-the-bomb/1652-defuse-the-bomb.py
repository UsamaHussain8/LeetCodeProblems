class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        code_length: int = len(code)
        sum_code: List[int] = [0] * code_length

        if k == 0:
            return sum_code
        elif k < 0:           
            start = code_length - 1 + k
            k = k * -1
            j = start + k
            summ = sum(code[i] for i in range(start, start+k))
            for i in range(code_length):
                summ -= code[(i + start) % code_length]
                summ += code[j % code_length]
                sum_code[i] = (summ)
                j += 1
                if j == code_length:
                    j = 0
        else:
            sum_code[0] = sum(code[1: k + 1])
            for i in range(1, code_length):
                sum_code[i] = sum_code[i - 1] - code[i] + code[(i + k) % code_length]

        return sum_code