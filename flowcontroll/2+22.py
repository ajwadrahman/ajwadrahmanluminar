num=int(input("enter a number"))
i=1
temp=num
sum=0
while(i<=num):
    sum=sum+temp
    temp=(temp*10)+num
    i+=1
print(sum)
num=int(input("enter a number"))
i=1
pattern=""
sum=0
while(i<=num):
    pattern=pattern+str(num)
    sum=sum+int(pattern)
    i+=1
print(sum)
