def sum(n):
    if(n==1):
        return 1
    else:
        return(sum(n-1)+n)

while(True):
    n = int(input('Enter an integer number : '))

    if(n==-1):
        break
    else:
        sumval = sum(n)
        print('The sum of the first ',n,' values are : ',sumval)
