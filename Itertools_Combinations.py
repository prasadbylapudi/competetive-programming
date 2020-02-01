import itertools

Teams_available=['srikakulam','nuzvid','RK valley','Ongole',"IIIT hyderabad"]

result=list(itertools.combinations(Teams_available,r=2))
'''print(result)'''
for team in result:
    print(team)

