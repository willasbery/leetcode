class Solution:
    def addBinary(self, a: str, b: str) -> str:
        diff = abs(len(b) - len(a))
        a = ("0" * diff) + a if len(a) < len(b) else a
        b = ("0" * diff) + b if len(b) < len(a) else b

        ans = ""
        carry = False
        for a_val, b_val in zip(list(a)[::-1], list(b)[::-1]):
            if carry:
                c_val = 1
                carry = False
            else:
                c_val = 0

            digit = int(a_val) + int(b_val) + int(c_val)
            
            if digit == 0:
                ans = "0" + ans
            elif digit == 1:
                carry = False
                ans = "1" + ans
            elif digit == 2:
                carry = True
                ans = "0" + ans
            elif digit == 3:
                carry = True
                ans = "1" + ans

        if carry:
            ans = "1" + ans

        return ans
            



            

            
