''' common number finding in two lists using the list comprehensions'''
list_a=['darling','prabhas','prasad','munna','bahubali']
list_b=['bahubali','prasad','prabhas']
common_nums=[i for i in list_a for j in list_b if i==j]
print(common_nums)
