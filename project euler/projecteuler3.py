number = 20
val = 0
def primebool(x):
    for i in range (2,int(x/2)):
        val = x % i
    if val == 0:
        primebool = True
    if i == x/2 and val !=0:
        primebool = False
for i in range (2,int(number * 0.5)):
    if number % i == 0:
        val = i
        number = number / val 
        if primebool(val) == True:
            break
print (i)


