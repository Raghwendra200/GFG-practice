
class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        if n<0:
            return 0
        if n==1:
            return 1
        else:
    
            return n+self.seriesSum(n-1)    



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.seriesSum(n)

        print(res)
        print("~")

# } Driver Code Ends