# def add_numbers(n1,n2):
#     return n1+n2
# print(add_numbers(10,20))

# def smart_sub(n1,n2):
#     return n1-n2 if n1>n2 else n2-n1
# print(smart_sub(10,20))
# def even_odd(num):
#     return "even" if num %2==0 else "even"
# print(even_odd(20))

# def validate_gmail(email):
#     return email.endswith("gmail")
# print(validate_gmail("aj@gmail"))
#
# def validate_name(name):
#     return name.startswith("a")
# print(validate_name("aju"))

# def fact(num):
#     fact=1
#     for i in range(1,(num+1)):
#         fact=fact*i
#     return (fact)
# print(fact(3))

# true or false prime
# return prime rame low to up

# laamnda
# cube=lambda n:n*3
def prim(num):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag=1
            break
    return True if flag==0 else False


def prime(n1,n2):

    for i in range(n1,n2+1):
        if prim(i):
            print(i)
prime(12,40)

# git and github
# list






