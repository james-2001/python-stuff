num = -15
ver = ("prime")
if num < 1:
    return
for i in range (2, ((int(num/2))+1)):
        val = num % i
        if val == 0:
            ver = ("not prime")
            break
print (ver)
