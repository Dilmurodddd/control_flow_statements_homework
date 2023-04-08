def main(a,b,c):
    """
    Find number of positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    if a>=0:
        a=1
    if b>=0:
        a=a+1
    if c>=0:
        a=a+1

    return a
print(main(1,-2,-3))
