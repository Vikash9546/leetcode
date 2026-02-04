class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos=[0,0]
        for i in moves:
            if i == 'U':
                pos[0]-=1
            elif i=='D':
                pos[0]+=1
            elif i=='R':
                pos[1]+=1
            else:
                pos[1]-=1
        if pos[0] ==0 and pos[1] ==0:
            return True
        return False

        