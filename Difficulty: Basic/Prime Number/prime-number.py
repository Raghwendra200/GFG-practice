#User function Template for python3

class Solution:
    def isPrime(self, n):
        if n<2:
            return False
        if n==2:
            return True
        if n%2==0:
            return False
        for i in range(3,int(n**.5)+1,2):
            if n%i==0:
                return False
        
        return True
        # code here


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n = int(input())  # Read the number to check primality

        ob = Solution()
        # Using Python's conditional expression for true/false
        print("true" if ob.isPrime(n) else
              "false")  # Print "true" if prime, else "false"
        print("~")

# } Driver Code Ends