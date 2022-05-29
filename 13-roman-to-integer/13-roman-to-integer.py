class Solution:
    def romanToInt(self, s: str) -> int:
        sympols_values = {'I': 1, 'V': 5, 'IX': 9, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        numirc_value = 0
        for i in range(len(s)-1 ,-1, -1):
            if(i< len(s)-1):
                if(sympols_values[s[i]] < sympols_values[s[i+1]]): 
                    numirc_value -= sympols_values[s[i]]
                else: 
                    numirc_value += sympols_values[s[i]]
            else: numirc_value += sympols_values[s[i]]       
        return numirc_value