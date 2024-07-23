1a)
def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result , f(i))
    return result

def smiley_sum(t):
    def f(x):
        if x == 0:
            return 0
        if x == t:
            return 1
        elif x < t:
            return (t + 1 - x) ** 2
        elif x > t:
            return (x - t + 1) ** 2
    
    def op(x, y):
        return x + y
        
    n = 2 * t
    
    # Do not modify this return statement
    return combine(f, op, n)

1b)
def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result , f(i))
    return result

def new_fib(n):
    def f(x):
        # answer here
        return x
        
    def op(x, y):
        # answer here
        if x == 0 or x == 1:
            return x
        else:
            return op(x-1, y) + op(x-2, y)
        
    # do not modify this return statement
    return combine(f, op, n+1)
