n = int(input("Enter the number: "))
i = 1
while i<=n:
    if i%2==0:
        print(i, "is even number.", end=" ")
    else:
        print(i, "is odd number.", end=" ")
    i += 1
    print()