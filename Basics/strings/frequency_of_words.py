def frequency_of_words():
    str=input("enter a string")
    li=str.split()
    d={}

    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i]+=1
    print(d)

frequency_of_words()