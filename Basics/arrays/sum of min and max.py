A=[1, 2, 3 ,4,5]
    if n==1:
        print(A[0])

    if A[0]>A[1]:
        max=A[0]
        min=A[1]
    else:
        max = A[1]
        min = A[0]

    for i in range(2,n):
        if A[i]>max:
            A[i]=max
        elif A[i]<min:
            A[i]=min

