lst=[20,21,22,34,56,2,3,5,6]
lst.sort()
element=56
low=0
upp=len(lst)-1
while(low<upp):
    cur_sum=lst[low]+lst[upp]
    # print(cur_sum)
    if element==cur_sum:
        print(f"pairs {lst[upp]},{lst[low]}")
        break

    elif cur_sum >element:
        upp-=1
    elif cur_sum < element:
        low+=1