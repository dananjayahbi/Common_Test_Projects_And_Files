def sumcube(n):
    if(n==1):
        return 1
    else:
        return(sumcube(n-1) + n * n* n)


while(True):
    n = int(input('Enter an integer number : '))

    if(n==-1):
        break
    else:
        cube = sumcube(n)
        print('The sum of the first ',n,' cubes : ',cube)
