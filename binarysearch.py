lst1=[11,22,33,44,55,35,12]
# flag=0
# elemnt=11
# lst.sort()
# low=0
# upp=len(lst)-1
# while(low<=upp):
#     mid=(low+upp)//2
#     if elemnt==lst[mid]:
#         flag=1
#         break
#     elif elemnt > lst[mid]:
#         low=mid+1
#     elif elemnt < lst[mid]:
#         upp=mid-1
# print("found" if flag > 0 else "not found")
lst2=[10,12,34,44,38,55]
lst1.sort()
lst2.sort()
p1=0
p2=0
while(p1<len(lst1) and p2<len(lst2)):
    if lst1[p1]==lst2[p2]:
        print(f"common {lst1[p1]}")
        p1+=1
        p2+=1
    elif lst1[p1]>lst2[p2]:
        p2+=1
    elif lst1[p1]<lst2[p2]:
        p1+=1