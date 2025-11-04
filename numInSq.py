n = int(input("Enter the number: "))
for i in range(1,n+1):
    for j in reversed(range(1,n+1)):
        print(j , end=" ")
    print()