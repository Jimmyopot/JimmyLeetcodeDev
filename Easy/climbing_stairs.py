'''
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct 
ways can you climb to the top?
'''



'''
DYNAMIC PROGRAMMING

- All about RECURSION => REPETITION! 
- Pattern based, eg, Fibonacci sequence.
- Find a recursive soln, are there repeated states in it?, and store them in a matrix.
  1. Recursion.
  2. Store (Memoize) -  It involves rewriting the recursive algorithm so that as answers to problems are found, they are stored in an array/ dictionary/ hash map.
  3. Bottom-up.
- You see trends in the soln.
- eg, Fibonacci sequence:
  1, 1, 2, 3, 5, 8, 13
  (1+1=2), (1+2=3), (2+3=5), (3+5=8), (5+8=13)
'''   



# soln 1

class Solution(object):
    def climbStairs(self, n):
        if n == 0:
            return 0 
        if n == 1:
            return 1
        if n == 2:
            return 2
          
        hash_map = {1:1, 2:2}  # use hash map to map index with steps
        
        for i in range(3, n+1):  # (n+1) means we need to go 1 step forward to get value of n
            curr = hash_map[i-1] + hash_map[i-2]
            hash_map[i] = curr
            
        return hash_map[n]
      
l = Solution()
print(l.climbStairs(5))



# soln 2

class Solution2(object):
    def climbStairs2(self, n):
        # fibonacci sequence
        # 1:1, 2:2, 3:3, 4:5, 5:8, 6:13, 7:21
        # 1 stair = 1 step, 3 stairs = 3 steps, 7 stairs = 13 steps
        if n == 0 or n == 1:
            return 1
        
        path = {1:1, 2:2, 3:3} # [BOTTOM UP APPROACH]
        
        for x in range(4, n+1):
            path[x] = path[x-1] + path[x-2]
            
        return path[n]
      
l = Solution2()
print(l.climbStairs2(7))
# time complexity = O(n)


