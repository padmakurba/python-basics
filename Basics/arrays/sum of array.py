lst = []
n = int(input("enter the total elements u want inside your list"))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print(lst)
print(len(lst))

sum = 0

for i in range(0,len(lst)):
    sum = sum + lst[i]
print(sum)


