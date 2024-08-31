class Solution:
    def intToRoman(self, num: int) -> str:
        roman_to_int_mapping = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
        special_cases = {900: "CM", 400: "CD", 90: "XC", 40: "XL", 9: "IX", 4: "IV"}
        roman_equivalent: str = ""
        divisors = list(roman_to_int_mapping.keys())
        special_divisors = list(special_cases.keys())
        i: int = 0 
        j: int = 0
        
        while num != 0:
            if str(num).startswith('4') or str(num).startswith('9'): 
                while num // special_divisors[i] == 0:
                    i += 1
                else:  
                    roman_equivalent += special_cases[special_divisors[i]]
                    num = num % special_divisors[i]
                    i += 1
            else:
                while num // divisors[j] == 0:
                    j += 1
                else:
                    quotient: int = num // divisors[j]
                    for k in range(0, quotient):
                        roman_equivalent += roman_to_int_mapping[divisors[j]]

                    num = num % divisors[j]
                    j += 1

        return roman_equivalent
