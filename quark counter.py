u = [2/3, 0, 1/3]
d = [-1/3, 0, 1/3]
s = []
def antifunction(x):
    return -1 * x 
def chargefunction(x):
    return x[0]
def strangenessfunction(x):
    return x[1]
def baryonfunction (x):
    return x[2]

proton = [u[i] + d[i] + u[i] for i in range (len(u))]
neutron = [u[i] + d[i] + d[i] for i in range (len(u))]

print (chargefunction(antifunction(proton)))
