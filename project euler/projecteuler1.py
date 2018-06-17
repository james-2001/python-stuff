lim = int(input("what would you like as your upper limit?"))
count = int(input("where would you like to start from?"))
total = 0
while count < lim:
    if count % 3 == 0 or count % 5 == 0:
        total += count
    count += 1
print (total)


