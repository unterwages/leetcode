def addDigits(num):
    while num>9:
        num = num%10+num/10
    return num

print addDigits(19)
