#Find out the factorial of a given number n.

print("Enter the value of n:")
n =int(input())
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("The factorial of", n, "is", factorial)
