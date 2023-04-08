def main(a,b,c):
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    d=0
    if a<0:
        d=1
    if b<0:
        d=d+1
    if c<0:
        d=d+1

    return d
print(main(-1,-2,3))
