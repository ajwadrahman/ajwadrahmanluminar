tx = "abcdedc"
# word_count={}
# for t in tx:
#     if t in word_count:
#         print("fst recus",t)
#         break
#     else:
#         word_count[t]=1


# word_count = {}
# ric_lst = []
# for t in tx:
#     if t in word_count:
#         ric_lst.append(t)
#     else:
#         word_count[t]=1
# print(ric_lst[1],"sec")


wor={"a":2,"b":2,"c":3,"d":5}
# for v,k in wor.items():
#     print(v,k)
wrd_lst=wor.items()
print(sorted(wrd_lst,key=lambda item:item[1],reverse=True))

# print(min or max(wrd_lst,key=lambda item:item[1]))






