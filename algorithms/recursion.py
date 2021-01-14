'''
- Recursion is a way of programming or coding a problem, in which a function calls itself 
  one or more times in its body.
- Recursion in computer science is a method where the solution to a problem is based on 
  solving smaller instances of the same problem.
'''

# soln 1
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
l = factorial(5)
print(l)



# soln 2

def iterative_factorial(n):
    result = 1
    
    for i in range(2, n+1):
        result *= i  
        return result
    
l = factorial(6)
print(l)



# soln 3

def sum_n(n):
    if n== 0:
        return 0
    else:
        return n + sum_n(n-1)
    
print(sum_n(6))



# soln 4

def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line

print(pascal(6))



# soln 5

def fibonacci(k):
    if k > 0:
        result = k + fibonacci(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
fibonacci(6)