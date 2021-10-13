number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
if number1 > number2:
    gap = -1
else: 
    gap = 1 
for index in range (number1, number2 + gap, gap )
    print(index)

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
gap = (number1 - number2) // abs(number1 - number2)
for index in range (number1, number2 + gap, gap):
    print(index)

