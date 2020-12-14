# soln 1
class Solution(object):
    
    def reverse(self, x):
        # number = 123
        def divide(number, divider):
            return int(number * 1.0 / divider)
        
        def mod(number, m):
            if number < 0:
                return number % -m
            else:
                return number % m
                '''
                remember:
                123 % 10 = 3
                -123 % 10 = 7
                -123 % -10 = 3
                '''
        
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        result = 0
        
        while x:
            pop = mod(x, 10)
            x = divide(x, 10)
            if result > divide(MAX_INT, 10) or (result == divide(MAX_INT, 10) and pop > 7):
                return 0
            if result < divide(MIN_INT, 10) or (result == divide(MIN_INT, 10) and pop < -8):
                return 0
            result = result * 10 + pop
        return result
        
        # TIME COMPLEXITY = O(n)
        # SPACE COMPLEXITY = 0(1)
        
        
        
# soln2 (STRING REVERSE METHOD)

def reverse_integer(x):
    y = str(abs(x))  # converts int x to a string
    y = y.strip()  # strip all leading 0's (e.g, 120-> 21, 1000-> 1)
    y = y[::-1]  # reverses the string
    output = int(y)  # reverses back to INTEGER
    
    if output >= 2 ** 31 -1 or output <= -2 ** 31:
        return 0
    elif x < 0:
        return -1 * output
    else:
        return output
    
print(reverse_integer(-12345))
# TIME COMPLEXITY = O(n)



# soln3

def reverse_signed(num):
    sum = 0
    sign = 1
    
    if num < 0:
        sign = -1
        num = num * -1
        
    while num > 0:
        rem = num % 10
        sum = sum * 10 + rem
        num = num // 10
        
    if not -2147483648 < sum < 2147483648:
        return 0
    return sign * sum

print(reverse_signed(456))