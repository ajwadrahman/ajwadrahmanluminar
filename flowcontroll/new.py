# for row in range(1,5):
#     for col in range(1,5):
#         print(col, end="\t")
#     print()
# for row in range(1,5):
#     for col in range(1,5):
#         print(row, end="\t")
#     print()
# for row in range(1,5):
#     for col in range(1,row+1):
#         print(col,end="\t")
#     print()
# for row in range(1,5):
#     for col in range(1,row+1):
#         print(row,end="\t")
#     print()
# for row in range(1,5):
#       for col in range(5,row,-1):
#           print("#",end="\t")
#       print()
      # full pyramid
# rows=5
# k=2*rows-1
# for row in range(0,rows):
#     for col in range(0,k):
#         print(end="")
#     k=k-2
#     for col in range(0,row+1):
#         print("*",end="\t")
#         print("")

# unfinished hollow
row=5

for i in range (row):
    for col in range(row-i):
            print(" ",end=" ")
    for col in range(2*i+1):
        if col==0 or col==2*i or i==row-1:
            print("*", end="\t")
        else:
            print("",end="")
    print()
