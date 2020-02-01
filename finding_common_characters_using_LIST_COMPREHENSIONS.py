''' common number finding in two lists using the list comprehensions'''
list_a=['a','b','c','d','e','f']

list_b=['c','d','e','f']
common_nums=[i for i in list_a for j in list_b if i==j]
print(common_nums)
