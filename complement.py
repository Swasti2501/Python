n = int(input("Enter a number: "))
mask = 1
while mask < n:
    mask = (mask << 1) | 1
print(mask ^ n)