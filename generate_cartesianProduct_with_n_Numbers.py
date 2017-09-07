def cartesian_product(*X):
    if len(X) == 1: #special case, only X1
        return [ (x0, ) for x0 in X[0] ]
    else:
        return [ (x0,)+t1 for x0 in X[0] for t1 in cartesian_product(*X[1:]) ]

n=int(raw_input("Number of times to roll: "))
events=[1,2,3,4,5,6]
prod=[]
for arg in range(n+1):
    prod.append(events)
print cartesian_product(*prod)

