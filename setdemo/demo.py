# lst=[1,3,4,2,5,5,5]
# st=set(lst)
# print(st)
# st1={1,2,3,4}
# st2={3,4,5}
# union_set=st1.union(st2)
# print(union_set)
#
# intersection_set=st1.intersection(st2)
# print(intersection_set)
#
# diff_set=st1.difference(st2)
# print(diff_set)

stdnt=["ram","ravi","aju","raju"]
pass_stdnt=["ram","raju"]
fail_stdnt=set(stdnt ).difference(set(pass_stdnt))


print(fail_stdnt)