import random
counter = 1
stickcounter = 0
switchcounter = 0
doornumber = 10000000
switchwon = 0
n = 100000000000  # n number of doors you want to try up to
while doornumber < n:
    # loop lots of times...
    while counter < 1000:
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
    if stickcounter == 0:
        percentwon = float('inf')
    else:
        percentwon = (switchcounter/stickcounter)
    print(f"{doornumber}, {stickcounter}, {switchcounter}, {percentwon}")
    doornumber += 1
    # reset counter
    counter = 1
    switchcounter = 0
    stickcounter = 0
