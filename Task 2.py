number = int(input('Enter an integer: '))
if number % 2 == 0:
    print("even")
else:
    print("odd")
total = 0

for i in range(1, 51):  # 1 to 50 inclusive
    total += i

print("The sum of integers from 1 to 50 is:", total)



