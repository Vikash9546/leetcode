class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        n=len(grid)
        m=len(grid[0])
        queue=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    queue.append([i,j,0])

        while queue:
            lis=queue.popleft()
            r=lis[0]
            c=lis[1]
            t=lis[2]
            if t>time:
                time=t

            if (r-1)>=0 and grid[r-1][c]==1:
                queue.append([r-1,c,t+1])
                grid[r-1][c]=2
            if (r+1)<n and grid[r+1][c]==1:
                queue.append([r+1,c,t+1])
                grid[r+1][c]=2

            if (c-1)>=0 and grid[r][c-1]==1:
                queue.append([r,c-1,t+1])
                grid[r][c-1]=2
            if (c+1)<m and grid[r][c+1]==1:
                queue.append([r,c+1,t+1])
                grid[r][c+1]=2

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return time
            