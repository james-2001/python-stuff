counter = 0
import random
doornumber= 3
switchcounter =0
stickcounter = 0
while counter < 1000000:
    contdoor = random.randint(1, doornumber)
    prizedoor = random.randint(1, doornumber)
    opendoor = 1

        # find the first door which doesn't have the prize and isn't the one the contestant chose
    while opendoor == prizedoor or opendoor == contdoor:
        opendoor += 1

        # find out whether the contestant would be better off switching or sticking
    if contdoor == prizedoor:
        stickcounter += 1
    else:
        if random.randint(1, doornumber-2) == 1:
            switchcounter += 1
    counter += 1
print ("switch", switchcounter, "stick", stickcounter)