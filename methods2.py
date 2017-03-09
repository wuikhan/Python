print("----- Program 1-----")
def sum_nums(num1=2, num2=4):
    return num1 + num2
sum = sum_nums(2, 8)  #another way
print(sum)
#output will be 10

print("----- Program 2 -----")
def sum_nums(num1=2, num2=4):
    return num1 + num2
sum = sum_nums()  #another way
print(sum)
#output will be 6

print("----- Program 3 -----")
def sum_nums(num1=2, num2=4):
    return num1 + num2
sum = sum_nums(num1=8, num2=22)  # another way
print(sum)
#output will be 30
