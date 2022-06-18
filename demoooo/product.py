mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMOLED", 32000, "samsung", 20],
    [1002, "redminote10", "4g", "led", 17000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung", 89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67]

]
# out of stock
# out_stock = [prdcts for prdcts in mobiles if prdcts[-1] == 0]
# print(out_stock)

# total stock
# ttl_stok = sum([prdcts[-1] for prdcts in mobiles  ])
# print(ttl_stok)

# 20 to 30k
# rage_20 = [prdcts  for prdcts in mobiles if prdcts[4] >= 20000 and prdcts[4] <= 30000]
# print(rage_20)

# 5g
# coverage=[prodcts for prodcts in mobiles if prodcts[2]=="5g"]
# print(coverage)

# sumsung
# sum_phn=[prdct  for prdct in mobiles if prdct[5]=="samsung"]
# print(sum_phn)

# costly
# max_pric=max([prdct[4] for prdct in mobiles])
# cstly_phn=[prdct for prdct in mobiles if prdct[4]==max_pric]
# print(cstly_phn)

# mobiles.sort(reverse=True,key=lambda prdct:prdct[4])
# print(mobiles)


# low cost
# min_pric=min([prdct[4] for prdct in mobiles])
# bdgt_phn = [prdcts for prdcts in mobiles if prdcts[4]==min_pric]
# print(bdgt_phn)
# cost_mob=max(mobiles.sort())

# stock > 10
# stock_ten=[prdct for prdct in mobiles if prdct[-1]>10]
# print(stock_ten)

# count of amoled
# amoled= ([prdct for prdct in mobiles if prdct[3]=="AMOLED"])
# print(len(amoled))

# sort
# mobile_srt = [prdct.sort(-1) for prdct in mobiles ]
# print(mobile_srt)

#avilable 10000 phn
mob_ten=[ prdct[4]==10000  for prdct in mobiles ]
print("yes"if True in mob_ten else "no")

# list of smae price

