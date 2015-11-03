__author__ = 'smy'

class Solution(object):
    def maxProfit(self,prices):
        if len(prices)==0:
            return 0
        result = 0
        lastMax = prices[-1]
        for val in reversed(prices[0:len(prices)-1]):
            result = max(lastMax-val,result)
            lastMax = max(lastMax,val)
        return result

    def generateParenthesis(self, n):
        result = [""]
        for i in range(n):
            result[0] += "("
        for i in range(n):
            result[0] += ")"
        for i in range(1,n):
            for j in range(n,2*n-1):
                result.append(result[0][0:i]+")"+result[0][i+1:j]+"("+result[0][j+1:])
        for val in result:
            print val

    def helper(self,grid,endX,endY):
        print endX,",",endY
        if endX == endY and endX == 0:
            return grid[0][0]
        if endX < 0 or endY < 0:
            return 0
        print "no:",endX,",",endY
        return min(self.helper(grid, endX-1, endY)+grid[endX][endY],self.helper(grid,endX,endY-1)+grid[endX][endY])

    def minPathSum(self,grid):
        print len(grid[0])-1,len(grid)-1
        return self.helper(grid,len(grid[0])-1,len(grid)-1)


    def test(self):
        ll = [1,2]
        for i in range(len(ll)):
            print "size:",len(ll),i
            ll.append(3)

solution = Solution()
# solution.generateParenthesis(3)
# print solution.maxProfit([2,1,3])
test = [[1,2,5],[3,2,1]]
# print solution.minPathSum(test)
