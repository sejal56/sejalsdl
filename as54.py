def word_count(str):
    count=dict()
    words=str.split()

    for a in words :
        if a in count :
            count[a]+=1
        else :
            count[a]=1
    return count

str1=input("Enter the string")
c=word_count(str1)
print(c)
