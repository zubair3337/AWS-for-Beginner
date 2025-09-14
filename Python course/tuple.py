# import sys
# list1=["jerry", 10, "tom", 12.50]
# tuple1=("jerry", 10, "tom", 12.50)
# print("size of list=", sys.getsizeof(list1))
# print("size of tuple=", sys.getsizeof(tuple1))

# import timeit
# listtime=timeit.timeit(stmt="[1,2,3,4,5,6,7,8,]," number=1000000)
# tupletime=timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)", number=1000000)
# Print("list takes time:",listtime)
# Print("tupe take time:",tupletime)


import timeit

listtime = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]", number=1000000)
tupletime = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)", number=1000000)

print("List takes time:", listtime)
print("Tuple takes time:", tupletime)
