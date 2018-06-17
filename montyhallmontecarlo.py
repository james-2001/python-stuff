import random
counter = 1
stickcounter = 0
switchcounter = 0

# loop lots of times...
while counter < 1000:
    contdoor = random.randint(1, 3)
    prizedoor = random.randint(1, 3)
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

print("switch ", switchcounter, " times")
print("stick ", stickcounter, " times")
