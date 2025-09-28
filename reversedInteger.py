x = int(input("Enter an integer: "))
sign = -1 if x < 0 else 1
x = abs(x)
ans = 0
while x != 0:
    ans = ans * 10 + x % 10
    x //= 10
ans *= sign
if ans < -2**31 or ans > 2**31 - 1:
    ans = 0
print(ans)