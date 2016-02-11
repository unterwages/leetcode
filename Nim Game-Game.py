import random
stones = random.randint(10, 14)
print "# of stones", stones

def pick(n):
    if n>4 or n<1:
        print "Illegal number"
    else:
        pick(n)
        stones = stones- n
pick(n)
if stones > 0:
    n = int(raw_input("how many do you pick?"))
    pick(n)
else:
    print "you win"


                
