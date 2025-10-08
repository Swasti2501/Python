n = int(input("Enter the number to print its factor: "))
i = 1
while i<=n:
    if n%i == 0:
        print(i, end=" ")
    i += 1
print()