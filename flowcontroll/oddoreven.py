 # to find even (num %2==0)
num=15
# if (num%3==1):
#     print("fizz")
# elif (num%5==1):
#     print("buzz")
# elif (num%15==0):
#     print("fizzbuzz")
res=""
if num%3==0:
    res+="fizz"
if num%5==0:
    res+="buzz"

print(res)