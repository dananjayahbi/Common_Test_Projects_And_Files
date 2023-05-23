A =[]

for k in range(1,10):
    A.append(float(input('Enter student marks : ')))
print(A)

def selectionsort(A):
    n = len(A)
    for j in range(0,n-1):
        smallest=j
        for i in range(j+1,n):
            if(A[i] < A[smallest]):
               smallest = i
        A[j],A[smallest] = A[smallest],A[j]

selectionsort(A)
print(A)


n=len(A)

if(n%2 == 0):
    median = (A[n//2] + A[n//2-1]) /2
    print("Median value of the array A is:", median)
else:
    median = A[n//2]
    print("Median value of the array A is:", median)


range = max(A) - min(A)
print("Range of the array A is:",range)
