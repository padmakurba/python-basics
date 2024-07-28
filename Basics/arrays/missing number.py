def get_missing_number(A):
    n=A[-1]
    total=n*(n+1)//2
    sum1=sum(A)
    missing_number=total-sum1
    print(missing_number)

A=[1,3,4,5,6,7,8,9,10]
get_missing_number(A)