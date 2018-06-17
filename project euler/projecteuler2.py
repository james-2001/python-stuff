print ("Hello, welcome to the fibbonaci multiple summer")
fib1 = 1
fib2 = 2 
total = 0
bound = int(input("what would you like the upper bound to be? "))
multiple = int(input("what would you like the multiple as? "))
while fib2 < bound:
    if fib2 % multiple == 0:
        total += fib2
    fib2 += fib1 
    fib1 = fib2 - fib1 
print (total)