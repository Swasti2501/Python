n = int(input("Enter the number: "))
i = 1
sum = 0
while True:
    sum += i
    i += 1
    if i>n:
        break
print(sum)