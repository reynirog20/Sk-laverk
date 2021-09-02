n = int(input("Enter the length of the sequence: ")) 

first_num = 1
second_num = 2
third_num = 3

print(first_num)
print(second_num)
print(third_num)
for i in range(n):
    if i >= 3:
        sum_num = first_num + second_num + third_num
        print(sum_num)
        first_num = second_num
        second_num = third_num
        third_num = sum_num