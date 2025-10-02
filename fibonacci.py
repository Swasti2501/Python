n = int(input("Enter the value: "))
last, prev = 0, 1
current = last + prev
for i in range(4,n+1):
    last = prev
    prev = current
    current = last + prev
print(current)
    