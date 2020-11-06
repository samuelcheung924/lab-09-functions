def factorial(n):
    total = 1
    for i in range(1, n+1):
        #print(i)
        total = total * (i)
    return total

num = int(input("Please enter a number "))
print(f'{num}! is {factorial(num)}')
