num1=[1,2,3,6]
# lst=[]
# for i in range(0,len(num1)):
#     for j in range((i+1),len(num1)):
#         if num1[i]==num1[j]:
#             lst.append(num1[i])
# print(lst)

sum=8
for i in range(0,len(num1)):
    for j in range((i+1),len(num1)):
       cur_sum=num1[i]+num1[j]

       if cur_sum == sum:

           print(f"pairs{num1[i]},{num1[j]}")














