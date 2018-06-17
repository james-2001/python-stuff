import random
counter = 1
stickcounter = 0
switchcounter = 0
doornumber = 3
switchwon= 0
doorcount =0
n= 10000000 #n number of doors you want to try up to
while doorcount < n:
    # loop lots of times...
    while counter < 10000:
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
            switchcounter += 1
        counter += 1
    # find which of the two options had the best results over the simulation
    if switchcounter > stickcounter:
        switchwon += 1
    doorcount +=1

print ("switch won ", switchwon, " times" )
print ("stick won ", (n- switchwon), " times")

