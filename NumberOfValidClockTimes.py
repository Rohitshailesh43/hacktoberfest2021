# You are given a string of length 5 called time, representing the current time on a digital clock in the format "hh:mm". The earliest possible time is "00:00" and the latest possible time is "23:59".

# In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a digit from 0 to 9.

# Return an integer answer, the number of valid clock times that can be created by replacing every ? with a digit from 0 to 9.

 

# Example 1:

# Input: time = "?5:00"
# Output: 2
# Explanation: We can replace the ? with either a 0 or 1, producing "05:00" or "15:00". Note that we cannot replace it with a 2, since the time "25:00" is invalid. In total, we have two choices.
# Example 2:

# Input: time = "0?:0?"
# Output: 100
# Explanation: Each ? can be replaced by any digit from 0 to 9, so we have 100 total choices.
# Example 3:

# Input: time = "??:??"
# Output: 1440
# Explanation: There are 24 possible choices for the hours, and 60 possible choices for the minutes. In total, we have 24 * 60 = 1440 choices.








# SOLUTION:
  
  
  class Solution:
    
    def countTime(self, time: str) -> int:
        
        # [1] if all symbols are digits, there is only 1 valid time
        t = 1
        
        # [2] if minute digits have unknown symbols, they independently
        #     generate additional combinations
        if time[3] == "?": t *= 6
        if time[4] == "?": t *= 10

        # [3] however, digits in the number of hours are not independent
        if time[0:2] == "??":
            t *= 24
        elif time[0] == "?" and time[1] != "?": 
            t *= 2 if time[1] in ["4", "5", "6", "7", "8", "9"] else 3
        elif time[1] == "?" and time[0] != "?": 
            t *= 10 if time[0] in ["0", "1"] else 4
        
        return 
