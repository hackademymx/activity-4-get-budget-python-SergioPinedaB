def getTotalBudget(people):
    cont = 0
    
    for person in people:
        cont += person["budget"]
    
    return cont
        
