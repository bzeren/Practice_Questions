## Problem: Given a m x n grid filled with non-negative numbers, 
## find a path from top left to bottom right which minimizes the sum 
## of all numbers along its path. You can only move either down or right at any point in time.

import numpy as np

class Solution(object):
    global lowestSum
    lowestSum = 99999999
    def minPathSum(self, grid):
        """
        type grid: List[List[int]]
        rtype: int
        """
        
        #Convert input into numpy array
        npGrid = np.array(grid)
        
        #Begin recursion
        return self.minPathSumRec(npGrid, 0)
        
    
    def minPathSumRec(self, grid, current_sum):
	global lowestSum
	#print("current grid", grid)
        ##Terminating condition
        _shape = grid.shape #tuple of row,col (dimensions)
        if current_sum + grid[0][0] >= lowestSum:
            return lowestSum
        
        if _shape[0] == 1 and _shape[1] == 1: #terminating condition (bottom right square)
            return current_sum + grid[0][0]
        
        else:
            intermediate = current_sum + grid[0][0]
            #Check neighbors (R, D)

            rowRemovedSum = 999999
            colRemovedSum = 999999
            
            if grid.shape[0] > 1:
                rowRemovedSum = self.minPathSumRec(np.delete(grid, 0, 0), intermediate)
             
            if grid.shape[1] > 1:
                colRemovedSum = self.minPathSumRec(np.delete(grid, 0, 1), intermediate)
            
            _min = min(rowRemovedSum, colRemovedSum)
            lowestSum = _min
            print "lowest:", _min
            return _min            

a = np.array( [[1, 0, 2], [2, 4, 6], [6, 7, 8]])
print(a)
soln = Solution()
print(soln.minPathSum(a))
