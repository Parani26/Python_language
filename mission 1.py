show(quarter_turn_left(sail_bb))




def simple_fractal(a):
    final = beside(a,stack(a,a)) 
    return final

def mosaic(b,c,d,a):
    final = stack(beside(a,b),beside(d,c)) 
    return final












    

def first_row(a,n):
    return stackn(n, a)

def second_row(a,n):
    return stack_frac((n-1)/n, (stack_frac(1/(n-1),quarter_turn_right(stackn(n-2,a)),a)) , quarter_turn_right(stackn(n-2,a)))

def egyptian(a, n):
    def rfirst_row(a,n):
        return quarter_turn_right(first_row(a,n))
    def rsecond_row(a,n):
        return quarter_turn_right(second_row(a,n))
    return stack_frac((n-1)/n,stack_frac(1/(n-1),rfirst_row(a,n),rsecond_row(a,n)),rfirst_row(a,n))
    



`
make_cross(rcross_bb)





    

    

        
