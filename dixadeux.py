def base10tobase2(decimal):
    base2 = []
    
    while decimal // 2 != 0:
        base2.append(decimal % 2)
        decimal = decimal // 2
    if decimal == 1:
        base2.append(decimal % 2)
    base2.reverse()
    return(base2)