from range import MyRange, my_range


print('Class for range iterator implementation')
print(list(MyRange(1, 10, 2)))
print(list(MyRange(10)))
print(list(MyRange(10, 1, -2)))
for i in MyRange(15, 5, -2):
    print(i)


print("Function for range generator implementation")
print(list(my_range(1, 10, 2)))
print(list(my_range(10)))
print(list(my_range(10, 1, -2)))
for i in my_range(15, 5, -2):
    print(i)
