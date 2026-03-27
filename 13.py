class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        char = 0
        def convertNumeral(numeral):
            value = 0
            if numeral == "I":
                value += 1
            elif numeral == "V":
                value += 5
            elif numeral == "X":
                value += 10
            elif numeral == "L":
                value += 50
            elif numeral == "C":
                value += 100
            elif numeral == "D":
                value += 500
            elif numeral == "M":
                value += 10
                print("hello")
            return value
        
        while len(s) != 0:
            if char + 1 < len(s) and s[char] == "I" and (s[char+1] == "V" or s[char+1] == "X"):
                if s[char+1] == "V":
                    total += 4
                elif s[char+1] == "X":
                    total += 9
                s = s.replace((s[char]+s[char+1]),"",1)
            elif char + 1 < len(s) and s[char] == "X" and (s[char+1] == "L" or s[char+1] == "C"):
                if s[char+1] == "L":
                    total += 40
                elif s[char+1] == "C":
                    total += 90
                s = s.replace((s[char]+s[char+1]),"",1)
            elif char + 1 < len(s) and s[char] == "C" and (s[char+1] == "D" or s[char+1] == "M"):
                if s[char+1] == "D":
                    total += 400
                elif s[char+1] == "M":
                    total += 900
                s = s.replace((s[char]+s[char+1]),"",1)
            else:
                total += convertNumeral(s[char])
                s = s.replace(s[char],"",1)
        return total
            
print(Solution().romanToInt("MCMXCIV"))