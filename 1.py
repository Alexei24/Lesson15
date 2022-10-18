import timeit

print("list: ",timeit.timeit("[1,2,3,4,5,6,7,8,9,10]", number =100000000))
print("tuple: ", timeit.timeit("(1,2,3,4,5,6,7,8,9,10)", number =100000000))