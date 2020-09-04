
import math as m

def checkPrime(number):
    if number <= 1:
        return None
    max_int = m.floor(m.sqrt(number))
    for i in range(2,max_int+1):
        if number %i == 0:
           return None
    return number


if __name__ == "__main__":
    a = []
    for i in range(0,250):
        if checkPrime(i) == None:
            continue
        else:
            a.append(checkPrime(i))
    print(a)
    
