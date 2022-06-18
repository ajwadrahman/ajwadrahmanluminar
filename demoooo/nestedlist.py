lst=[
    [11,20],
    [30,40],
    [50,60],
    [70,80]
]

# for list in lst:
#     for num in list:
#         if num > 16:
#             print(num)
# flat_lst=[]
# for list in lst:
#     for num in list:
#         flat_lst.append(num)
# print(min(flat_lst))

#lit comprihension
flat=[num for sub in lst for num in sub]
# print(flat)
# gt_num=[num for num in flat if num>16]
# print(gt_num)

# odd=[num for num in flat if  num%2!=0]
# print(odd)


# sum_evn=sum([num for num in flat if num%2==0])
# print(sum_evn)

mapped_num=[num+1 if num > 20 else num-1 for num in flat ]
print(mapped_num)

