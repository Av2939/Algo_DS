class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        s = []
        
        for i in intervals:
            s.append((i[0], "start"))
            s.append((i[1], "end"))
            
        
        s.sort()
        count = 0
        res = 0
        
        for time, type in s:
            if type == "start":
                count += 1
                res = max(count, res)
            elif type == "end":
                count -= 1
        return res