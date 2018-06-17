import random
contdoor= random.randint(1,3)
prizedoor= random.randint(1,3)
opendoor = random.randint(1,2)
while opendoor == prizedoor or opendoor == contdoor or opendoor == 0:
    opendoor += random.randint (10,100)
    opendoor = (opendoor % 4)
print(contdoor)
print(prizedoor)
print(opendoor)



if contdoor + opendoor == 3:
            contdoor = 3
            break
        if contdoor + opendoor == 4:
            contdoor = 2
            break
        if contdoor + opendoor == 5:
            contdoor = 1
            break