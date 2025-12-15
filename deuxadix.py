def base2tobase10(binary):
    base2 = []
    base10 = 0
    
    for i in str(binary):
        base2.append(i)
        
    base2.reverse()
    
    for i in range(0,len(base2)):
        base10 += int(base2[i])*(2**i)
    print(base10)