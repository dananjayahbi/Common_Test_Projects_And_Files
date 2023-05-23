def power(base,exp):
    if(exp == 0):
        return 1
    else:
        return base * power(base,exp-1)

while(True):
    base = int(input('Enter the value for X : '))
    exp = int(input('Enter the value for n : '))

    if(base == -1):
        break
    else:
        p = power(base,exp)
        print('The ',exp,' power of ',base,' is : ',p) 
