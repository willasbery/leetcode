class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        for i in range(len(temperatures)):
            found = False

            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    output.append(j - i)
                    found = True
                    break
            
            if not found:
                output.append(0)
        
        return output
                    
