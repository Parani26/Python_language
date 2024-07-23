show(fractal(make_cross(rcross_bb), n))

functions
quarter turn right
turn upside down
quarter turn left
stack(,)
beside(,)
show(stack_frac(1/3, rcross_bb, sail_bb))


remb to show evrything
1 base unit: make_cross(rcross_bb)

2 base units: stack_frac(1/2, make_cross(rcross_bb), make_cross(rcross_bb))
           
3 base units stack_frac(2/3,stack_frac(1/2, make_cross(rcross_bb), make_cross(rcross_bb)), make_cross(rcross_bb))

1a)

def fractal(a , n):
    if n == 1:
        return a
    else:
        return stack(a, beside(fractal(a , n-1),fractal(a , n-1))

1b)
def fractal_iter(a,n):
    result = a
    for i in range (2, n+1):
        result = stack(a, beside(result,result))
    return result

#dont need the counter or i in the loopm  



1c)
def dual_fractal(a, b, n):
    if n == 1:
        return a
    elif n == 2:
        return stack(a, beside(b, b))
    else:
        return stack(a, beside(dual_fractal(b, a, (n - 1)), (dual_fractal(b, a, (n - 1)))))

#you can swap the params and apparently it doesnt affect base cases but the recusive fxn only

1d)

def dual_fractal_iter(a, b, n):
    if n % 2 == 0:
        result = b
        for i in range(1, n):
            if i % 2 == 0:
                result = stack(b, beside(result,result))
            else:
                result = stack(a, beside(result,result))
                
    elif n % 2 == 1:
        result = a
        for i in range(1, n):
            if i % 2 == 0:
                result = stack(a, beside(result,result))
            else:
                result = stack(b, beside(result,result))
        
    return result












    




qn2)
mission1

def mosaic(b,c,d,a):
    final = stack(beside(a,b),beside(d,c)) 
    return final


def steps(a,b,c,d):
    level_1 = stack(beside(d,blank_bb),beside(blank_bb,blank_bb))
    level_4 = stack(beside(blank_bb,a),beside(blank_bb,blank_bb))
    level_2 = stack(beside(blank_bb,blank_bb),beside(c,blank_bb))
    level_3 = stack(beside(blank_bb,blank_bb),beside(blank_bb,b))
    level_1_2 = overlay(level_1, level_2)
    level_3_4 = overlay(level_3, level_4)
    final = overlay(level_1_2, level_3_4)
    return final


    overlay, overlay_frac, scale, scale_independent, and translate.
           
        
        
    

