''' common number finding in two lists using the list comprehensions'''

list_a=[1,2,3,4,5]

list_b=[5,6,7,1,9]

common_nums=[i for i in list_a for j in list_b if i==j]

print(common_nums)