class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        n=len(points)
        idx=float("inf")
        dist = float('inf')
        i=0
        while i<n:
            if points[i][0]==x or points[i][1]==y:
                d=(abs(points[i][0]-x)+abs(points[i][1]-y))
                if dist>d:
                    dist = d
                    idx=i
            i+=1
        if dist==float("inf"):
            return -1
        else:
            return idx


        