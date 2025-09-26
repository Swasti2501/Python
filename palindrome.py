n = int(input("Enter a number: "))
if n < 0:
    print("False")
num = n
ans = 0
while num:
    rem = num % 10
    ans = ans * 10 + rem
    num //= 10
if ans == n:
    print("True")
else:
    print("False")