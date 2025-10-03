n = str(input("Enter: "))
palindrome = True
for i in range(len(n)//2):
    if n[i] != n[-i-1]:
        palindrome = False
        break
if palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")        