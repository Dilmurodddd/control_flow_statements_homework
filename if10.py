def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    a="Freezing"
    b="Very Cold"
    c="Cold"
    d="Normal"
    e="Hot"
    f="Very Hot"
    s=''
    if temp==0:
        s=a
    if temp>=1 and temp<=10:
        s=b
    if temp>=11 and temp<=20:
        s=c
    if temp>=21 and temp<=30:
        s=d
    if temp>=31 and temp<=40:
        s=e
    if temp>=41 and temp<=100:
        s=f

    return s
print(main(2))
