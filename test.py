

def functionTest(maxDigit):
    array = []
    for i in range(maxDigit+1):
        for y in range(maxDigit+1):
            for j in range(maxDigit+1):
                for x in range(maxDigit+1):
                    if (x + j + y + i) == 21:
                        candidato = i*1000 + y*100 + j*10 + x
                        if(candidato > 1000):
                        
                            array.append( candidato )
                        
                        
    return array
    
    
maxDigit = input()
print(functionTest(int(maxDigit)))