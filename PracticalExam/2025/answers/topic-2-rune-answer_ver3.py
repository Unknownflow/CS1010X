from runes import *

def side(pic, n):
    if n==1:
        return pic
    else:
        return stack_frac(1/n, pic, side(pic, n-1))

def top(pic, n):
    return ( quarter_turn_right(side(quarter_turn_left(pic), n)))

def center_pic( pic1, pic2):
    return beside(stack(pic1, pic2), stack(pic2, pic1))

def egyptian_with_corners ( ribbon_pic, center_pic, n):
    n_minus_2 = n - 2
    temp_pic = stack_frac( 1/(n_minus_2+1), top(ribbon_pic, n_minus_2), center_pic)
    temp_pic = stack_frac( (n-1)/n, temp_pic, top(ribbon_pic, n_minus_2))

    t_pic = ( stack_frac( 1/(n_minus_2+1), center_pic, \
                        side(ribbon_pic, n_minus_2)))
    t_pic = quarter_turn_left(stack_frac( (n-1)/n, t_pic, center_pic ))
    
    
    temp_pic = stack_frac( 1/(n_minus_2+1), t_pic, \
                            quarter_turn_left(temp_pic))
    temp_pic = stack_frac( (n-1)/n, temp_pic, t_pic)
    temp_pic = quarter_turn_right(temp_pic)
    return temp_pic

