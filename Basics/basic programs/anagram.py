str1=input("enter first string")
str2=input("enter second string")
if len(str1)==len(str2):
    if sorted(str1)==sorted(str2):
        print("givens strings are anagram")
    else:
        print("given strings are not anagram")
else:
    print("given strings are not anagram beacuse the lenght is different and different characters")