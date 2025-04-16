def enumerate_interval(min, max):
    return list(range(min, max+1))

def map(fn, seq):
    if seq == []:
        return []
    else:
        return [fn(seq[0]),] + map(fn, seq[1:])

def filter(pred, seq):
    if seq == []:
        return []
    elif pred(seq[0]):
        return [seq[0],] + filter(pred, seq[1:])
    else:
        return filter(pred, seq[1:])

def accumulate(fn, initial, seq):
    if seq == []:
        return initial
    else:
        return fn(seq[0], 
                  accumulate(fn, initial, seq[1:]))


# Leave your answers below   
    
def part_i():
    '''code for [1, 2, 3, 4, 5, 6, 7, 8]'''
    return


def part_ii():
    '''code for [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]'''
    return

def part_iii():
    '''code for [1, 9, 25, 49, 81, 121]'''
    return

def part_iv():
    '''code for [1, 1, 9, 2, 25, 3, 49, 4, 81, 5]'''
    return

def part_v():
    '''code for [20, 16, 14, 10, 8, 4, 2]'''
    return


                
