n = int(input("Enter a number: "))
if n <= 0:
    print("False")
else:
    while n > 1:
        if n % 2 != 0:
            print("False")
            break
        n //= 2
    else:
        print("True")